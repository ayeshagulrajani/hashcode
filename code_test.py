## Opening the file using open() function
import sys

sys.setrecursionlimit(10**8)
file_name = ""
while 1 :
    try :
        file_name = int(input("Menu \n1.a_example.in\n2.b_small.in \n3.c_medium.in\n4.d_quite_big.in\n5.e_also_big.in\n Choose :"))
        if file_name == 1 :
            file_name = "a_example.in"
            break
        elif file_name == 2:
            file_name = "b_small.in"
            break
        elif file_name == 3:
            file_name = "c_medium.in"
            break 
        elif file_name == 4:
            file_name = "d_quite_big.in"
            break
        elif file_name == 5:
            file_name = "e_also_big.in"
            break
        else:
            print("Re Enter your choice\n\n")
    except Exception as e :
        print("Renter numeric data\n\n")
        
def isSubsetSum(array,n,total,minimum,subset):
    if total< minimum or n == 0:
        return (subset,total)
    
    if array[n-1] > total:
        return isSubsetSum(array,n-1,total,minimum,subset)
    
    subset.append(array[n-1])
    return isSubsetSum(array,n-1,total-array[n-1],minimum,subset)
        
with open("dataset/{}".format(file_name),"r") as f:
    file_data = f.readlines()
    max_slices,types = [int(x) for x in file_data[0].split(" ")]
    type_data = [ int(x) for x in file_data[1].split(" ") ]
    # print(type_data)
    
    subset , total = isSubsetSum(type_data,types,max_slices,type_data[0],[])
    total = max_slices-total
    subset = sorted(subset)
    index = []
    for s in subset :
        index.append(type_data.index(s))
    print(total)
    print(len(index))
    print(index)