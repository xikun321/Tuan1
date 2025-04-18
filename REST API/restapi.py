import requests

# Gọi API và xử lý dữ liệu
def lay_va_phan_tich_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("Hiển thị 5 bài viết đầu tiên:\n")
        for i, post in enumerate(data[:5]):
            print(f"Bài viết {i+1}:")
            print(f"ID: {post['id']}")
            print(f"User ID: {post['userId']}")
            print(f"Tiêu đề: {post['title']}")
            print(f"Nội dung: {post['body']}\n{'-'*40}\n")
    else:
        print(f"Lỗi khi gọi API. Mã lỗi: {response.status_code}")

# Chạy hàm chính
lay_va_phan_tich_api()
