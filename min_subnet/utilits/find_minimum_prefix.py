import ipaddress

def find_minimum_prefix(ip_addresses, max_bit_depth):
    for i in range(max_bit_depth, 0, -1):
        subnet = ipaddress.ip_network(ip_addresses[0] + '/' + str(i), strict=False)
        if all(ipaddress.ip_address(ip) in subnet for ip in ip_addresses):
            return i
    return max_bit_depth