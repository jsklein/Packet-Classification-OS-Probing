1. The diff serv config files are used for the router in GNS3 .
2. server.py - create two copies of server and ruh them on two different ports on c2.
3. Now using scapy send packets to the c2 from c1.


Router configaration 

class-map match-all gold
 match ip dscp af12
class-map match-all bronze
 match ip dscp af11

policy-map kt
 class gold
  bandwidth percent 70
 class bronze
  bandwidth percent 5
