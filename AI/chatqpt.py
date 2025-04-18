
import openai

# Đặt API Key của bạn
openai.api_key = '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'

def get_openai_response(prompt):
    # Gửi yêu cầu đến OpenAI API với cách gọi đúng
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Hoặc "gpt-4" tùy thuộc vào mô hình bạn muốn sử dụng
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Trả về kết quả text từ API
    return response['choices'][0]['message']['content']

# Nhập prompt từ người dùng
prompt = input("Nhập prompt của bạn: ")

# Gọi hàm với prompt người dùng nhập
response_text = get_openai_response(prompt)
print("Kết quả từ AI:", response_text)
