def Large_nbr (n):
    l = []
    for i in range (n):
        num = int(input(f"Enter number {i+1}: "))
        l.append(num)
    return l
n = int(input("Enter the number of elements : "))
List = Large_nbr(n)
print("The Largest Number is : " , max(List))
