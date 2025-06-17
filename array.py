#Array implementation 
arr = []   # empty array created

# initalize values

arr = [10,15,20,25]

# array traversing

for i in arr:
    print(i)
#Array insertion 
arr.append(30)      #insert at end
arr.insert(0,5)     # insert 5 at index 0
print(arr)

#Array Deletion
arr.remove(20) #By value
arr.pop(2)      # By index
print(arr)