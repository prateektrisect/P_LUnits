# Given function
def countLowerCase(m):
  count = 0
  for i in range(0, len(m)):
    if(m[i]>='a' and m[i]<='z'):
      count = count + 1
  return ("LowerCase=" + str(count))
  

# Test code
# Don't change anything in this block
if __name__ == "__main__":
  # For list of integers
  lst1 = []  
  n = int(input())
  lst1 = [int(item) for item in input().split()]
  
  
  
# Write code here 
# and call your function 
