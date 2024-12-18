import requests 

# Nhập URL từ người dùng
Inputs = input("Nhập Input của bạn: ").strip()

# Kiểm tra và thêm 'http://' nếu thiếu
if not Inputs.startswith("http://") and not Inputs.startswith("https://"):
    Inputs = "https://" + Inputs

try:
    # Gửi yêu cầu GET đến URL
    req = requests.get(Inputs)

    # Kiểm tra mã trạng thái
    if req.status_code == 200:
        print(req.status_code)
        print("CC - Yêu cầu thành công!")
        req.encoding = 'utf-8'
        print(req.text)
    else:
        print(req.status_code)
        print("TTT - Yêu cầu thất bại!")
except requests.exceptions.RequestException as e:
    print("Lỗi khi thực hiện yêu cầu:", e)
