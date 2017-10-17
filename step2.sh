neutron net-create w-net
neutron subnet-create --name w-subnet w-net 10.0.10.0/24

neutron net-create x-net
neutron subnet-create --name x-subnet x-net 10.0.11.0/24

neutron net-create y-net
neutron subnet-create --name y-subnet y-net 10.0.12.0/24

neutron net-create z-net
neutron subnet-create --name z-subnet z-net 10.0.13.0/24

neutron router-create remote-access
neutron router-gateway-set remote-access ext-net
neutron router-interface-add remote-access w-subnet
neutron router-interface-add remote-access x-subnet
neutron router-interface-add remote-access y-subnet
neutron router-interface-add remote-access z-subnet

nova boot --image trusty-server --flavor m1.small --nic net-name=w-net --key-name $1 host-a
nova boot --image trusty-server --flavor m1.small --nic net-name=w-net --nic net-name=x-net --key-name $1 r1
nova boot --image trusty-server --flavor m1.small --nic net-name=x-net --nic net-name=y-net --key-name $1 r2
nova boot --image trusty-server --flavor m1.small --nic net-name=y-net --nic net-name=z-net --key-name $1 r3
nova boot --image trusty-server --flavor m1.small --nic net-name=z-net --key-name $1 host-b

#nova boot --image trusty-server --flavor m1.small --nic net-name=y-net --nic net-name=x-net --key-name kenway-kenwayXsunXutahXedu r4

neutron floatingip-create ext-net
neutron floatingip-create ext-net
neutron floatingip-create ext-net
neutron floatingip-create ext-net
neutron floatingip-create ext-net
neutron floatingip-create ext-net
