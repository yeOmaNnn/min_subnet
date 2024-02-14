import ipaddress
from typeVersion import TypeVersion
from utilits.find_minimum_prefix import find_minimum_prefix


def find_common_network(ip_addresses, typeVesionIp: TypeVersion):
    # Преобразуем IP-адреса в числовой формат
    ips = [typeVesionIp.get_ip_to_int(ip_address) for ip_address in ip_addresses]

    # Находим общую сеть используя битовую маску
    common_network = ips[0] & ips[1]
    for ip in ips[2:]:
        common_network = common_network & ip

    # Преобразуем результат обратно в строку IP-адреса
    common_network_str = str(typeVesionIp.get_ip(common_network))

    # Находим подсеть общей сети
    prefix_length = find_minimum_prefix(ip_addresses, typeVesionIp.get_max_bit_depth())
    subnet = typeVesionIp.get_fun_network()((common_network, prefix_length), strict=False)


    return common_network_str, subnet