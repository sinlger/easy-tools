# Công cụ phân tích URL

## 1. Tổng quan về công cụ
Công cụ phân tích URL là một công cụ trực tuyến dùng để phân tích các chuỗi URL, có khả năng tách biệt các URL phức tạp thành nhiều thành phần như giao thức, tên người dùng, mật khẩu, tên máy chủ, cổng kết nối, đường dẫn, tham số,... từ đó giúp các nhà phát triển nhanh chóng nắm bắt cấu trúc và thông tin chi tiết của URL, thuận tiện cho việc xây dựng, gỡ lỗi và phân tích các yêu cầu mạng.

## 2. Chi tiết chức năng

  1. **Ô nhập liệu**
     * Cung cấp ô nhập liệu để bạn nhập chuỗi URL cần phân tích.

  2. **Hiển thị kết quả phân tích**
     * **Giao thức (Protocol)** : Hiển thị phần giao thức trong URL, ví dụ như "https:", thể hiện giao thức truyền tải mạng mà URL đang sử dụng.
     * **Tên người dùng (Username)** : Nếu URL chứa thông tin tên người dùng, thì sẽ hiển thị tại đây, được dùng để xác định danh tính người dùng cung cấp trong URL.
     * **Mật khẩu (Password)** : Hiển thị phần mật khẩu trong URL, kết hợp cùng tên người dùng để xác thực danh tính người dùng.
     * **Tên máy chủ (Hostname)** : Hiển thị tên miền tương ứng với URL, ví dụ như "atoolio.com", đại diện cho tên máy chủ mục tiêu.
     * **Cổng kết nối (Port)** : Hiển thị số cổng được chỉ định trong URL, dùng để xác định cổng kết nối cụ thể trên máy chủ nơi dịch vụ được cung cấp. Mặc định, mỗi giao thức sẽ có cổng kết nối mặc định khác nhau, ví dụ: cổng 80 dành cho HTTP, cổng 443 dành cho HTTPS.
     * **Đường dẫn (Path)** : Hiển thị phần đường dẫn trong URL, ví dụ như "/url-parser", trỏ đến vị trí tài nguyên hoặc dịch vụ cụ thể trên máy chủ.
     * **Tham số (Params)** : Liệt kê phần tham số truy vấn trong URL, bắt đầu bằng ký tự "?", tiếp theo là nhiều cặp "khóa-giá trị" làm tham số, ví dụ như "?key1=value&key2=value2", được dùng để gửi thêm thông tin và lệnh đến máy chủ.
     * **Hiển thị chi tiết tham số** : Mỗi cặp khóa-giá trị của tham số truy vấn sẽ được hiển thị riêng lẻ, rõ ràng tên của từng tham số và giá trị tương ứng.

## 3. Các bước sử dụng

  1. Mở trình duyệt web và truy cập trang [Công cụ phân tích URL](https://atoolio.com/url-parser).
  2. Nhập chuỗi URL mà bạn muốn phân tích vào ô nhập liệu, ví dụ như "https://me:pwd@atoolio.com:3000/url-parser?key1=value&key2=value2#the-hash".
  3. Nhấn vào nút phân tích (thông thường nhấn Enter cũng có thể kích hoạt phân tích), công cụ sẽ tự động phân tích URL đã nhập và hiển thị thông tin chi tiết của từng thành phần bên dưới.
  4. Kiểm tra kết quả phân tích, sao chép phần nội dung tương ứng của các thành phần khi cần thiết để sử dụng cho các công việc phát triển, gỡ lỗi hoặc các thao tác khác.

## 4. Ví dụ

  1. **Ví dụ 1**
     * URL đã nhập: "http://user:pass@example.com:8080/page?param1=hello&param2=world"
     * Kết quả phân tích:
       * Giao thức: http:
       * Tên người dùng: user
       * Mật khẩu: pass
       * Tên máy chủ: example.com
       * Cổng kết nối: 8080
       * Đường dẫn: /page
       * Tham số: ?param1=hello&param2=world
       * Hiển thị chi tiết tham số:
         * param1: hello
         * param2: world

  2. **Ví dụ 2**
     * URL đã nhập: "https://www.google.com/s?wd=Công cụ phân tích URL"
     * Kết quả phân tích:
       * Giao thức: https:
       * Tên người dùng: (không có)
       * Mật khẩu: (không có)
       * Tên máy chủ: www.google.com
       * Cổng kết nối: (cổng mặc định 443, không hiển thị)
       * Đường dẫn: /s
       * Tham số: ?wd=Công cụ phân tích URL
       * Hiển thị chi tiết tham số:
         * wd: Công cụ phân tích URL