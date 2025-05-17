# Tài liệu hướng dẫn người dùng công cụ chuyển đổi TOML sang YAML

## Tổng quan

TOML sang YAML là một công cụ trực tuyến cho phép người dùng dễ dàng chuyển đổi các tệp cấu hình định dạng TOML (Tom's Obvious, Minimal Language) sang định dạng YAML (YAML Ain't Markup Language). Đây là công cụ hữu ích đặc biệt đối với các nhà phát triển cần di chuyển cấu hình giữa các hệ thống khác nhau hoặc tích hợp nhiều công nghệ khác nhau.

## Giao diện người dùng

Giao diện của công cụ được thiết kế đơn giản và trực quan, bao gồm các thành phần chính sau:

1. Ô nhập liệu bên trái: Đây là khu vực người dùng có thể nhập hoặc dán văn bản định dạng TOML, được ghi chú là "Your TOML".
2. Ô nhập liệu bên phải: Được sử dụng để hiển thị văn bản đã chuyển đổi sang định dạng YAML, được ghi chú là "YAML from your TOML".
3. Nút chuyển đổi ở giữa: Sau khi người dùng nhập xong văn bản TOML, họ có thể nhấn vào nút này để thực hiện quá trình chuyển đổi.

## Mô tả chức năng

### Nhập văn bản TOML

- Người dùng có thể trực tiếp nhập văn bản cấu hình định dạng TOML vào ô nhập liệu bên trái.
- Họ cũng có thể sao chép văn bản TOML từ các tệp tin hoặc trình soạn thảo khác và dán vào ô nhập liệu này.

### Quy trình chuyển đổi

- Sau khi văn bản TOML được nhập hoặc dán vào, hãy nhấn vào nút chuyển đổi ở giữa. Hệ thống sẽ ngay lập tức phân tích văn bản TOML đã nhập và chuyển đổi nó sang định dạng YAML.
- Khi quá trình chuyển đổi hoàn tất, văn bản YAML kết quả sẽ được hiển thị trong ô nhập liệu bên phải.

### Xem kết quả chuyển đổi YAML

- Ô nhập liệu bên phải hiển thị toàn bộ văn bản YAML đã được chuyển đổi.
- Tại đây, người dùng có thể kiểm tra xem kết quả chuyển đổi có chính xác không và cấu trúc văn bản YAML có đáp ứng kỳ vọng của họ không.

### Sao chép văn bản YAML

- Người dùng có thể chọn và sao chép toàn bộ văn bản YAML trong ô nhập liệu bên phải, điều này rất tiện lợi khi họ cần sử dụng ở những nơi khác, ví dụ như dán vào các tệp cấu hình hoặc gửi cho người khác.

## Ví dụ

### Ví dụ 1: Chuyển đổi cơ bản

**Dữ liệu đầu vào định dạng TOML:**

```toml
# Đây là ví dụ đơn giản về TOML
title = "Ví dụ TOML"

[author]
name = "Trương Tam"
age = 28
email = "zhangsan@example.com"
```

**Kết quả đầu ra định dạng YAML:**

```yaml
# Đây là ví dụ đã được chuyển đổi sang YAML
title: Ví dụ TOML

author:
  name: Trương Tam
  age: 28
  email: zhangsan@example.com
```

### Ví dụ 2: Chuyển đổi cấu trúc phức tạp

**Dữ liệu đầu vào định dạng TOML:**

```toml
# Ví dụ về TOML với cấu trúc phức tạp hơn
database:
  host = "localhost"
  port = 3306
  user = "admin"
  password = "securepassword"

[features]
logging = true
debug = false

[[servers]]
name = "main-server"
port = 8080

[[servers]]
name = "secondary-server"
port = 8081
```

**Kết quả đầu ra định dạng YAML:**

```yaml
# Ví dụ về YAML với cấu trúc phức tạp hơn
database:
  host: localhost
  port: 3306
  user: admin
  password: securepassword

features:
  logging: true
  debug: false

servers:
  - name: main-server
    port: 8080
  - name: secondary-server
    port: 8081
```

## Lưu ý quan trọng

- Nếu định dạng TOML được nhập vào không chính xác, quá trình chuyển đổi có thể thất bại và hệ thống có thể hiển thị thông báo lỗi.
- Công cụ hỗ trợ hầu hết các cấu trúc cú pháp TOML phổ biến, tuy nhiên đối với một số yếu tố cú pháp đặc biệt hoặc ít sử dụng, việc chuyển đổi hoàn hảo có thể không khả thi.
- Văn bản YAML tạo ra có thể có những khác biệt nhỏ về định dạng tùy thuộc vào phiên bản và đặc tả YAML được sử dụng.