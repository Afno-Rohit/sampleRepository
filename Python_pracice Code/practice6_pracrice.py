# a=int(input("Enter the number 1:"))
# b=int(input("Enter the number 2:"))
# c=int(input("Enter the number 3:"))
# d=int(input("Enter the number 4:"))
# if(a>b and a>c and a>d):
#     print("a is greatest number :")
# elif(b>a and b>c and b>d):
#     print("b is greatest number :")
# elif(c>a and c>b and c>d):
#     print("c is greatest number :")
# else:
#     print("d is greatest number:")

# marks1=int(input("Enter the marks of English :"))
# marks2=int(input("Enter the marks of science:"))
# marks3=int(input("Enter the marks of math:"))
# Total_percentage= (100*(marks1+marks2+marks3)/300)
# if(Total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("Stuent is passed :")
# else:
#     print("student is failed! try next year :")

# p1="Make a lot of money"
# p2="buy now" 
# p3="subscribe this"
# p4="click this"
# message=input("Enter your comment :")
# if((p1 in message) or(p2 in message) or(p3 in message) or(p4 in message)):
#     print("This comment is spam:")
# else:
#     print("This comment is not spam :")

# username=input("Enter your name :")
# if((len(username)<10)):
#     print("your username contains less than 10 characters ")
# else:
#     print("All is well:")

# l=["Rohit","aman","Grapes"]
# name=input("Enter your name :")
# if(name in l):
#     print("A valid name is present :")
# else:
#     print("A valid name is not present:")    

marks=int(input("Enter your marks :"))
if(marks<=100 and marks>=90):
    grade ="Ex"
elif(marks<=90 and marks>=80):
    grade="A"
elif(marks<=80 and marks>=70):
    grade="B"
elif(marks<=60 and marks>=50):
    grade="D"
elif(marks<50 and marks>=0):
    grade="f"
print(grade)