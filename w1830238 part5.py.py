# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion

# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830238

# Date: 30.04.2021


#Lists(P = Pass,d = Defer, F= Fail)
p = [120,100,100,80,60,40,20,20,20,0]
d = [0,20,0,20,40,40,40,20,0,0]
f = [0,0,20,20,20,40,60,80,100,120]

#Histogram Function
def histogram (x, z =' '):
    s = '*'*x
    print(f'{z:10} {x}: {s}')
#Histogram outcomes in total
def total(a,b,c,d):
   total = a + b + c + d
   print(total, "outcomes in total.")

   
#Counting the number of each outcomes    
progress  = 0
trailing  = 0
retriever = 0
excluded  = 0

#Bringing out the numbers inside of lists
def lists():
  global passc  
  passc = p[count]
  global defer
  defer = d[count]
  global fail
  fail = f[count]

#Progression outcomes
def Progression_outcomes():
    global passc
    global defer
    global fail
    global progress
    global trailing
    global excluded
    global retriever
    if passc == 120 :
         
         progress += 1
         print("Progress")

    elif passc == 100 :
          trailing += 1
          print("Progress (module trailer)")                    

    elif passc == 80 or passc == 60 or passc or 40 or passc == 20 or passc == 0 :
         if fail == 120 or fail == 100 or fail == 80 :

             excluded += 1
             print("Exclude")

         else :

             retriever +=1
             print ("Do not Progress – module retriever")
    



count = 0

#Loop
while count < 10 :
 lists()
 Progression_outcomes()
 count += 1

print()
#Histogram Display
histogram(progress,'Progress')
histogram(trailing,'Trailing')
histogram(retriever,'Retriever')
histogram(excluded,'Excluded')

print()
total(progress,trailing,retriever,excluded)

