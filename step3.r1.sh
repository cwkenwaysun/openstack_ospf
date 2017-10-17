sudo apt-get update
sudo apt-get install -y quagga
sudo apt-get install -y telnet
sudo sed -i s'/zebra=no/zebra=yes/' /etc/quagga/daemons
sudo sed -i s'/ospfd=no/ospfd=yes/' /etc/quagga/daemons
sudo cp /usr/share/doc/quagga/examples/zebra.conf.sample /etc/quagga/zebra.conf
sudo cp r1.conf /etc/quagga/ospfd.conf
sudo /etc/init.d/quagga start
sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
