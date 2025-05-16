# Tài liệu hướng dẫn sử dụng công cụ phân tích người dùng trực tuyến

## 1. Giới thiệu về công cụ

Công cụ phân tích người dùng trực tuyến có khả năng phát hiện và phân tích chính xác thông tin về trình duyệt, động cơ render, hệ điều hành, kiến trúc CPU cũng như loại/mô hình thiết bị từ chuỗi đại diện người dùng (user agent string). Công cụ này giúp các nhà phát triển nhanh chóng thu thập các chi tiết liên quan đến thiết bị đầu cuối (client).

## 2. Mô tả chức năng

### (1) Nhận diện trình duyệt

Công cụ có thể nhận diện chính xác loại trình duyệt mà người dùng đang sử dụng cùng phiên bản cụ thể. Ví dụ, khi nhập một chuỗi nhất định, nếu hiển thị "Edge 135.0.0.0", điều này cho thấy trình duyệt của người dùng là Edge với phiên bản 135.0.0.0.

### (2) Nhận diện động cơ render

Hiển thị rõ ràng động cơ render được sử dụng bởi trình duyệt và phiên bản tương ứng. Ví dụ: nếu hiển thị "Blink 135.0.0.0" thì có nghĩa là động cơ render là Blink với phiên bản 135.0.0.0.

### (3) Nhận diện hệ điều hành

Cung cấp thông tin chi tiết về tên hệ điều hành và phiên bản của nó. Ví dụ, "Windows 10" cho biết hệ điều hành là Windows và phiên bản là 10.

### (4) Nhận diện thông tin thiết bị

Cho phép truy xuất thông tin như loại thiết bị, mô hình và nhà sản xuất (nếu có sẵn). Ví dụ, một số thiết bị có thể hiển thị đầy đủ mô hình của chúng; tuy nhiên cũng tồn tại một số trường hợp không có sẵn thông tin mô hình, loại hoặc nhà sản xuất của thiết bị, lúc đó sẽ có thông báo tương ứng: "No device model/type/vendor available".

### (5) Nhận diện thông tin CPU

Có thể nhận diện các đặc điểm liên quan đến CPU. Ví dụ, nếu hiển thị "amd64", điều này cho thấy kiến trúc CPU thuộc loại amd64.

## 3. Ví dụ sử dụng

### Ví dụ 1: Trường hợp trình duyệt máy tính để bàn phổ biến

Giả sử chuỗi đại diện người dùng là:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0

Sau khi nhập chuỗi này vào công cụ phân tích:

  * **Trình duyệt**: Được xác định là Edge 135.0.0.0.
  * **Động cơ**: Được xác định là Blink 135.0.0.0.
  * **Hệ điều hành**: Là Windows 10.
  * **Thiết bị**: Không có sẵn mô hình, loại hoặc nhà sản xuất thiết bị cụ thể, do đó sẽ hiển thị thông báo phù hợp.
  * **CPU**: Kiến trúc là amd64.

### Ví dụ 2: Trường hợp trình duyệt trên thiết bị di động

Xét chuỗi đại diện người dùng sau:
Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1

Sau khi nhập chuỗi này vào công cụ phân tích:

  * **Trình duyệt**: Có thể xác định trình duyệt Safari trên nền tảng iOS cùng phiên bản tương ứng (phiên bản cụ thể phụ thuộc vào kết quả phân tích thực tế).
  * **Động cơ**: Hiển thị động cơ Webkit tương ứng cùng các chi tiết về phiên bản.
  * **Hệ điều hành**: Rõ ràng xác định là hệ điều hành iOS cùng số hiệu phiên bản (ví dụ như 16_6_1...).
  * **Thiết bị**: Thu thập được thông tin thiết bị, ví dụ như đây là iPhone (mô hình cụ thể phụ thuộc vào kết quả phân tích).
  * **CPU**: Hiển thị kiến trúc CPU phù hợp với thiết bị di động (nếu có phần nào có thể xác định rõ ràng).