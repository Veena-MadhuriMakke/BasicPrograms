#check wheather the given key is in the dictionary 
my_dict = {}
n = int(input("Enter how many number of keys you want to insert :"))
for i in range (n):
    key = input(f"Enter key #{i+1} : ") #taking a ky as input
    value = input(f"Enter a value for {key} : ") #taking a value fro the key
    my_dict[key]=value #assigning the value to the key
print("your dictionary is :", my_dict)
k = input("Enter the key you wants to check: ")
if k in my_dict:
    print("Present")
else:
    print("Not Present")
v = input("Enter the value you wants to check: ")
if v in my_dict.values():
    print("Present")
else:
    print("Not Present")
