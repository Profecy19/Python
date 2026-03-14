'''
    *
  * * *
* * * * *
'''

if __name__ == "__main__":
    n = int(input("Enter no. of rows: "))
    
    for i in range(0, n):
        for k in range(0,n-i):
            print(" ",end=" ")
        
        for j in range(k, n):
            print("*", end=" ")
        
        for l in range(0,i):
            print("*", end=" ")
        print("\n")