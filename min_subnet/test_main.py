from click.testing import CliRunner
from main import get_net

class TestIPFound(CliRunner):

    def test_from_doc(self):
        result = self.invoke(get_net,["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv4.txt", "4"])
        assert result.exit_code == 0
        assert result.output.find("192.168.1.0/29") != -1

        result = self.invoke(get_net,["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv6.txt", "6"])
        assert result.exit_code == 0
        assert result.output.find("ffe0::/72") != -1

    def test_new_data(self):
        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv4.1.txt", "4"])
        assert result.exit_code == 0
        assert result.output.find("192.168.0.0/25") != -1
        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv4.2.txt", "4"])
        assert result.exit_code == 0
        assert result.output.find("192.168.0.0/23") != -1
        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv6.1.txt", "6"])
        assert result.exit_code == 0
        assert result.output.find("8000::/1") != -1
        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv6.2.txt", "6"])
        assert result.exit_code == 0
        assert result.output.find("0:20:2201:1004:2000:8000:42:4/128") != -1


    def test_error(self):
        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv4.5.txt", "4"])
        assert result.exit_code > 0

        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv4.6.txt", "4"])
        assert result.exit_code > 0

        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv6.3.txt", "6"])
        assert result.exit_code > 0

        result = self.invoke(get_net, ["C:/Users/Yeoman/PycharmProjects/min_subnet/IPv6.4.txt", "6"])
        assert result.exit_code > 0



if __name__ == "__main__":
    test1 = TestIPFound()
    test1.test_from_doc()
    test1.test_new_data()
    test1.test_error()