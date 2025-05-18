# Tài Liệu Hướng Dẫn Sử Dụng Công Cụ Tạo Xác Thực Cơ Bản

## Mô Tả Chức Năng

Công cụ tạo xác thực cơ bản là một phần mềm dùng để tạo các tiêu đề ủy quyền được mã hóa dưới dạng Base64 cho giao thức xác thực HTTP cơ bản. Khi cung cấp tên người dùng và mật khẩu, công cụ có thể nhanh chóng tạo ra tiêu đề ủy quyền tương ứng, thuận tiện cho các nhà phát triển sử dụng trong quá trình phát triển phần mềm.

## Hướng Dẫn Sử Dụng

### Nhập Tên Người Dùng

Tại ô nhập liệu "Username", hãy nhập vào tên người dùng mà bạn muốn sử dụng. Đây có thể là bất kỳ tên nào bạn mong muốn để tiến hành xác thực.

### Nhập Mật Khẩu

Nhập mật khẩu tương ứng với tên người dùng đã cung cấp vào ô "Password". Trong quá trình nhập, mật khẩu sẽ tự động bị ẩn đi nhằm bảo vệ an toàn thông tin mật khẩu của bạn.

### Kiểm Tra Tiêu Đề Ủy Quyền Được Tạo Ra

Sau khi nhập xong tên người dùng và mật khẩu, công cụ sẽ tự động tạo tiêu đề ủy quyền phù hợp. Tiêu đề này sẽ được hiển thị theo định dạng như sau:

```
Authorization header:
Authorization: Basic [Chuỗi ký tự được mã hóa Base64]
```

Trong đó, "Basic" biểu thị việc sử dụng phương pháp xác thực cơ bản, chuỗi ký tự phía sau là kết quả của việc mã hóa Base64 từ tổ hợp tên người dùng và mật khẩu theo định dạng "tên người dùng:mật khẩu".

### Sao Chép Tiêu Đề Ủy Quyền

Nếu bạn cần sử dụng tiêu đề ủy quyền đã được tạo ở một nơi khác, bạn có thể nhấn vào nút "Copy header" để sao chép tiêu đề này vào bộ nhớ tạm. Bằng cách này, bạn có thể dễ dàng dán nó vào các tệp tin hoặc đoạn mã nơi yêu cầu.