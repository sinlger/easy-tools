# Tài liệu hướng dẫn người dùng công cụ tạo cặp khóa RSA

## 1. Tổng quan về công cụ

Công cụ trực tuyến này cho phép bạn dễ dàng tạo các chứng chỉ PEM ngẫu nhiên chứa khóa riêng và khóa công khai RSA. Nó đặc biệt hữu ích đối với các nhà phát triển cần nhanh chóng tạo một cặp khóa RSA trong quá trình phát triển phần mềm.

## 2. Mô tả chức năng

### (1) **Thiết lập độ dài khóa**

* **Chức năng**: Người dùng có thể thiết lập độ dài của khóa (tính bằng bit) trong một phạm vi xác định.
* **Hành động**: Nhập vào ô "Bits" độ dài mong muốn, ví dụ như 2048 bit thường được sử dụng. Công cụ hỗ trợ một số độ dài bit nhất định để đảm bảo khóa được tạo ra đáp ứng yêu cầu an toàn và mục đích sử dụng.
* **Mục đích**: Thông thường, độ dài khóa càng lớn thì mức độ an toàn càng cao, tuy nhiên tốc độ mã hóa và giải mã có thể chậm lại. Vì vậy cần cân nhắc lựa chọn độ dài phù hợp với từng trường hợp sử dụng thực tế.

### (2) **Làm mới cặp khóa**

* **Chức năng**: Giúp tạo nhanh một cặp khóa RSA ngẫu nhiên mới.
* **Hành động**: Nhấn vào nút "Refresh key-pair", hệ thống sẽ tạo lại một cặp khóa mới bao gồm khóa công khai và khóa riêng dựa trên độ dài khóa hiện tại đã cấu hình.
* **Mục đích**: Khi bạn cần tạo nhiều cặp khóa khác nhau để thử nghiệm hoặc sử dụng trực tiếp, chỉ cần nhấn nút Refresh mà không cần điều chỉnh thủ công các thông số khác, giúp tăng hiệu suất làm việc.

### (3) **Khóa công khai - Hiển thị và quản lý**

* **Chức năng**: Hiển thị khóa công khai RSA đã được tạo và cung cấp các thao tác thuận tiện để sử dụng.
* **Hiển thị nội dung**: Trong phần "Public key", khóa công khai xuất hiện dưới dạng định dạng PEM tiêu chuẩn bao gồm các dòng "-----BEGIN PUBLIC KEY-----" và "-----END PUBLIC KEY-----", bạn có thể sao chép và sử dụng trực tiếp trong ứng dụng của mình.
* **Chức năng sao chép**: Nút sao chép bên cạnh giúp người dùng dễ dàng copy khóa công khai vào clipboard chỉ với một cú nhấp chuột, sau đó dán vào nơi cần thiết như tập tin cấu hình hay đoạn mã nguồn.

### (4) **Khóa riêng - Hiển thị và quản lý**

* **Chức năng**: Hiển thị khóa riêng RSA đã được tạo và cung cấp cách thức đơn giản để sử dụng.
* **Hiển thị nội dung**: Trong phần "Private key", định dạng PEM tiêu chuẩn cũng được áp dụng với các dòng đánh dấu "-----BEGIN RSA PRIVATE KEY-----" và "-----END RSA PRIVATE KEY-----", người dùng có thể sử dụng khóa này để thực hiện các thao tác như mã hóa, giải mã hoặc ký điện tử.
* **Chức năng sao chép**: Nút sao chép liền kề giúp bạn dễ dàng copy khóa riêng để sử dụng trong môi trường an toàn, ví dụ như lưu trữ trên máy chủ hoặc thiết lập cấu hình trong ứng dụng.

## 3. Ví dụ về tình huống sử dụng

1. Các nhà phát triển có thể tận dụng công cụ này khi cần tạo khóa thử nghiệm nhanh trong lúc xây dựng các ứng dụng dựa trên thuật toán mã hóa RSA. Họ có thể chọn độ dài khóa thích hợp, tạo cặp khóa bằng nút Refresh rồi sử dụng khóa công khai để mã hóa và khóa riêng để kiểm tra giải mã.
2. Khi thiết lập các giao thức truyền thông an toàn (ví dụ như SSL/TLS), nếu bạn cần chứng chỉ tự ký hoặc cặp khóa dành cho môi trường thử nghiệm, bạn có thể tạo chúng ở đây và cấu hình tương ứng khóa công khai và khóa riêng vào vị trí thích hợp trên máy chủ và máy khách.