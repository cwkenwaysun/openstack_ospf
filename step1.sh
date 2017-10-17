#!/bin/bash

neutron router-gateway-clear flat-lan-1-router
neutron router-interface-delete flat-lan-1-router flat-lan-1-subnet
neutron router-delete flat-lan-1-router
neutron subnet-delete flat-lan-1-subnet
neutron net-delete flat-lan-1-net

neutron router-gateway-clear tun0-router
neutron router-interface-delete tun0-router tun0-subnet
neutron router-delete tun0-router
neutron subnet-delete tun0-subnet
neutron net-delete tun0-net

echo "step1 done!";