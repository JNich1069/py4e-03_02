scr = input ('Enter Score: ')
try:
    fs = float (scr)
except:
       print ('Error')
       quit ()
if fs > 1.0 :
    print ('Error, Out of Range')
elif fs >= 0.9 :
    print ('A')
elif fs >= 0.8 :
    print ('B')
elif fs >= 0.7 :
    print ('C')
elif fs >= 0.6 :
    print ('D')
elif fs <= 0.6 :
    print ('F')
