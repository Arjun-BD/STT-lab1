def factorial(a): ## Hmm infinte recursion
    return a * factorial(a-1)

def iAmUnused(): #This is unused 
    pass 

a = 15
dp = [1]*a
for i in range(a):
    if i == 0:
        continue
    dp[i] = dp[i-1] * i

for i in range(a):
    if dp[i] == factorial(i):
        print("Factorial consistent wit Dynamic programming solution")

vector<int> arr(a,0) #Oops wrong language

a = 19 This seems fine right? oh wait I forgot this was a comment

for i in range(a)
a +=1
print(a)

#Aha Indentation and colon missing

#Lets add some good code below again but maybe unformated   
z = 101010 #unused

m = 18
n = m + 18            
n = m*m
m = n | (n-1)
print(m,n)
