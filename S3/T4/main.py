# Given function
def drinks(ele):
  if((ele%2==0) and (ele%3!=0)):
    print("Pepsi")
  elif((ele%2!=0) and (ele%3==0)):
    print("Coke")
  elif((ele%2==0) and (ele%3==0)):
    print("PepsiCoke")
  else:
    print("Pepsi")
  

# Test code
# Don't change anything in this block
if __name__ == "__main__":
  # For list of integers
  lst1 = []  
  n = int(input())
  lst1 = [int(item) for item in input().split()]
  
  
  
# Write code here 
# and call your function 
