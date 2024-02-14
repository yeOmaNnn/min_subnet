import ipaddress
import click
import os
from typeVersion import TypeVersion
from utilits.find_common_network import find_common_network


typeVersionIp = {
    "4": TypeVersion(32, ipaddress.IPv4Address, ipaddress.IPv4Network),
    "6": TypeVersion(128, ipaddress.IPv6Address, ipaddress.IPv6Network),
}


@click.command()
@click.argument("path")
@click.argument("ver_ip")
def get_net(path: str, ver_ip: str):
    # if not os.path.exists(path):
    #     click.echo("File not exists")
    #     return
    ver_ip = ver_ip.lower()
    if ver_ip != "6" and ver_ip != "4":
        click.echo("Unknown version")
        return
    valid_ip = []
    select_type_version: TypeVersion = typeVersionIp[ver_ip]
    with open(path, 'r') as file_ip:
        for line in file_ip.readlines():

            line = line.replace("\n", "")
            check_ip = select_type_version.get_ip(line)
            valid_ip.append(line)

    if len(valid_ip) == 0:
        click.echo("No valid ip address")
        return
    common_network, subnet = find_common_network(valid_ip, select_type_version)
    if common_network == "0":
        click.echo("This set does not have a common subnet")
    else:
        click.echo(f"Result net: {subnet}")
    return


if __name__ == "__main__":
    get_net()
