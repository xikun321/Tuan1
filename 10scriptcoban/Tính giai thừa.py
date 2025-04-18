def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

num = int(input("Nhập số để tính giai thừa: "))
print(f"{num}! = {factorial(num)}")
