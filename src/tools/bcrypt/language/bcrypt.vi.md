# Hướng dẫn sử dụng công cụ mã hóa văn bản

## 1. Tổng quan về công cụ

Đây là một công cụ mã hóa văn bản mạnh mẽ, chủ yếu dựa trên thuật toán bcrypt, hỗ trợ mã hóa văn bản và so sánh giá trị băm (hash) với văn bản gốc. Nó có thể được áp dụng trong các tình huống liên quan đến bảo mật như lưu trữ và xác thực mật khẩu.

## 2. Truy cập công cụ

Nhập URL của trang chứa công cụ vào thanh địa chỉ trình duyệt, nhấn "Enter" để truy cập trang và chờ cho đến khi tất cả các phần tử trên trang được tải hoàn toàn.

## 3. Hướng dẫn thao tác

### (1) Mã hóa văn bản

1. **Nhập văn bản** : Tại ô nhập liệu "Your string", hãy nhập nội dung văn bản bạn muốn mã hóa. Ví dụ: mật khẩu do người dùng thiết lập lúc đăng ký.
2. **Thiết lập Salt count** : Nhấn vào các nút "+" hoặc "-" cạnh "Salt count" để điều chỉnh số lần lặp lại của giá trị Salt. Salt là chuỗi ký tự ngẫu nhiên được thêm vào văn bản gốc trước khi mã hóa nhằm tăng cường tính bảo mật và ngăn chặn các cuộc tấn công như kiểu Rainbow Table. Thông thường nên đặt không dưới 10 lần lặp.
3. **Xem kết quả mã hóa** : Sau khi hoàn tất các thiết lập trên, công cụ sẽ tự động mã hóa văn bản đã nhập và hiển thị giá trị hash tương ứng tại ô phía dưới.