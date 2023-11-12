from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Host, OVSKernelSwitch
from mininet.link import TCLink
import time
import random

class MyTopo( Topo ):

    # Sets up the topology: Single - Topology
    # With N host, and 1 switch
    def build(self, num_hosts):
        #  Loop throught the for loop and then self define
        #  the then link each host to the switch using the for loop
        s1 = self.addSwitch('s1')
        for i in range(1, num_hosts + 1):
            host = self.addHost('h{}'.format(i))
            self.addLink(host, s1)

    #  This is the algorthim for the sjf,
    #  So i created a list of jobs, and assign a rand. excution time for each host
    #  then it gets sorted, so that the shortest excution time gets sorted first for the host
    #  Basically shortest excution time, then the host with that packet gets sent first
def sjf_scheduling(hosts):
    jobs = [(host, random.randint(1, 100)) for host in hosts] 
    jobs.sort(key=lambda x: x[1])
    return [job[0] for job in jobs]

    # Sets up the topology, hots, switch, and links
    # then it simulates the packets being sent to out
    # and gets the excution time and end time 
def run_sjf(num_hosts):
    topo = MyTopo(num_hosts=num_hosts)
    net = Mininet(topo=topo, host=Host, switch=OVSKernelSwitch, link=TCLink)
    net.start()

    #  Store the list of host into a host_list
    host_list = [net.get('h{}'.format(i)) for i in range(1, num_hosts + 1)]

    #  Loops through the list and inform us that the host has started
    for host in host_list:
        host.cmd("Job {} started".format(host.name))

    #  Calls the function, sorts the excution 
    ordered_jobs = sjf_scheduling(host_list)

    #  So this for loop runs through the list of jobs from the function
    #  Then it keeps track of the excution time and end time
    #  Using that we can get the time it was excuted and recieved to get the latency
    for job in ordered_jobs:
        start_time = time.time()
        job.cmd("Executing {}".format(job.name))
        end_time = time.time()
        execution_time = end_time - start_time
        job.cmd("Job completed on {}".format(job.name))
        print("Execution time for {} is {} seconds".format(job.name, execution_time))
    net.stop()

if __name__ == '__main__':
    num_hosts = 5  
    run_sjf(num_hosts)

