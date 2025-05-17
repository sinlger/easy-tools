# Tài liệu Hướng dẫn Công cụ Mở rộng Dải IPv4

## 1. Giới thiệu về Công cụ

Công cụ Mở rộng Dải IPv4 tính toán các mạng IPv4 hiệu quả dựa trên địa chỉ IPv4 bắt đầu và kết thúc được cung cấp. Điều này bao gồm các khối mạng hợp lệ (được biểu diễn dưới dạng ký hiệu CIDR), dải địa chỉ và tổng số địa chỉ có sẵn trong dải đó.

## 2. Mô tả Chi tiết về Các Tính năng

### (A) Chức năng Nhập cơ bản

1. **Nhập địa chỉ bắt đầu** - Trong trường "Start address", hãy nhập địa chỉ IPv4 sẽ được sử dụng làm điểm bắt đầu, ví dụ như "192.168.1.1".
2. **Nhập địa chỉ kết thúc** - Trong trường "End address", hãy nhập địa chỉ IPv4 sẽ được dùng làm điểm kết thúc, ví dụ như "192.168.6.255".

### (B) Xử lý Tự động và Hiển thị Kết quả

1. **Điều chỉnh dải địa chỉ** - Công cụ tự động điều chỉnh địa chỉ bắt đầu và kết thúc để tạo ra một dải phù hợp hơn. Ví dụ: "192.168.1.1" sẽ được chuyển thành "192.168.0.0", và "192.168.6.255" sẽ trở thành "192.168.7.255".
2. **Tính toán số lượng địa chỉ** - Tổng số địa chỉ IPv4 khả dụng trong dải mới sẽ được tính toán, ví dụ từ "1.535" tăng lên "2.048", qua đó nâng cao hiệu quả sử dụng tài nguyên địa chỉ.
3. **Tạo ký hiệu CIDR** - Ký hiệu CIDR tương ứng với dải địa chỉ mới sẽ được hiển thị, như "192.168.0.0/21", giúp đơn giản hóa việc quản lý và cấu hình mạng.

## 3. Những Lưu ý Quan trọng

Hãy đảm bảo rằng các địa chỉ bắt đầu và kết thúc do người dùng nhập vào tuân theo đúng định dạng địa chỉ IPv4 để đảm bảo hoạt động chính xác của công cụ và kết quả thu được đáng tin cậy.