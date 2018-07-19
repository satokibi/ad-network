#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red

#Open the trace file
set tf [open ad-kadai2.log w]
$ns trace-all $tf

#Open the nam trace file
set nf [open ad-kadai2.nam w]
$ns namtrace-all $nf

#Open the tcptrace file
set tcpf [open ad-kadai2.tcp w]
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

#Create links between the nodes
$ns duplex-link $n0 $n1 10Mb 10ms DropTail
$ns duplex-link $n1 $n2 5Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail


$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n1 $n2 orient right
$ns duplex-link-op $n2 $n3 orient right

#Monitor the queue for the link between node 2 and node 3
$ns duplex-link-op $n0 $n1 queuePos 0.5
$ns duplex-link-op $n1 $n2 queuePos 0.5

##### TCP Flow
#Create a Null agent (a traffic sink) and attach it to node n3
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink

set tcp [new Agent/TCP/Reno]
$tcp set class_ 1
$ns attach-agent $n0 $tcp
$tcp trace cwnd_
$tcp attach-trace $tcpf
$ns connect $tcp $sink

set ftp [new Application/FTP]
$ftp attach-agent $tcp

#Connect the traffic sources with the traffic sink

#Schedule events for the FTP agents
set starttm 1.0 
set stoptm  15.0
$ns at $starttm "$ftp start"
$ns at $stoptm  "$ftp stop"

#Call the finish procedure after 20 seconds of simulation time
$ns at 20.0 "finish"

#Run the simulation
$ns run

