# Tài liệu Hướng dẫn Sử dụng Trình tạo HMAC trực tuyến của A Toolio

## 1. Mô tả Công cụ

Trình tạo HMAC trực tuyến được cung cấp bởi A Toolio có thể tính toán các mã xác thực thông điệp dựa trên băm (HMAC) bằng cách sử dụng một khóa bí mật và hàm băm, rất phù hợp cho các nhà phát triển cần nhanh chóng tạo ra các mã HMAC trong nhiều tình huống phát triển khác nhau.

## 2. Mô tả Tính năng

### Phần Nhập liệu

1. **Văn bản gốc** - Nhập văn bản bạn muốn tính giá trị băm.
2. **Khóa bí mật** - Nhập khóa bí mật dùng để tạo mã HMAC.
3. **Hàm băm** - Chọn hàm băm mong muốn. Mặc định là SHA256, tuy nhiên bạn cũng có thể chọn các hàm băm khác theo nhu cầu.
4. **Chế độ mã hóa đầu ra** - Chọn định dạng mã hóa đầu ra mong muốn. Mặc định là hệ thập lục phân (cơ số 16), nhưng cũng có thể chọn các định dạng khác.

### Phần Xuất kết quả

1. **HMAC of your text** - Hiển thị giá trị HMAC đã được tạo, với nút sao chép giúp dễ dàng chuyển kết quả sang nơi khác.

## 3. Các Bước Sử dụng

**Bước 1: Nhập văn bản và khóa bí mật**

Nhập văn bản bạn muốn xử lý vào ô "Văn bản gốc", sau đó nhập khóa bí mật vào ô tương ứng. Những dữ liệu này phải được nhập chính xác.

**Bước 2: Chọn hàm băm**

Từ menu xổ xuống "Hàm băm", hãy chọn hàm băm phù hợp như SHA256, SHA1,... tùy vào nhu cầu sử dụng của bạn. Các hàm băm khác nhau sẽ cho ra kết quả HMAC khác nhau.

**Bước 3: Chọn chế độ mã hóa đầu ra**

Chọn định dạng mã hóa mong muốn từ menu "Chế độ mã hóa đầu ra" như định dạng thập lục phân (cơ số 16) hoặc Base64. Điều này quyết định cách thức biểu diễn giá trị HMAC được tạo ra.

**Bước 4: Tạo và Xem HMAC**

Sau khi hoàn tất các bước trên, hệ thống sẽ tự động tính toán giá trị HMAC và hiển thị nó trong phần "HMAC of your text". Bạn có thể xem kết quả trực tiếp tại đây.

**Bước 5: Sao chép giá trị HMAC**

Nếu bạn cần sử dụng giá trị HMAC này, hãy nhấn vào nút sao chép bên cạnh kết quả để lưu giá trị vào bộ nhớ tạm và dán nó vào vị trí mong muốn.