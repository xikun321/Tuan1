a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
phep_tinh = input("Chọn phép tính (+, -, *, /): ")
if phep_tinh == '+':
    print(f"Kết quả: {a + b}")
elif phep_tinh == '-':
    print(f"Kết quả: {a - b}")
elif phep_tinh == '*':
    print(f"Kết quả: {a * b}")
elif phep_tinh == '/':
    print(f"Kết quả: {a / b}")
else:
    print("Phép tính không hợp lệ")
