altitude=int(input())
if(altitude<=1000):
    print('Safe to land')
elif(altitude>1000 and altitude<5000):
    print('Bring down to 1000')
else:
    print('Turn Around')
