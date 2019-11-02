import ipaddress
import datetime
import sys
import re

print ("ENTER IP/CIDR")
XYZ = input() 
net = ipaddress.ip_network(XYZ, strict=False)

A  = XYZ                      #IP address
B  = net.netmask              #Subnet
C  = net.network_address      #Network ID
D  = net.broadcast_address    #Broadcast
E  = net.num_addresses -2     #Total number of addresses -2 for hosts

sA = str(A)
sB = str(B)
sC = str(C)
sD = str(D)
sE = str(E)

sep = '/'
rest = sA.split(sep, 1)[0]
dash = '-' * 40

tA = ("IP Address" )  
tB = ("Subnet"     )  
tC = ("Network"    )  
tD = ("Broadcast"  )  
tE = ("Hosts"      )

bA = '.'.join([bin(int(x)+256)[3:] for x in rest.split('.')]) 
bB = '.'.join([bin(int(x)+256)[3:] for x in sB.split('.')])
bC = '.'.join([bin(int(x)+256)[3:] for x in sC.split('.')])
bD = '.'.join([bin(int(x)+256)[3:] for x in sD.split('.')])

print()
print()
print('{:18s} {:20s} {}'.format(tA, sA, bA)) 
print('{:18s} {:20s} {}'.format(tB, sB, bB)) 
print('{:18s} {:20s} {}'.format(tC, sC, bC)) 
print('{:18s} {:20s} {}'.format(tD, sD, bD)) 
print('{:18s} {:20s} {}'.format(tE, sE, "")) 
print()
print()

print ("Would you like to save it to a text file ?")
ans = input('(Y/N) << ').lower()

if ans in ['yes', 'y']:
    print ("What would you like to name the text file ?")
    DOC = input()
    sys.stdout = open((DOC) +'.txt','wt')
    print()
    print()
    print('{:18s} {:20s} {}'.format(tA, sA, bA)) 
    print('{:18s} {:20s} {}'.format(tB, sB, bB)) 
    print('{:18s} {:20s} {}'.format(tC, sC, bC)) 
    print('{:18s} {:20s} {}'.format(tD, sD, bD)) 
    print('{:18s} {:20s} {}'.format(tE, sE, "")) 
    print()
    print()

if ans in ['no', 'n']:
    print()

else:
    print()



