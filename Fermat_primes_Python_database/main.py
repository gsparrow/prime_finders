# vim: nu
# vim: foldmethod=marker

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import math

con = None #{{{
# }}}
  

for x in xrange(3, int(math.pow(2, 31)), 2):                                          #find all primes less than 2^31
  if x%2==0:                                                                          #if the number is even, which it should not be
    pass                                                                              #ignore it
#    print "The number is even, not prime."
  else:
    prime_flag = True
    for i in xrange(3, ((x/2)+1), 2):                                                 #start checkibg for primality, only need to go up to half
      if x%i==0:                                                                      #the numbers size
        prime_flag = False
        i=x
    if prime_flag==False:
      pass
#      print "This number is not prime."
    else:
#      print "The prime is " + str(x)
      if x%4!=1:                                                                      #check if it is a special prime of the form 4n+1
        try:
          con = lite.connect('Prime_database.db')
          cur = con.cursor()
          my_string="INSERT INTO primes(prime, \"4n+1\") VALUES(" +str(x) +",0)"      #0 for false
          cur.execute(my_string);
          con.commit()
        except lite.Error, e:
          print "Error %s:" % e.args[0]
          sys.exit(1)
        finally:
          if con:
            con.close()
      else:
        try:
          con = lite.connect('Prime_database.db')
          cur = con.cursor()
          my_string="INSERT INTO primes(prime, \"4n+1\") VALUES(" +str(x) +",1)"      #1 for true
          cur.execute(my_string);
          con.commit()
        except lite.Error, e:
          print "Error %s:" % e.args[0]
          sys.exit(1)
        finally:
          if con:
            con.close()
