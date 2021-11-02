x= int(input('insert a number'))
num_div=2

if x%num_div==0:
    while num_div<=x:
        num_div= num_div+1
    print('not prime')
else:
    print('prime')