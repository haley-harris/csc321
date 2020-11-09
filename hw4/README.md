

Command to create file of only hostnames:

`cat domains.tsv | tail -n+2 | cut -f 2 >> hostnames.txt`

Iterate over hostnames and run host command on each

`cat hostnames.txt | while read name; do host ${name}; echo ${name}; done`

Finds the domain name servers of IPv4 address

`cat hostnames.txt | while read name; do host ${name}; echo ${name}; done | grep 'has address' | cut -d ' ' -f 4 | while read ip; do host ${ip}; done | grep 'domain name pointer' | awk '{print $5}' | rev | cut -c2- | rev >> domains.txt`

* ` rev | cut -c2- | rev` reverses string, cuts the 'first' (last) character - the `.` and reverses it back to original state

Hostnames + IPv4 addresses

`cat hosts_adds.txt | grep 'has address' |awk '{print $1, $4}'  >> hostname_and_ip.txt`

Domain name servers + IPv4 addresses

`cat domains.txt | while read name; do host ${name}; done | grep 'has address' | awk '{print $1, $4}' >> domain_and_ip.txt`