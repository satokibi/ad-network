#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red

#Open the trace file
set tf [open ad-kadai4-2-2.log w]
$ns trace-all $tf

#Open the nam trace file
set nf [open ad-kadai4-2-2.nam w]
$ns namtrace-all $nf

#Open the tcptrace file
set tcpf [open ad-kadai4-2-2.tcp w]
Agent/TCP set trace_all_oneline_ true


#Define a 'finish' procedure
proc finish {} {
        global ns tf nf tcpf
        $ns flush-trace
	#Close the trace files
        close $tf
        close $nf
	close $tcpf
        exit 0
}

#Create four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n3 $n5 1Mb 10ms DropTail


$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n3 $n5 orient right-down

#Monitor the queue for the link between node 2 and node 3
$ns duplex-link-op $n2 $n3 queuePos 0.5

#LossModule
set lrate 0.01
set loss_module [new ErrorModel]
$loss_module unit pkt
$loss_module set rate_ $lrate
$loss_module ranvar [new RandomVariable/Uniform]
$loss_module drop-target [new Agent/Null]
#$ns lossmodel $loss_module $n1 $n2

##### TCP Flow(Main Flow) Node0 --> Node4
#Create a Null agent (a traffic sink) and attach it to node n4
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink

set tcp [new Agent/TCP/Reno]
$tcp set class_ 1
$ns attach-agent $n0 $tcp
$tcp trace cwnd_
$tcp attach-trace $tcpf
$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp

###### UDP/CBR Flow(Sub Flow) Node1 --> Node5
set udp0 [new Agent/UDP]
$udp0 set class_ 2
$ns attach-agent $n1 $udp0
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0 

set null [new Agent/Null]
$ns attach-agent $n5 $null

$ns connect $udp0 $null

#Schedule events for the CBR agents
set starttcp 1.0 
set stoptcp  15.0
set startudp 5.0
set stopudp  10.0
$ns at $starttcp "$ftp start"
$ns at $stoptcp  "$ftp stop"

$ns at $startudp "$cbr0 start"
$ns at $stopudp "$cbr0 stop"

#Call the finish procedure after 20 seconds of simulation time
$ns at 20.0 "finish"

#Run the simulation
$ns run

