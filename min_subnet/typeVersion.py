class TypeVersion():
    def __init__(self, max_bit_depth, fun_address, fun_network):
        self._max_bit_depth_ = max_bit_depth
        self._fun_address_ = fun_address
        self._fun_network_ = fun_network

    def get_ip_to_int(self, ip):
        return int(self._fun_address_(ip))

    def get_ip_to_bin(self, ip):
        return bin(self.get_ip_to_int(ip))

    def get_ip(self, ip):
        return self._fun_address_(ip)

    def get_max_bit_depth(self):
        return self._max_bit_depth_

    def get_fun_network(self):
        return self._fun_network_


