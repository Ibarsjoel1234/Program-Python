nn=input()
var =len(nn)
if var > 1:
   for i in range(2, var):
       if (var % i) == 0:
           print("no")
           break
   else:
       print("yes")

else:
   print("no")
