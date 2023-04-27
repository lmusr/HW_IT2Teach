def task_integer1():
 """A two-digit integer is given.
 Find the sum and the product of its digits."""
 try: # check for errors
     n = int(input( "N = "))
 except: # if some error
     print( "L must be an INTEGER !!!")
     input( "Press enter for exit ...")
 else: # if no errors
     n1 = n%10
     n2 = n//10
     sum1 = n1+n2
     prod = n1*n2
     print( "Sum = ", sum1)
     print( "Product = ", prod)
