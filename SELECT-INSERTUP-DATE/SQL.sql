-- 1. Tạo bảng nếu chưa tồn tại
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER
);

-- 2. Chèn dữ liệu vào bảng
INSERT INTO users (name, email, age)
VALUES 
    ('Nguyen Van A', 'vana@example.com', 25),
    ('Tran Thi B', 'thib@example.com', 32),
    ('Le Van C', 'lvc@example.com', 28);

-- 3. Lấy toàn bộ người dùng
SELECT * FROM users;

-- 4. Lấy tên và email người dùng trên 30 tuổi
SELECT name, email FROM users
WHERE age > 30;

-- 5. Cập nhật tuổi người dùng có email là 'vana@example.com'
UPDATE users
SET age = 35
WHERE email = 'vana@example.com';

-- 6. Lấy toàn bộ người dùng sắp xếp theo tuổi giảm dần
SELECT * FROM users
ORDER BY age DESC;
