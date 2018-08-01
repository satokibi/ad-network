#create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red
$ns color 3 Green
$ns color 4 Yellow
$ns color 5 Brown
$ns color 6 Black

#Open the trace file
set tf [open ad-kadai6_2_5.log w]
$ns trace-all $tf

#Open the nam trace file
set nf [open ad-kadai6_2_5.nam w]
$ns namtrace-all $nf

#Open the tcp trace file
set tcpf [open ad-kadai6_2_5.tcp w]
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

#Create five nodes
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

#Create a Null agent (a traffic sink) and attach it to node n4
set null0 [new Agent/Null]
$ns attach-agent $n4 $null0

set startmain 1.0
set stopmain  25.0

##### Main flow
#Create a UDP agent and attach it to node n0
# and Create a CBR traffic source and attach it to udp0
set udp0 [new Agent/UDP]
$udp0 set class_ 1
$ns attach-agent $n0 $udp0

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0

#Connect the traffic sources with the traffic sink
$ns connect $udp0 $null0  

#Schedule events for the CBR agents
$ns at $startmain "$cbr0 start"
$ns at $stopmain  "$cbr0 stop"

##### Sub flow (TCP/FTP)

set starttm $startmain
set stoptm $stopmain

foreach i {2 3 4 5 6} { 

#Create a TCP agent and attach it to node n1,
#Create a TCPSink agent and attach it to node n5,
# and Create a FTP traffic source and attach it to ftp
set tcp [new Agent/TCP/Reno]
$tcp set class_ $i+2
$tcp set packetSize_ 1500
$tcp trace cwnd_
$tcp attach-trace $tcpf
$ns attach-agent $n1 $tcp
set tcpsink [new Agent/TCPSink]
$ns attach-agent $n5 $tcpsink
$ns connect $tcp $tcpsink

set ftp [new Application/FTP]
$ftp attach-agent $tcp

#Schedule events for the FTP agents
set starttm [expr {$starttm + 1.5}]
set stoptm  [expr {$stoptm - 1.5}]
$ns at $starttm "$ftp start"
$ns at $stoptm  "$ftp stop"

}

#Call the finish procedure after 35 seconds of simulation time
$ns at 35.0 "finish"

#Run the simulation
$ns run

