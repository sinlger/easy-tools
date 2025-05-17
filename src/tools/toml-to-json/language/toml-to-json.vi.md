# Tài liệu hướng dẫn người dùng công cụ chuyển đổi trực tuyến từ TOML sang JSON

## 1. Giới thiệu công cụ

TOML sang JSON là một công cụ trực tuyến tiện lợi, phân tích dữ liệu ở định dạng TOML và chuyển đổi chúng sang định dạng JSON. Người dùng có thể dễ dàng dán hoặc nhập dữ liệu định dạng TOML vào ô nhập liệu ở bên trái, kết quả tương ứng ở định dạng JSON sẽ được tự động tạo ra ở bên phải.

## 2. Mô tả chi tiết chức năng

### 1. Nhập dữ liệu định dạng TOML

* Trong ô văn bản bên trái có tên "Your TOML", người dùng có thể dán hoặc nhập thủ công dữ liệu ở định dạng TOML. Ô văn bản này hỗ trợ nhập văn bản nhiều dòng, cung cấp không gian đầy đủ để nhập các thông tin cấu hình phức tạp hơn dưới định dạng TOML.

### 2. Xuất kết quả định dạng JSON

* Ngay khi dữ liệu TOML được nhập hoặc dán vào ô văn bản bên trái, công cụ sẽ tự động phân tích và chuyển đổi. Dữ liệu JSON sau khi chuyển đổi sẽ hiển thị trong ô văn bản bên phải với tiêu đề "JSON from your TOML". Người dùng có thể xem, sao chép hoặc xử lý tiếp dữ liệu này.

## 3. Các bước sử dụng

1. Mở trang web của công cụ ([https://atoolio.com/toml-to-json](https://atoolio.com/toml-to-json)).
2. Tại ô văn bản bên trái có tên "Your TOML", hãy dán hoặc nhập vào dữ liệu TOML mà bạn muốn chuyển đổi.
3. Hệ thống sẽ tự động thực hiện chuyển đổi và kết quả sẽ được hiển thị tại ô văn bản bên phải có tiêu đề "JSON from your TOML".

## 4. Các tính năng chính

* Giao diện đơn giản, trực quan: Công cụ có giao diện rõ ràng, dễ sử dụng, quy trình vận hành đơn giản, không yêu cầu thiết lập hay cấu hình phức tạp, giúp người dùng nhanh chóng làm quen và sử dụng.
* Chuyển đổi theo thời gian thực: Sau khi nhập dữ liệu TOML, công cụ sẽ tự động chuyển đổi và hiển thị kết quả, không cần nhấn nút chuyển đổi thủ công, nhờ đó nâng cao hiệu suất chuyển đổi.
* Sử dụng trên nền tảng trực tuyến: Không cần cài đặt phần mềm nào cả. Miễn là có thiết bị kết nối Internet, bạn có thể sử dụng công cụ này mọi lúc, mọi nơi để chuyển đổi dữ liệu từ TOML sang JSON.

## 5. Ví dụ minh họa

### Ví dụ 1: Chuyển đổi cơ bản từ TOML sang JSON

Giả sử chúng ta có dữ liệu sau đây ở định dạng TOML:
```toml
title = "TOML Example"
owner = "John Doe"
```

Khi dán những dữ liệu này vào ô văn bản bên trái có tên "Your TOML", công cụ sẽ tự động chuyển đổi sang định dạng JSON như sau:
```json
{
  "title": "TOML Example",
  "owner": "John Doe"
}
```

### Ví dụ 2: Chuyển đổi từ TOML sang JSON với cấu trúc lồng ghép

Chúng ta có dữ liệu TOML phức tạp hơn:
```toml
[database]
server = "192.168.1.1"
ports = [8001, 8002, 8003]
connection_max = 5000
```

Sau khi nhập vào công cụ, chúng ta sẽ nhận được dữ liệu JSON như sau:
```json
{
  "database": {
    "server": "192.168.1.1",
    "ports": [8001, 8002, 8003],
    "connection_max": 5000
  }
}