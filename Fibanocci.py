# program to write the Fibonacci Series, Calucate the value based on the position and caluclatinv the postion based on the value
def fibonacci_series(n):
    series = []
    a , b = 0 , 1
    for _ in range(n):
        series.append(a)
        a , b = b , a+b
    return series
n = int(input(" Enter the number of elements you want : "))
print(f" {n} Fibonacci series ", fibonacci_series(n))


def fibonacci_value(k):
    if k==1 or k==2:
        return 1
    else:
        return fibonacci_value(k-1)+fibonacci_value(k-2)
k = int(input("Enter the Value postion : "))
print(f"The value of the position {k} in the Fibonacci Series : ",fibonacci_value(k))


def fibonacci_position(p):
    a , b = 0 , 1
    position = 0 
    while p<=p:
        if a == p:
            return position
        a , b = b , a+b
        position +=1
    return -1
p = int(input("Enter the Value : "))
print(f"The Position of the value {p} in the Fibonacci Series : ", fibonacci_position(p))


        