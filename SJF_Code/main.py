from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink

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
    net.stop()

if __name__ == '__main__':
    run_sjf()

