print("welcome to IPcalc")
print("Please enter IP")
A = input()
print ("Please enter the /")
B = int(input())
FIP =("IP                  =" + A +"/" + str(B))

#SUBNET sys

if B==0:
    SUB =("0.0.0.0")
elif B==1:
    SUB =("128.0.0.0")
elif B==2:
    SUB =("192.0.0.0")
elif B==3:
    SUB =("224.0.0.0")
elif B==4:
    SUB =("240.0.0.0")
elif B==5:
    SUB =("248.0.0.0")
elif B==6:
    SUB =("252.0.0.0")
elif B==7:
    SUB =("254.0.0.0")
elif B==8:
    SUB =("255.0.0.0")
elif B==9:
    SUB =("255.128.0.0")
elif B==10:
    SUB =("255.192.0.0")
elif B==11:
    SUB =("255.224.0.0")
elif B==12:
    SUB =("255.240.0.0")
elif B==13:
    SUB =("255.248.0.0")
elif B==14:
    SUB =("255.252.0.0")
elif B==15:
    SUB =("255.254.0.0")
elif B==16:
    SUB =("255.255.0.0")
elif B==17:
    SUB =("255.255.128.0")
elif B==18:
    SUB =("255.255.192.0")
elif B==19:
    SUB =("255.255.224.0")
elif B==20:
    SUB =("255.255.240.0")
elif B==21:
    SUB =("255.255.248.0")
elif B==22:
    SUB =("255.255.252.0")
elif B==23:
    SUB =("255.255.254.0")
elif B==24:
    SUB =("255.255.255.0")
elif B==25:
    SUB =("255.255.255.128")
elif B==26:
    SUB =("255.255.255.192")
elif B==27:
    SUB =("255.255.255.224")
elif B==28:
    SUB =("255.255.255.240")
elif B==29:
    SUB =("255.255.255.248")
elif B==30:
    SUB =("255.255.255.252")
elif B==31:
    SUB =("255.255.255.254")
elif B==32:
    SUB =("255.255.255.255")
else:
    SUB =("SUBNET ERROR")
SNT =("Subnet mask         =" +SUB)	
#   IPCALC 

a = A
Z = a.split(".")
CELLA = (Z[0])
CELLB = (Z[1])
CELLC = (Z[2])
CELLD = (Z[3])

CELLAU = (int(CELLA)) 
CELLBU = (int(CELLB))
CELLCU = (int(CELLC))
CELLDU = (int(CELLD))

CELLAX = (str(bin(CELLAU)))
CA = (CELLAX[2:])

CELLBX = (str(bin(CELLBU)))
CB = (CELLBX[2:])

CELLCX = (str(bin(CELLCU)))
CC = (CELLCX[2:])

CELLDX = (str(bin(CELLDU)))
CD = (CELLDX[2:])


Anum = (len(CA))
Bnum = (len(CB))
Cnum = (len(CC))
Dnum = (len(CD))

if Anum == 1:
    AV = ("0000000" +CA)
elif Anum == 2:
    AV = ("000000" +CA)
elif Anum == 3:
    AV = ("00000" +CA)
elif Anum == 4:
    AV = ("00000" +CA)
elif Anum == 5:
    AV = ("000" +CA)
elif Anum == 6:
    AV = ("00" +CA)
elif Anum == 7:
    AV = ("0" +CA)
elif Anum == 8:
    AV = ("" +CA)
    
if Bnum == 1:
    BV = ("0000000" +CB)
elif Bnum == 2:
    BV = ("000000" +CB)
elif Bnum == 3:
    BV = ("00000" +CB)
elif Bnum == 4:
    BV = ("00000" +CB)
elif Bnum == 5:
    BV = ("000" +CB)
elif Bnum == 6:
    BV = ("00" +CB)
elif Bnum == 7:
    BV = ("0" +CB)
elif Bnum == 8:
    BV = ("" +CB)

if Cnum == 1:
    CV = ("0000000" +CC)
elif Cnum == 2:
    CV = ("000000" +CC)
elif Cnum == 3:
    CV = ("00000" +CC)
elif Cnum == 4:
    CV = ("00000" +CC)
elif Cnum == 5:
    CV = ("000" +CC)
elif Cnum == 6:
    CV = ("00" +CC)
elif Cnum == 7:
    CV = ("0" +CC)
elif Cnum == 8:
    CV = ("" +CC)
    
if Dnum == 1:
    DV = ("0000000" +CD)
elif Dnum == 2:
    DV = ("000000" +CD)
elif Dnum == 3:
    DV = ("00000" +CD)
elif Dnum == 4:
    DV = ("00000" +CD)
elif Dnum == 5:
    DV = ("000" +CD)
elif Dnum == 6:
    DV = ("00" +CD)
elif Dnum == 7:
    DV = ("0" +CD)
elif Dnum == 8:
    DV = ("" +CD)

BIP =("IP in binary =" +AV +"." +BV +"." +CV +"." +DV)
Xnum = (AV +BV +CV +DV)
XX = (len(Xnum[B:]))
HOST = (2**XX-2)
HST = (str(HOST))
UHR =("Useable Hosts       =" +HST)

if B==0:
    BRD = ("11111111"*4)
    NET = ("00000000"*4)
elif B==1:
    BRD = (AV[:1] +"1111111"                        +"11111111"*3)
    NET = (AV[:1] +"0000000"                        +"00000000"*3)
elif B==2:
    BRD = (AV[:2] +"111111"                         +"11111111"*3)
    NET = (AV[:2] +"000000"                         +"00000000"*3)
elif B==3:
    BRD = (AV[:3] +"11111"                          +"11111111"*3)
    NET = (AV[:3] +"00000"                          +"00000000"*3)
elif B==4:
    BRD = (AV[:4] +"1111"                           +"11111111"*3)
    NET = (AV[:4] +"0000"                           +"00000000"*3)
elif B==5:
    BRD = (AV[:5] +"111"                            +"11111111"*3)
    NET = (AV[:5] +"000"                            +"00000000"*3)
elif B==6:
    BRD = (AV[:6] +"11"                             +"11111111"*3)
    NET = (AV[:6] +"00"                             +"00000000"*3)
elif B==7:
    BRD = (AV[:7] +"1"                              +"11111111"*3)
    NET = (AV[:7] +"0"                              +"00000000"*3)
elif B==8:
    BRD = (AV                                       +"11111111"*3)
    NET = (AV                                       +"00000000"*3)
elif B==9:
    BRD = (AV +BV[:1] +"1111111"                    +"11111111"*2)
    NET = (AV +BV[:1] +"0000000"                    +"00000000"*2)
elif B==10:
    BRD = (AV +BV[:2] +"111111"                     +"11111111"*2)
    NET = (AV +BV[:2] +"000000"                     +"11111111"*2)
elif B==11:
    BRD = (AV +BV[:3] +"11111"                      +"11111111"*2)
    NET = (AV +BV[:3] +"00000"                      +"00000000"*2)
elif B==12:
    BRD = (AV +BV[:4] +"1111"                       +"11111111"*2)
    NET = (AV +BV[:4] +"0000"                       +"00000000"*2)
elif B==13:
    BRD = (AV +BV[:5] +"111"                        +"11111111"*2)
    NET = (AV +BV[:5] +"000"                        +"00000000"*2)
elif B==14:
    BRD = (AV +BV[:6] +"11"                         +"11111111"*2)
    NET = (AV +BV[:6] +"00"                         +"00000000"*2)
elif B==15:
    BRD = (AV +BV[:7] +"1"                          +"11111111"*2)
    NET = (AV +BV[:7] +"0"                          +"00000000"*2)
elif B==16:
    BRD = (AV +BV                                   +"11111111"*2)
    NET = (AV +BV                                   +"00000000"*2)
elif B==17:
    BRD = (AV +BV +CV[:1] +"1111111"                +"11111111")
    NET = (AV +BV +CV[:1] +"0000000"                +"00000000")
elif B==18:
    BRD = (AV +BV +CV[:2] +"111111"                 +"11111111")
    NET = (AV +BV +CV[:2] +"000000"                 +"00000000")
elif B==19:
    BRD = (AV +BV +CV[:3] +"11111"                  +"11111111")
    NET = (AV +BV +CV[:3] +"00000"                  +"00000000")
elif B==20:
    BRD = (AV +BV +CV[:4] +"1111"                   +"11111111")
    NET = (AV +BV +CV[:4] +"0000"                   +"00000000")
elif B==21:
    BRD = (AV +BV +CV[:5] +"111"                    +"11111111")
    NET = (AV +BV +CV[:5] +"000"                    +"00000000")
elif B==22:
    BRD = (AV +BV +CV[:6] +"11"                     +"11111111")
    NET = (AV +BV +CV[:6] +"00"                     +"00000000")
elif B==23:
    BRD = (AV +BV +CV[:7] +"1"                      +"11111111")
    NET = (AV +BV +CV[:7] +"0"                      +"00000000")
elif B==24:
    BRD = (AV +BV +CV                               +"11111111")
    NET = (AV +BV +CV                               +"00000000")
elif B==25:
    BRD = (AV +BV +CV +DV[:1] +"1111111") 
    NET = (AV +BV +CV +DV[:1] +"0000000")
elif B==26:
    BRD = (AV +BV +CV +DV[:2] +"111111")
    NET = (AV +BV +CV +DV[:2] +"000000")
elif B==27:
    BRD = (AV +BV +CV +DV[:3] +"11111") 
    NET = (AV +BV +CV +DV[:3] +"00000")
elif B==28:
    BRD = (AV +BV +CV +DV[:4] +"1111")
    NET = (AV +BV +CV +DV[:4] +"0000")
elif B==29:
    BRD = (AV +BV +CV +DV[:5] +"111") 
    NET = (AV +BV +CV +DV[:5] +"000")
elif B==30:
    BRD = (AV +BV +CV +DV[:6] +"11")
    NET = (AV +BV +CV +DV[:6] +"00")
elif B==31:
    BRD = (AV +BV +CV +DV[:7] +"1") 
    NET = (AV +BV +CV +DV[:7] +"0")
elif B==32:
    BRD = (AV +BV +CV +DV)
    NET = (AV +BV +CV +DV)


QA =(BRD[:8])
QB =(BRD[8:16])
QC =(BRD[16:24])
QD =(BRD[24:32])

WA =(NET[:8])
WB =(NET[8:16])
WC =(NET[16:24])
WD =(NET[24:32])

AI = (int(QA, 2))
SA = (str(AI))

BI = (int(QB, 2))
SB = (str(BI))

CI = (int(QC, 2))
SC = (str(CI))

DI = (int(QD, 2))
SD = (str(DI))



AY = (int(WA, 2))
YA = (str(AY))

BY = (int(WB, 2))
YB = (str(BY))

CY = (int(WC, 2))
YC = (str(CY))

DY = (int(WD, 2))
YD = (str(DY))

BROAD = (SA +"." +SB +"." +SC +"." +SD)
NETWRK =(YA +"." +YB +"." +YC +"." +YD)


print()
print()
print (FIP) #FULL IP 
print (SNT) #SUBNET MASK
print (UHR) #USEABLE HOST RANGE 
print ("Broadcast           =" +BROAD)
print ("Network             =" +NETWRK)
print()
print()


