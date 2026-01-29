# n=int(input("Enter a number :"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

# l=["Rohit","Soham","Samir","Aman"]
# for name in l:
#         if(name.startswith("S")):
#                    print(f"namaste {name}")
    
# n=int(input("Enter a number :"))
# i=1
# while(i<11):
#     print(f"{n}*{i}={n*i}")
#     i=i+1
     
# n=int(input("Enter a number :"))
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime:")
#         break
# else:
#     print("Number is prime")

# n=int(input("Enter a number :")) 
# i=2
# while(i<n):
#     if(n%i)==0:
#         print("Number is not prime:")
#         break
#     i=i+1
# else:
#     print("Number is prime ")

# n=int(input("Enter a number :"))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum) 
 
# n=int(input("Enter a number :"))
# product=1
# for i in range(1,n+1):
#     product=product*1
    
# print(f"The factorial of {n} is  {product}")
   
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("*"* (2*i-1),end="")
#     print("")

   
# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#     print(" "* (n-1),end="")
#     print("*"* (i ),end="")
#     print("")

# n=int(input("Enter a number :"))
# for i in range(1,n+1):
#      if(i==1 or i==n):
#           print("*"* n,end="")
# else:
#      print("*",end="")
#      print(" "*(n-2),end="")
#      print("*",end="")
# print("")

# n = int(input("Enter a number : "))
# for i in range(1, n+1):
#     if i == 1 or i == n:        # first and last row full *
#         print("*" * n)
#     else:
#         print("*" + " "*(n-2) + "*")  # hollow middle rows


n=int(input("Enter a number :"))
for i in range(1,11):
     print(f"{n}*{11-i}={n*(11-i)}")