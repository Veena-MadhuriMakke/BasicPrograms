# check if the frist and last element int the list is same or not 
list = input("Enter the elements in the list: ").split()
def First_Last(list):
    first = list[0]
    last = list[-1]
    if len(list)>0:
        if first == last:
            return True
        else :
            return False
    else :
        print("List is Empty")
print(First_Last(list))