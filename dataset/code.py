# f = 'e_also_big.in'

# with open(f,"r") as f:
#     data = f.readlines()
#     ini_data = [int(x) for x in data[0].split(" ")]
#     pizza_data = list()
#     for line in range(1,len(data)):
#         pizza_data.append(data[line])
#     pizza_data = [int(x) for x in pizza_data[0].split(" ")]
#     # print(ini_data)

#     required = []
    
#     # for i in range(len(pizza_data)):
#     #     for x in range(i) :
#     #         required.append(pizza_data[x])
#     #     req

#     #f print(required)
#     print(sum(required), ini_data[0])
# A recursive solution for subset sum 
# problem 

# Python program to print all subsets with given sum 
  
# The vector v stores current subset. 
# def printAllSubsetsRec(arr, n, v, sum) : 
  
#     # If remaining sum is 0, then print all 
#     # elements of current subset. 
#     if (sum == 0) : 
#         for value in v : 
#             print(value, end=" ") 
#         print() 
#         return
      
  
#     # If no remaining elements, 
#     if (n == 0): 
#         return
  
#     # We consider two cases for every element. 
#     # a) We do not include last element. 
#     # b) We include last element in current subset. 
#     printAllSubsetsRec(arr, n - 1, v, sum) 
#     v1 = [] + v 
#     v1.append(arr[n - 1]) 
#     printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1]) 
  
  
# # Wrapper over printAllSubsetsRec() 
# def printAllSubsets(arr, n, sum): 
  
#     v = [] 
#     printAllSubsetsRec(arr, n, v, sum) 
  
  
# # Driver code 
  
# arr = [ 4 ,14 ,15 ,18 ,29 ,32 ,36 ,82 ,95 ,95] 
# sum = 100
# n = len(arr) 
# printAllSubsets(arr, n, sum) 
  
# # This code is contributed by ihritik 

# import itertools

# def find_subsets(s,n):
#     return list(itertools.combinations(s,n))

def subsetSums(array , l,r,sum = 0):
    if l>r :
        print(sum)
        return
    
    subsetSums(array,l+1,r,sum+array[l])
    subsetSums(array,l+1,r,sum)
    

with open("c_medium.in") as f:
    lines = f.readlines()
    max_size = int(lines[0].split(" ")[0])
    types = int(lines[0].split(" ")[1])
    
    sum_of_subsets = []
    subsets = []
    data = []
    
    for i in range(1,len(lines)):
        for x in lines[i].split(" "):
            if int(x) > max_size:
                continue
            data.append(int(x))  
    
    subsetSums(data,0,len(data)-1) 
            