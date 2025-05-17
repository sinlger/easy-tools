# Tài liệu Hướng dẫn Công cụ Tính toán Subnet IPv4

Công cụ tính toán Subnet IPv4 là một tiện ích trực tuyến thuận tiện, được thiết kế để phân tích các khối CIDR IPv4 và lấy thông tin chi tiết về mạng con. Dưới đây là phần mô tả chức năng và hướng dẫn sử dụng công cụ này:

## 1. Chức năng Nhập liệu

Trong ô nhập liệu, người dùng có thể nhập vào một địa chỉ IPv4, với hoặc không có mặt nạ mạng con (subnet mask). Ví dụ, bạn có thể nhập "192.168.0.1/24", công cụ sẽ thực hiện các phép tính tương ứng dựa trên dữ liệu đầu vào.

## 2. Kết quả của Phép tính

1. **Mặt nạ mạng (Netmask)**
   * Hiển thị sự kết hợp giữa địa chỉ IPv4 và mặt nạ mạng dưới dạng CIDR như "192.168.0.0/24", giúp người dùng hiểu rõ phạm vi mạng đang xử lý.

2. **Địa chỉ mạng (Network address)**
   * Cung cấp địa chỉ mạng bên trong mạng con, đây là địa chỉ đặc biệt đại diện cho toàn bộ mạng. Ví dụ: "192.168.0.0" cho thấy điểm bắt đầu của mạng con này.

3. **Mặt nạ mạng (Network mask)**
   * Trình bày mặt nạ mạng con dưới định dạng thập phân như "255.255.255.0", dùng để xác định ranh giới giữa phần địa chỉ mạng và phần địa chỉ máy chủ trong địa chỉ IP.

4. **Mặt nạ mạng dưới dạng nhị phân (Network mask in binary)**
   * Hiển thị mặt nạ mạng dưới dạng nhị phân như "11111111.11111111.11111111.00000000", hỗ trợ người dùng hiểu sâu hơn về nguyên lý hoạt động của mặt nạ mạng con.

5. **Ký hiệu CIDR (CIDR notation)**
   * Cho biết ký hiệu CIDR của mặt nạ mạng con, ví dụ "/24", là cách biểu diễn ngắn gọn độ dài của mặt nạ mạng, giúp nhanh chóng nắm bắt cách chia mạng.

6. **Mặt nạ Wildcard (Wildcard mask)**
   * Đưa ra giá trị của mặt nạ Wildcard như "0.0.0.255", mặt nạ này bổ sung cho mặt nạ mạng con và thường được dùng trong cấu hình của một số thiết bị mạng và phần mềm.

7. **Kích thước mạng (Network size)**
   * Thông báo tổng số địa chỉ IP khả dụng trong mạng con, ví dụ như "256", từ đó người dùng nắm được dung lượng của mạng con này.

8. **Địa chỉ đầu tiên khả dụng (First address)**
   * Hiển thị địa chỉ IP đầu tiên có thể gán cho máy chủ (host) trong mạng con, ví dụ "192.168.0.1", đánh dấu vị trí bắt đầu của dải địa chỉ khả dụng.

9. **Địa chỉ cuối cùng khả dụng (Last address)**
   * Trình bày địa chỉ IP cuối cùng có thể gán cho máy chủ (host) trong mạng con, như "192.168.0.254", xác định điểm kết thúc của dải địa chỉ khả dụng.

10. **Địa chỉ phát sóng (Broadcast address)**
    * Cung cấp địa chỉ phát sóng của mạng con này, ví dụ "192.168.0.255", được sử dụng để gửi thông điệp đến tất cả các máy chủ trong mạng con.

11. **Lớp địa chỉ IP (IP class)**
    * Chỉ ra lớp mà địa chỉ IP thuộc về, ví dụ như "C", hỗ trợ người dùng nhận biết cách phân loại địa chỉ IP này.

## 3. Chức năng Điều hướng

Hai nút bấm được cung cấp lần lượt có tên gọi "Khối trước (Previous block)" và "Khối tiếp theo (Next block)", giúp người dùng dễ dàng chuyển đổi qua lại giữa các khối mạng con liền kề để xem thông tin.