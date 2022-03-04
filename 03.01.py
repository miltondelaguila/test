Hours = input ("How many hours? ")
Rate = input ("Add the rate: ")
try :
    hs = float(Hours)
    rt = float(Rate)
except :
    print ("Use numeric values")
    quit()

if hs < 40 :
    print(hs)
    print(rt)
    print(hs*rt)
else :
    print(hs)
    print(rt)
    print ((40*rt)+((hs-40)*(rt*1.5)))
