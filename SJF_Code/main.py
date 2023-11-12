from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink
import time

class MyTopo( Topo ):

    def build( self ):

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        s1 = self.addSwitch( 's1' )
        
        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

def run_sjf():
    topo = MyTopo()
    net = Mininet(topo=topo, host=Host, switch=OVSKernelSwitch, link=TCLink)
    net.start()
    h1, h2, h3 = net.get('h1', 'h2', 'h3')


    s_sent = time.time()    #temp for recording the time when a packet is sent
    h1.cmd('echo "Job 1 started"')
    e_end = time.time()    #temp for recording time when packet recieved 

    s_sent1 = time.time()    #temp for recording the time when a packet is sent
    h2.cmd('echo "Job 2 started"')
    e_end1 = time.time()    #temp for recording time when packet recieved 

    s_sent2 = time.time()    #temp for recording the time when a packet is sent
    h3.cmd('echo "Job 3 started"')
    e_end2 = time.time()    #temp for recording time when packet recieved 


    #  so this portion is to calcuate the completion time
    #  so that i can figure out the tail-latency
    total_time = e_end - s_sent
    total_time1 = e_end1 - s_sent1
    total_time2 = e_end2 - s_sent2

    
    print("Completion time for h1: {} seconds".format(total_time))
    print("Completion time for h2: {} seconds".format(total_time1))
    print("Completion time for h3: {} seconds".format(total_time2))
    

    net.stop()

if __name__ == '__main__':
    run_sjf()

