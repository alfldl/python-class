
#    0123456789
s = "Hello world!"
print ('-------s1-----------')
print (s[0])
print (s[1])
print (s[-1])   # 맨 뒤
print (s[-2])   # 맨 뒤에서 2번째

#     01234 56789
s2 = "Hello world!"
print ('-------s2-----------')
print (s2[1:3])
print (s2[0:5])

s3 = 'Hello'
print ('-------s3-----------')
print (s3[1:])
print (s3[:3])
print (s3[:])

s4 = 'abcd'
print ('-------s4-----------')
print (s4[::2])
print (s4[::-1])