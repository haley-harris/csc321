import netifaces
import ipaddress


def get_interfaces():
    """
    Returns a list of your computer's IP configuration:

    ['lo0', 'gif0', 'stf0', 'XHC20', 'en0', 'p2p0', 'awdl0',
     'en1', 'bridge0', 'utun0']
    """
    interfaces = netifaces.interfaces()
    return interfaces


def get_mac(interface):
    """
    returns MAC address for given interface

    example:

    get_mac('p2p0')

    returns 03:98:cc:d5:6e:cb
    """

    link_layer_interfaces = netifaces.interfaces()

    if interface in link_layer_interfaces:

        address = netifaces.ifaddresses(interface)

        if address != {}:
            mac_addrs = address[netifaces.AF_LINK]
            mac_address = mac_addrs[0]
            return mac_address.get('addr')
        else:
            print('MAC address does not exist for this interface')


def get_ips(interface):
    """
    For the given interface string, return a dictionary with
    the IPv4 and IPv6 address objects for that interface

    The 'en0' interface returns the following ipv4 and ipv6 addresses

      {'v4': ipaddress.IPv4Address('192.168.1.100'),
       'v6': ipaddress.IPv6Address('fe80::c72f:5a4b:9e93:d93d%utun0')}
    """

    link_layer_interfaces = netifaces.interfaces()

    ipv_dict = {}

    for interface in link_layer_interfaces:
        address = netifaces.ifaddresses(interface)

        if netifaces.AF_INET in address.keys():
            ip_addr = address[netifaces.AF_INET]
            ip4_address = ip_addr[0]['addr']
            ipv_dict['v4'] = f"ipaddress.IPv4Address('{ip4_address}')"
        if netifaces.AF_INET6 in address.keys():
            ip_addr = address[netifaces.AF_INET6]
            ip6_address = ip_addr[0]['addr']
            ipv_dict['v6'] = f"ipaddress.IPv6Address('{ip6_address}')"
        
    return ipv_dict


def get_netmask(interface):
    """
    returns a dictionary with the IPv4 and IPv6 netmask objects 
    (as IPv4/v6Address objects) for that interface

    Example:
      get_netmask('en0')

    Returns:
      {'v4': ipaddress.IPv4Address('255.255.255.0'),
       'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::/64')}
    """

    link_layer_interfaces = netifaces.interfaces()

    netmask_dict = {}

    for interface in link_layer_interfaces:
        address = netifaces.ifaddresses(interface)

        if netifaces.AF_INET in address.keys():
            ip_addr = address[netifaces.AF_INET]
            ip4_netmask = ip_addr[0]['netmask']
            netmask_dict['v4'] = f"ipaddress.IPv4Address('{ip4_netmask}')"
        if netifaces.AF_INET6 in address.keys():
            ip_addr = address[netifaces.AF_INET6]
            ip6_netmask = ip_addr[0]['netmask']
            netmask_dict['v6'] = f"ipaddress.IPv6Address('{ip6_netmask}')"

    return netmask_dict


def get_network(interface):
    """
    return a dictionary with the IPv4 and IPv6 network objects 
    for that interface

    Example
      get_network('en0')

    Returns
      {'v4': ipaddress.IPv4Network('192.168.1.100/32')}
    """

    link_layer_interfaces = netifaces.interfaces()
    address = netifaces.ifaddresses(interface)

    network_dict = {}

    ip4_addr = address[netifaces.AF_INET]
    ip4_address = ip4_addr[0]['addr']
    ip4_network = ipaddress.IPv4Network(ip4_address)
    network_dict['v4'] = f"ipaddress.IPv4Network('{ip4_network}')"

    ip6_addr = address[netifaces.AF_INET6]
    ip6_address = ip6_addr[0]['addr']
    # ip6_network = ipaddress.IPv6Network(ip6_address)
    print(network_dict)
    return network_dict
