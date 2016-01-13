#!/usr/bin/python
import math

#print "This program finds the two perfect squares that add up to your prime number that is of the form 4n+1."
#print "Please enter your prime number"
#x = input("Enter the prime: ")
#if x < 2:
#  print "The number must be positive"
#else:
print "Prime Number, First Square Root, Second Square Root,"
for x in xrange(3, int(math.pow(2, 31)), 2):
  if x%2==0:
    pass
#    print "The number is even, not prime."
  else:
    prime_flag = True
    for i in xrange(3, ((x/2)+1), 2):
      if x%i==0:
        prime_flag = False
    if prime_flag==False:
      pass
#      print "This number is not prime."
    else:
#      print "The prime is " + str(x)
      if x%4!=1:
        pass
#        print "The prime is " + str(x) + " but is not in the form 4n+1."
      else:
#        print "This prime is in the form 4n+1."
        j = int(math.floor(math.sqrt(x)))
        while j > 1:
          if math.sqrt(x-(j*j)) == int(math.sqrt(x-(j*j))):
            print str(x) + "," + str(j) + "," + str(int(math.sqrt(x-(j*j)))) + ","
          j=j-1

