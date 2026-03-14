'''
      *
    * *
  * * *
* * * *
'''

if __name__ == "__main__":
    n = int(input("Enter no. of rows: "))
    
    for i in range(0, n):
        for j in range(0, n-i):
            print(" ", end=" ")
            
        for k in range(j, n):
            print("*", end=" ")
        print("\n")