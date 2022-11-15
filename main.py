def fibonaci(n):
    if n<=1:
        return n
    else:
        return(fibonaci(n-1) + fibonaci(n-2))
n=int(input("enter number"))        
for i in range(n):
    print(fibonaci(i))
    
    
    
# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(fibonacci(i))
