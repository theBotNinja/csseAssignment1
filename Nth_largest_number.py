length = int(input("Enter the length of your list : "))

lis = [int(input(f"Enter {i}th element : ")) for i in range(0,length)]

lis.sort()

N = int(input("Enter the N : "))
try:
    if N == 0 : raise Exception("start from 1 and between list length") 
    print("The Nth largest number is : ",lis[-N])
except :
    print("start from 1 and between list length")
