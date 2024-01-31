# Networking_2_project
#  #

## Short Introduction ##


## Project Description: ##


### Project Description: ###

#### Example B: How to Run ####

1. Enabling Ryu controller to load the application and to run in the background:
```bash
$ ryu-manager sdn_controller.py &
```

2. Starting the network with Mininet: 
```bash
$ sudo python3 my_network_B.py
```

*Note 1:* Please stop the running Ryu controller before starting a new Ryu controller. For example, type `htop` in the terminal to show all running processes, press the key `F4` to look for the process *ryu-manager*, then press the key `F9` to stop the process, with the key `F10` to quite `htop`.

*Note 2:* When you want to stop the mininet, please delete the topology as follows:
```bash
mininet> exit
$ sudo mn -c
```

#### How to Verify ####

Add a new topology contained in the file text network_topology_B.txt: 
```bash
$ sudo python3 cli_application.py add -t .\network_topology_B.txt
```
There is no active slice is active and therefore the network is completely stopped.

1. ping mode: verifying connecitvity, e.g.:
```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> X X X X X 
h2 -> X X X X X 
h3 -> X X X X X 
h4 -> X X X X X
h5 -> X X X X X
h6 -> X X X X X
*** Results: 100% dropped (0/30 received)
```

Then add a slice and activate it. For example, add slice_one_topology_B.txt. When it asks, enter the id representing the slicer two from the keyboard, for example 123.

```bash
$ sudo python3 cli_application.py add -s .\slice_one_topology_B.txt
```
```bash
$ sudo python3 cli_application.py activate -s .\slice_one_topology_B.txt
```

Verify the isolation of the slice in Mininet with pingall command. Then verify bandwidth between host with iperf mode.

1. pingall mode: verifying slice_one_topology_B isolation:
*Example B: slice_one_topology_B activated* 
```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> X X h4 h5 X 
h2 -> X X X X X 
h3 -> X X X X X 
h4 -> h1 X X h5 X
h5 -> h1 X X h4 X
h6 -> X X X X X
*** Results: 80% dropped (6/30 received)
```

2. iperf mode: verifying slice_one_topology_B bandwidth:
*Example B: slice_one_topology_B activated* 
```bash
mininet> iperf h1 h4
*** Iperf: testing TCP bandwidth between h1 and h4 
*** Results: ['2.83 Mbits/sec', '3.90 Mbits/sec']
mininet> iperf h1 h5
*** Iperf: testing TCP bandwidth between h1 and h5 
*** Results: ['765 Kbits/sec', '990 Kbits/sec']
mininet> iperf h5 h4
*** Iperf: testing TCP bandwidth between h5 and h4
*** Results: ['756 Kbits/sec', '973 Kbits/sec']
```

Then, add the other slice: slice_two_topology_B.txt. When it asks, enter the id representing the slicer two from the keyboard, for example 234.

```bash
$ sudo python3 cli_application.py add -s .\slice_two_topology_B.txt
```
If you want to visualize the actual configuration of the network use the commando show.
```bash
$ sudo python3 cli_application.py show
```
It should show:

```
Network_topology: network_topology_B.txt
HostToRouter
(h1,s1)
(h2,s2)
(h3,s3)
(h4,s3)
(h5,s4)
(h6,s4)
RouterToRouter
(s1-eth1,s4-eth1)
(s1-eth2,s2-eth1)
(s3-eth1,s2-eth2)
Slices:
slice_name:slice_one_topology_B.txt     slice_id:123    slice_state:True
slice_topology:
HostToRouter
(h1,s1)
(h4,s3)
(h5,s4)
RouterToRouter
(s1-eth1-10,s4-eth1-10)
(s1-eth2-50,s2-eth1-50)
(s3-eth1-50,s2-eth2-50)
slice_name:slice_two_topology_B.txt     slice_id:234    slice_state:False
slice_topology:
HostToRouter
(h2,s2)
(h3,s3)
(h6,s4)
RouterToRouter
(s1-eth1-50,s4-eth1-50)
(s1-eth2-50,s2-eth1-50)
(s3-eth1-10,s2-eth2-10)
```

Then, activate the slice_two_topology_B.
```bash
$ sudo python3 cli_application.py activate -s .\slice_two_topology_B.txt
```
Verify the isolation of the slice in Mininet with pingall command. Then verify bandwidth between host with iperf mode.

1. pingall mode: verifying slice_two_topology_B isolation:
*Example B: slice_one_topology_B and slice_two_topology_B activated* 
```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> X X h4 h5 X 
h2 -> X h3 X X h6 
h3 -> X h2 X X h6
h4 -> h1 X X h5 X
h5 -> h1 X X h4 X
h6 -> X h2 h3 X X
*** Results: 60% dropped (12/30 received)
```

2. iperf mode: verifying slice_two_topology_B bandwidth:
*Example B: slice_two_topology_B activated* 
```bash
mininet> iperf h2 h3
*** Iperf: testing TCP bandwidth between h2 and h3 
*** Results: ['1.40 Mbits/sec', '1.73 Mbits/sec']
mininet> iperf h6 h2
*** Iperf: testing TCP bandwidth between h6 and h2 
*** Results: ['2.88 Mbits/sec', '3.97 Kbits/sec']
mininet> iperf h3 h6
*** Iperf: testing TCP bandwidth between h3 and h6
*** Results: ['1.27 Mbits/sec', '1.60 Mbits/sec']
```


## Implementation Details ##

### Contributing

The Contributors of this project are the following:
- Luca Caccavale: luca.caccavale@studenti.unitn.it


