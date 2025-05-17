# A Toolio - Tài liệu Hướng dẫn Công cụ Phân tích JWT

## 1. Mô tả Công cụ

A Toolio - Công cụ phân tích JWT là một công cụ trực tuyến tiện ích có thể phân tích và giải mã các token web JSON (JWT) và hiển thị rõ ràng nội dung của chúng. Nó cung cấp cho các nhà phát triển cách nhanh chóng xem chi tiết của JWT, từ đó hỗ trợ hiệu quả cho việc gỡ lỗi, xác thực và học tập.

## 2. Mô tả Tính năng

### (A) Tính năng Nhập dữ liệu

* **Ô nhập JWT** : Người dùng có thể dán JWT muốn phân tích vào ô nhập này. Ô nhập có dung lượng lớn, có thể chứa được các JWT với độ dài khác nhau, mang lại tính linh hoạt trong việc nhập liệu.

### (B) Tính năng Phân tích

* **Phân tích phần Header (Header)** : Có thể trích xuất chính xác thông tin từ phần tiêu đề của JWT, bao gồm các trường sau:
  * **alg (Algorithm)** : Hiển thị thuật toán mã hóa được sử dụng bởi JWT, ví dụ HS256 biểu thị việc sử dụng thuật toán HMAC với SHA-256.
  * **typ (Type)** : Hiển thị loại của JWT, thường là "JWT".

* **Phân tích phần Payload (Payload)** : Có thể phân tích chi tiết phần payload của JWT và hiển thị các khai báo (claims), ví dụ như:
  * **sub (Subject)** : Xác định người dùng hoặc đối tượng mà JWT hướng đến.
  * **name (Full name)** : Hiển thị tên đầy đủ của người dùng.
  * **iat (Issued At)** : Chỉ thời điểm JWT được phát hành, thường được hiển thị dưới dạng dấu thời gian (timestamp), có thể chuyển đổi thành định dạng ngày giờ cụ thể.

### (C) Tính năng Hiển thị

* **Hiển thị theo cấu trúc bảng** : Nội dung JWT đã phân tích sẽ được trình bày rõ ràng dưới dạng bảng cấu trúc, giúp người dùng dễ dàng nắm bắt ý nghĩa và giá trị của từng trường, làm cho thông tin trực quan và dễ đọc hơn.

## 3. Các Bước Sử Dụng

1. **Truy cập đường dẫn URL** : Mở [https://atoolio.com/jwt-parser](https://atoolio.com/jwt-parser) bằng trình duyệt để truy cập trang công cụ phân tích JWT.
2. **Nhập JWT** : Dán JWT mà bạn muốn phân tích vào ô nhập liệu.
3. **Nhấn nút phân tích** : Nhấn vào nút phân tích (thường nằm bên cạnh mục "JWT to decode", tên gọi chính xác phụ thuộc vào giao diện), hệ thống sẽ tự động phân tích JWT đã nhập.
4. **Xem kết quả** : Trong khu vực phía dưới, xem thông tin phân tích về phần Header và Payload để hiểu rõ nội dung chi tiết của JWT.

## 4. Lưu ý Quan Trọng

* Hãy đảm bảo rằng JWT bạn nhập có định dạng đúng, nếu không sẽ gây ra lỗi phân tích hoặc kết quả không chính xác.
* Công cụ này chỉ phục vụ cho việc phân tích và hiển thị nội dung của JWT, không đảm bảo phân tích hoàn toàn chính xác tất cả các loại JWT, đặc biệt là những JWT sử dụng thuật toán mã hóa đặc biệt hoặc định dạng không chuẩn.
* Trong quá trình sử dụng, nếu gặp vấn đề hay cần hỗ trợ, bạn có thể liên hệ qua các kênh hỗ trợ do trang web cung cấp (ví dụ như mục "Buy me a coffee" có thể ám chỉ bạn có thể liên lạc với nhà phát triển thông qua chức năng này).

Tài liệu này nhằm mục đích giúp bạn hiểu rõ hơn và sử dụng hiệu quả công cụ này để xử lý các nhiệm vụ liên quan đến JWT.