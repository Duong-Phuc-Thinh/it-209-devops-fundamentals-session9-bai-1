# Bài 1: Kiểm tra Cài đặt Docker Engine và Chạy Container Hello-World

Thư mục nộp bài: `homework/session_09/ex1/`

## 1. Giới thiệu
Bài tập này thực hiện kiểm tra trạng thái cài đặt Docker Engine trên hệ thống và khởi chạy container đầu tiên với `hello-world` nhằm đảm bảo:
- Docker CLI và Docker Daemon giao tiếp bình thường mà không cần tiền tố `sudo`.
- Image `hello-world` được pull từ Docker Hub và chạy thành công, in ra chuỗi thông điệp xác nhận chuẩn.

## 2. Các chức năng của mã nguồn (`main.py`)
- **Tự động hóa kiểm tra**: Thực thi 3 câu lệnh CLI chuẩn: `docker version`, `docker info`, và `docker run hello-world`.
- **Kiểm tra kết quả mong đợi**: Xác thực chuỗi `"Hello from Docker! This message shows that your installation appears to be working correctly."` trong đầu ra của container.
- **Tạo báo cáo tự động**: Ghi lại toàn bộ log terminal vào tệp `REPORT.md` theo đúng quy cách nộp bài.

## 3. Hướng dẫn chạy chương trình

### Điều kiện tiên quyết
Nếu gặp lỗi phân quyền khi chạy docker không có `sudo`, hãy chạy lệnh thêm user vào nhóm docker:
```bash
sudo usermod -aG docker $USER && newgrp docker
```

### Chạy script kiểm tra
```bash
python3 main.py
```

Sau khi chạy, kết quả sẽ được cập nhật trực tiếp vào file `REPORT.md`.
