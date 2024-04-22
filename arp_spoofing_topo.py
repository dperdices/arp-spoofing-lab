from mininet.topo import Topo
from mininet.net import Mininet
from mininet.nodelib import NAT
from mininet.node import Node
from mininet.cli import CLI
from mininet.term import makeTerms, makeTerm

class DisableIPv4Forwarding( Node ):
    def config( self, **params ):
        super( DisableIPv4Forwarding, self).config( **params )
        self.cmd( 'sysctl -w net.ipv4.ip_forward=0' )

class ARPSpoofingTopo( Topo ):
    # pylint: disable=arguments-differ
    def build( self, **_opts ):

        # Switch para la red 10.0.0.0/8    
        s = self.addSwitch("s1")

        # Router de la red 10.0.0.0/8
        router = self.addNode('router', cls=NAT, ip="10.0.0.1/8", inNamespace=False )
        self.addLink(s, router)
        
        # Cliente que va a ser atacado
        client = self.addHost("client", ip="10.0.1.1/8", defaultRoute='via 10.0.0.1')
        self.addLink(s, client, intfName2='client-eth0',
                      params2={ 'ip' : "10.0.1.1/8" } )

        # Atacante 
        attacker = self.addHost("attacker", cls=DisableIPv4Forwarding, ip="10.0.1.2/8", defaultRoute='via 10.0.0.1')
        self.addLink(s, attacker, intfName2='attacker-eth0',
                      params2={ 'ip' : "10.0.1.2/8" })
        

topo = ARPSpoofingTopo( )
net = Mininet(topo)

def disableIPv6(net):
    for h in net.hosts:
        h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    for sw in net.switches:
        sw.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")


net.start()
disableIPv6(net)
makeTerms(net.hosts, term="xterm")
CLI(net)
net.stopXterms()

net.stop()