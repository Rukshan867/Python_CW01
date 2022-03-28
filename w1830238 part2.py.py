# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  

# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830238        
  
# Date:  30.04.2021



#Loop condition
done = False

#Loop
while not done: 
 try :
  
  #Asking from user to enter student credit at pass,defer and fail
  passc = int(input("Please enter your credits at pass: "))

  if not passc in range(0,125,20):      #Checking the range
     print("Out of range")
     print()
     continue                           #If it's out of range the loop will start over

  defer = int(input("Please enter your credit at defer: ")) 
  if not defer in range(0,125,20):      #Checking the range
     print("Out of range")
     print()
     continue
        
  fail = int(input("Please enter your credit at fail: "))
  if not fail in range(0,125,20):       #Checking the range
     print("Out of range")
     print()
     continue 

  #Checking the total
  if passc + defer + fail == 120 :    

      #Progression outcomes       
      if passc == 120 :
          print("Progress")
          done = True        #Ending the Loop      

      elif passc == 100 :
           print("Progress (module trailer)")
           done = True       #Ending the Loop  

      elif passc == 80 or passc == 60 or passc or 40 or passc == 20 or passc == 0 :
          if fail == 120 or fail == 100 or fail == 80 :
              print("Exclude")
              done = True     #Ending the Loop  
             
          else :
              print ("Do not Progress – module retriever")
              done = True     #Ending the Loop  
  else :
       print("Total incorrect")
 
 except ValueError:
     print("Integer required")
 print()
