# Tài liệu Hướng dẫn Công cụ Chuyển đổi Địa chỉ IPv4

## 1. Giới thiệu về Công cụ

Công cụ Chuyển đổi Địa chỉ IPv4 là một công cụ trực tuyến giúp chuyển đổi địa chỉ IPv4 sang các hệ thống số khác nhau (thập phân, thập lục phân, nhị phân) và cả định dạng IPv6. Công cụ này hỗ trợ các nhà phát triển và kỹ thuật viên mạng trong việc nhanh chóng lấy được nhiều dạng biểu diễn khác nhau của địa chỉ IPv4, từ đó thuận tiện cho việc cấu hình mạng, phát triển phần mềm hoặc phân tích bảo mật.

## 2. Mô tả Chi tiết về Các Tính năng

### (A) Nhập địa chỉ IPv4
- Trong ô nhập liệu của công cụ, người dùng có thể nhập trực tiếp một địa chỉ IPv4 hợp lệ (ví dụ: 192.168.1.1). Sau khi nhập xong, nhấn vào nút "Chuyển đổi" hoặc phím Enter để bắt đầu quá trình chuyển đổi tự động.

### (B) Chuyển đổi sang Hệ thập phân
- **Tính năng**: Biến đổi địa chỉ IPv4 thành một giá trị thập phân.
- **Cách sử dụng**: Khi địa chỉ IPv4 đã được nhập vào, công cụ sẽ tự động tính toán và hiển thị giá trị thập phân tương ứng. Giá trị này được tạo ra bằng cách chuyển đổi từng byte trong 4 byte của địa chỉ IPv4 sang số thập phân, sau đó kết hợp chúng theo một phương pháp cụ thể.

### (C) Chuyển đổi sang Hệ thập lục phân
- **Tính năng**: Biến đổi địa chỉ IPv4 thành chuỗi số thập lục phân.
- **Cách sử dụng**: Khi địa chỉ IPv4 được nhập vào, mỗi byte sẽ được chuyển đổi thành hai ký tự thập lục phân, sau đó ghép nối lại với nhau để tạo thành một chuỗi thập lục phân hoàn chỉnh. Ví dụ, địa chỉ IPv4 192.168.1.1 sẽ được chuyển đổi thành C0A80101.

### (D) Chuyển đổi sang Hệ nhị phân
- **Tính năng**: Biến đổi địa chỉ IPv4 thành dạng nhị phân.
- **Cách sử dụng**: Khi nhập địa chỉ IPv4 vào, từng byte sẽ được chuyển đổi thành số nhị phân 8 bit, sau đó bốn byte sẽ được nối lại với nhau để tạo thành một chuỗi nhị phân 32 bit. Ví dụ, địa chỉ IPv4 192.168.1.1 sẽ được biểu diễn dưới dạng nhị phân là 11000000101010000000000100000001.

### (E) Chuyển đổi sang Định dạng IPv6
- **Tính năng**: Biến đổi địa chỉ IPv4 sang định dạng IPv6.
- **Cách sử dụng**: Công cụ sẽ tạo ra hai loại định dạng IPv6:
  1. **Địa chỉ IPv6 đầy đủ**: 8 byte đầu tiên được điền bằng số 0, 8 byte cuối cùng chứa phiên bản thập lục phân của địa chỉ IPv4, đồng thời thêm "ffff" phía trước phần địa chỉ IPv4 để nhận diện. Ví dụ, từ địa chỉ IPv4 192.168.1.1, địa chỉ IPv6 đầy đủ được tạo ra là 0000:0000:0000:0000:0000:ffff:c0a8:0101.