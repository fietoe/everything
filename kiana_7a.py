x = [1,2]
print (x)

print (x[0])

x[0] = 33
print (x)

my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)
    
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)    

my_list.append("Ladle")
print (my_list)

my_list = [] # Empty list
for i in range(5):
    user_input = input( "Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)
    
    # Create an array with 100 zeros.
my_list = [0] * 100    

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
 
# Initial sum should be zero
list_total = 0
 
# Loop through array, copying each item in the array into
# the variable named item.
for item in my_list:
    # Add each item
    list_total += item
 
# Print the result