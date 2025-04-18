import random
import string

length = int(input("Độ dài mật khẩu: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Mật khẩu ngẫu nhiên:", password)
