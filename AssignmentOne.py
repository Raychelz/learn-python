##Assignment one
##Sample
##Enter number x: 2
##Enter number y: 3
##X**y = 8
##log(x) = 1

import math
x = int(input("Enter number x: " ))
y =int(input("Enter number y:  "))

num = x**y
print(x,"Raised to the power of",y,"is", num)

numlog = math.log(x,2)

print("Log of",x,"is", numlog)
