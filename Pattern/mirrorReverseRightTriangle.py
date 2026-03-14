'''
* * * *
  * * *
    * *
      *
'''

if __name__ == "__main__":
    n = int(input("Enter no. of rows: "))
    
    for i in range(0, n):
        for k in range(0,i+1):
            print(" ",end=" ")
        for j in range(i, n):
            print("*", end=" ")
        print("\n")