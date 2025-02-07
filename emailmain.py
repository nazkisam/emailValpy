email = input('enter your email')
k=0
if len(email) >= 6:
  if email[0].isalpha():
     if ('@' in email) and (email.count('@')==1):
       if (email[-4] =='.') ^ (email[-3]=='.'): #xzor operator ff=f,tf=t
        for i in email:
          if i==i.isspace():
              k=1
        if k==1:
            print('wrong email space')   
       else:
         print('wrong .pos')     
     else:
       print('wrong @') 
  else:
    print('not valid')
else:
  print('wrong email 1')