
## Parsing relevant packets out of a full-take pcap file
-----------------------------------------------------------------------

before running python server and client scripts, first run tcpdump on each node and create pcap files for each:
    
    tcpdump -i eth0 -w {client/server}.pcap


to read contents of pcap file use: 

    tcpdump -r {client/server}.pcap 


to get info about packets in wireshark run: 

    wireshark {client/server/full-take}.pcap

* use `tcp.port eq {portnumber}` in the wireshark display filter bar to show packets sent to and from a specified port 
* weather update port: 5556
* task ventilator ports: 5557 and 5558


to merge weather update and task vent pcap files into a full take pcap file run 

    mergecap -F pcap -w full-take.pcap wuserver.pcap wuclient.pcap taskvent.pcap taskwork.pcap tasksink.pcap


read the full-take pcap file and filter by given port number(s) to separate weather update packets from task ventilator packets into their own pcap files:

    tcpdump -r full-take.pcap -w {filename}.pcap port {portnumber} or {portnumber}

