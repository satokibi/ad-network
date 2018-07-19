#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red

#Open the trace file
set tf [open ad-kadai4-1-2.log w]
$ns trace-all $tf

#Open the nam trace file
set nf [open ad-kadai4-1-2.nam w]
$ns namtrace-all $nf

#Open the tcptrace file
set tcpf [open ad-kadai4-1-2.tcp w]
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

##### UDP/FTP Flow
#Create a Null agent (a traffic sink) and attach it to node n3
set null0 [new Agent/Null]
$ns attach-agent $n4 $null0

set udp0 [new Agent/UDP]
$udp0 set class_ 1
$ns attach-agent $n0 $udp0

set cbr0 [new Application/Traffic/CBR]

$cbr0 attach-agent $udp0

$ns connect $udp0 $null0

###### UDP/CBR Flow at Node1
set udp1 [new Agent/UDP]
$udp1 set class_ 2
$ns attach-agent $n1 $udp1

set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500
$cbr1 set interval_ 0.005

$cbr1 attach-agent $udp1 

##### UDP Null at Node5
set null1 [new Agent/Null]
$ns attach-agent $n5 $null1

$ns connect $udp1 $null1

#Schedule events for the CBR agents
set startudp0 1.0 
set stopudp0  15.0
set startudp1 5.0
set stopudp1  10.0
$ns at $startudp0 "$cbr0 start"
$ns at $stopudp0  "$cbr0 stop"

$ns at $startudp1 "$cbr1 start"
$ns at $stopudp1 "$cbr1 stop"

#Call the finish procedure after 20 seconds of simulation time
$ns at 20.0 "finish"

#Run the simulation
$ns run

