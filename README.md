# CloudLab: Cloud Computing and Network Function Virtualization #
Name: Chien-Wei Sun
uid: u1141797

## Getting Started ##
1. Put the tarball in ctl node.
2. Run 'tar -zxvf la1.tar.gz'
3. Run 'cd la1'
4. Replace your key pair in the la1.
5. Run 'cp id_rsa id_rsa.pub ../.ssh/'
6. Run 'sudo cp /root/setup/admin-openrc.sh .'
7. Run 'source admin-openrc.sh'

## Seven-Step OSPF ##
1. Run 'python3 orchestrator.py'
2. Type 'step1', and wait for 10 seconds, then step1 is done.
3. Type 'step2', and wait for 2 minutes, then step2 is done.
4. Press Ctrl+c to leave orchestrator.
5. Type 'neutron floatingip-list -c floating_ip_address', you would get a list of IPs.
6. Type 'openstack ip floating add <one_of_IPs> host-a
7. Type 'ssh ubuntu@<one_of_IPs>', the same IP at 6. Then type 'yes'. Then 'exit'. This 
    step is to make sure nova and neutron is working well.
8. Do the similar 6. 7. step for [host-b, r1, r2, r3]. Each floating IP should be different.
9. If something in 6. 7. 8. went wrong, say, r2 can not connect: Type 'nova delete r2'
    Then look into step2.sh to run same command to reboot one, And still do 6. 7.
    Be careful the key pair value, it should be <user>-<your email with .@ = X>
10. If you do many time and still not work, restart an experiment and do these again.
11. Type 'vim orchestrator.py' Modify the value in 'fip' to those IPs you just set in 6. step.
    You can leave r4 to blank here.
12. Run 'python3 orchestrator.py'
13. Type 'step3', wait for 3 minutes, then step3 is done.
14. Type 'step4', wait for 3 seconds, then step4 is done. You may test Ping now or from any step after.
15. Type 'step5', wait for 3 seconds, then step5 is done. 
16. Type Ctrl+c to leave orchestrator.
17. Do the similar 6. 7. to r4.
18. Type 'vim orchestrator.py' Modify the value in 'fip' to IP for r4.
19. Run 'python3 orchestrator.py'
20. Type 'step6', wait for 1 minute, then step6 is done.
21. Type 'step7', wait for 1 second, then step7 is done.
22. OSPF done.
