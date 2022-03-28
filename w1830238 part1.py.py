# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  

# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830238        
  
# Date:  30.04.2021




while True :
 try:    
 #Asking from user to enter student credit at pass,defer and fail   
  passc = int(input("Please enter your credits at pass: "))
  defer = int(input("Please enter your credit at defer: ")) 
  fail = int(input("Please enter your credit at fail: "))



 
  if passc + defer + fail == 120 :

    #Progression outcomes        
     if passc == 120 :
         print("Progress")

     elif passc == 100 :
            print("Progress (module trailer)")             
     elif passc == 80 or passc == 60 :
            print ("Do not Progress – module retriever")

     elif passc == 40 :
         if defer == 0 :
            print("Exclude")
            
         else :
            print("Do not Progress – module retriever")
            
     elif passc == 20 :
        if defer == 20 or defer == 0 :
            print("Exclude")

        else :
            print("Do not Progress – module retriever")

     elif passc == 0 :
        if defer == 40 or defer == 20 or defer == 0 :
            print("Exclude")

        else :
            print("Do not Progress – module retriever")
  print()
 except ValueError:
     print("Requires a valid integer !")
     print()
