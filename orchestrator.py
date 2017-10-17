import os
import os.path
import subprocess
import re
from subprocess import Popen, PIPE

fip = {
    "host-a": "",
    "host-b": "",
    "r1": "",
    "r2": "",
    "r3": "",
    "r4": ""
}
user = os.environ["USER"]
print("Hello,", user, ":")
    
if os.path.isfile("id_rsa.pub"):
    file = open("id_rsa.pub", 'r')
    text = file.readlines()[0]
    email = text[text.rindex(" ")+1:len(text)-1].replace('.', 'X').replace('@', 'X')
    print("Your key is", email)
    
    print("Please remember to copy your keypair in the .ssh directory then run those steps!")
else:
    print("Please also copy your keypair in the la1 directory, and name it 'id_rsa.pub'.")


def shell_source(script):
    '''Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it.'''
    file = open(script, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        os.environ[ lines[i][lines[i].index(" ")+1:lines[i].index("=")] ] = lines[i][lines[i].index("=")+1:lines[i].index("\n")]
        print("set " + lines[i][lines[i].index(" ")+1:lines[i].index("=")] + " = " + os.environ[ lines[i][lines[i].index(" ")+1:lines[i].index("=")] ])

# start setting ospf
print("If this is the first time, please type 'setup'.\nInput 'quit' to quit.\n")
phase = input("Which step? ")
while True:
    if phase == "help":
        print("print help")
    elif phase == "setup":
        # setup key
        subprocess.call(['sudo', 'cp', '/root/setup/admin-openrc.sh', 'admin-openrc.sh'])
        #subprocess.call(['sudo', 'sh', 'admin-openrc.sh'])
        shell_source('admin-openrc.sh')
    elif phase == "step1":
        subprocess.run(['sh', 'step1.sh'])
    elif phase == "step2":
        subprocess.run(['sh', 'step2.sh', user + '-' + email])
        result = subprocess.run(['neutron floatingip-list -c floating_ip_address'], shell=True, stdout=subprocess.PIPE)
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(result))
        #print(fip)
        '''
        fip["host-a"] = ip[0]
        fip["host-b"] = ip[1]
        fip["r1"] = ip[2]
        fip["r2"] = ip[3]
        fip["r3"] = ip[4]
        fip["r4"] = ip[5]
        print(fip)
        for i in fip:
            subprocess.run(['openstack', 'ip', 'floating', 'add', fip[i], i])'''
        print("step2 done!")

    elif phase == "step3":
        #r1
        subprocess.run(['scp', 'r1.conf', 'ubuntu@' + fip["r1"] + ":~"])
        subprocess.run(['scp', 'step3.r1.sh', 'ubuntu@' + fip["r1"] + ":~"])
        subprocess.run(['ssh', 'ubuntu@' + fip["r1"], "bash < step3.r1.sh"])
        print("r1 set")
        #r2
        subprocess.run(['scp', 'r2.conf', 'ubuntu@' + fip["r2"] + ":~"])
        subprocess.run(['scp', 'step3.r2.sh', 'ubuntu@' + fip["r2"] + ":~"])
        subprocess.run(['ssh', 'ubuntu@' + fip["r2"], "bash < step3.r2.sh"])
        print("r2 set")
        #r3
        subprocess.run(['scp', 'r3.conf', 'ubuntu@' + fip["r3"] + ":~"])
        subprocess.run(['scp', 'step3.r3.sh', 'ubuntu@' + fip["r3"] + ":~"]) 
        subprocess.run(['ssh', 'ubuntu@' + fip["r3"], "bash < step3.r3.sh"])
        print("r3 set")
        print("step3 done!")

    elif phase == "step4":
        #host-a
        subprocess.run(['scp', 'step4.a.sh', 'ubuntu@' + fip["host-a"] + ":~"])
        subprocess.run(['ssh', 'ubuntu@' + fip["host-a"], "bash < step4.a.sh"])

        #host-b
        subprocess.run(['scp', 'step4.b.sh', 'ubuntu@' + fip["host-b"] + ":~"])
        subprocess.run(['ssh', 'ubuntu@' + fip["host-b"], "bash < step4.b.sh"])

        print("step4 done!")


    elif phase == "step5":
        subprocess.run(['sh', 'step5.sh', user + '-' + email])
    elif phase == "step6":
        #r4
        subprocess.run(['scp', 'r4.conf', 'ubuntu@' + fip["r4"] + ":~"])
        subprocess.run(['scp', 'step3.r4.sh', 'ubuntu@' + fip["r4"] + ":~"]) 
        subprocess.run(['ssh', 'ubuntu@' + fip["r4"], "bash < step3.r4.sh"])
        print("r4 set")
        print("step6 done!")

    elif phase == "step7":
        subprocess.run(['sh', 'step7.sh'])
    elif phase == "quit":
        print("The 'orchestrator.py' is quit.")
        quit()
    elif phase == "r":
        result = subprocess.run(['neutron floatingip-list -c floating_ip_address'], shell=True, stdout=subprocess.PIPE)
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', str(result))
        fip["host-a"] = ip[0]
        fip["host-b"] = ip[1]
        fip["r1"] = ip[2]
        fip["r2"] = ip[3]
        fip["r3"] = ip[4]
        fip["r4"] = ip[5]
        print(fip)
        for i in fip:
            subprocess.run(['openstack', 'ip', 'floating', 'add', fip[i], i])
    elif phase == "q":
        pass

    phase = input("Which step? ")

