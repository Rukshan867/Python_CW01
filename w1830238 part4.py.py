# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion

# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830238

# Date: 30.04.2021


#Histogram outcomes in total
def total(a,b,c,d):
   total = a + b + c + d
   print(total, "outcomes in total.")
    
       
          
#Counting the number of each outcomes 
pr    = 0
tr    = 0
re    = 0
ex    = 0
count = 0

#Main code

while True:       
 try :
    
  #Asking from user to enter student credit at pass,defer and fail   
  passc = int(input("Enter your total PASS credits: "))
  if not passc in range(0,125,20):                     #Checking the range 
     print("Out of range")
     print()
     continue                                          #If it's out of range loop will start over.

  defer = int(input("Enter your total DEFER credits: ")) 
  if not defer in range(0,125,20):
     print("Out of range")
     print()
     continue
        
  fail = int(input("Enter your total FAIL credits: "))
  if not fail in range(0,125,20):
     print("Out of range")
     print()
     continue 
  

  #Checking the total(120)
  if passc + defer + fail == 120 :
      #Progression outcomes
      if passc == 120 :
          pr += 1
          print("Progress")

      elif passc == 100 :      
          tr += 1 
          print("Progress (module trailer)")                    

      elif passc == 80 or passc == 60 or passc == 40 or passc == 20 or passc == 0 :
          if fail == 120 or fail == 100 or fail == 80 :
              ex += 1
              print("Exclude")
          else :
              re += 1            
              print ("Do not Progress – module retriever")
  else :
       print("Total incorrect")
       print()
       continue                      #If the total is incorrect the Loop will start over.

  #Exit the loop option
  print()  
  out = str(input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: "))
  if out == 'q' or out == 'Q':
      break
  

  
 except ValueError:
     print("Integer required")
 print()
     

print()
print('-' * 60)
print("Vertical Histogram")
print()
#Histogram Display
print (f'Progress {pr}  |  Trailer {tr}  |  Retriever {re}  |  Exclude {ex}  ')
maxi = max(pr,tr,re,ex)
while count < maxi:
    
    if pr - count > 0 :
        print("   *         ",end="")
    else:
        print("             ",end="")

    if tr - count > 0 :
        print("    *        ",end="")
    else:
        print("             ",end="")
        
    if re - count > 0 :
        print("       *     ",end="")
    else:
        print("             ",end="")
        
    if ex- count > 0 :
        print("        *      ")
    else:
        print("               ") 

    count+= 1
print()
total(pr,tr,re,ex)
