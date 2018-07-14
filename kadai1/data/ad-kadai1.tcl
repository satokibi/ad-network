#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows
$ns color 1 Blue
$ns color 2 Red

#Open the trace file
set tf [open ad-kadai1.log w]
$ns trace-all $tf

#Open the nam trace file
set nf [open ad-kadai1.nam w]
$ns namtrace-all $nf

#Define a 'finish' procedure
proc finish {} {
        global ns tf nf
        $ns flush-trace
	#Close the trace files
        close $tf
        close $nf
        exit 0
}

#Create four nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]

#Create links between the nodes
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
#$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n2 0.5Mb 10ms DropTail

$ns duplex-link-op $n0 $n1 orient right
$ns duplex-link-op $n1 $n2 orient right

#Monitor the queue for the link between node 2 and node 3
$ns duplex-link-op $n0 $n1 queuePos 0.5
$ns duplex-link-op $n1 $n2 queuePos 0.5

#Create a Null agent (a traffic sink) and attach it to node n3
set null0 [new Agent/Null]
$ns attach-agent $n2 $null0

set starttm 1.0 
set stoptm  15.0

##### flow 1
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
$ns at $starttm "$cbr0 start"
$ns at $stoptm  "$cbr0 stop"


#Call the finish procedure after 20 seconds of simulation time
$ns at 20.0 "finish"

#Run the simulation
$ns run

