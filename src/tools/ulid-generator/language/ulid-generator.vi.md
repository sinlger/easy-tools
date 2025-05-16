# Tài liệu người dùng cho công cụ tạo ULID

## 1. Tổng quan về công cụ
Công cụ tạo ULID được sử dụng để tạo các định danh duy nhất toàn cục ngẫu nhiên có thể sắp xếp theo thứ tự từ điển (ULID). Các định danh được tạo ra là duy nhất và có thể sắp xếp, thường được ứng dụng rộng rãi trong các hệ thống phân tán, định danh bản ghi cơ sở dữ liệu, và nhiều trường hợp khác.

## 2. Mô tả chức năng

### (1) Thiết lập số lượng
Thông qua tùy chọn "Quantity", bạn có thể thiết lập số lượng ULID cần tạo. Giá trị mặc định là 1, bạn có thể điều chỉnh số lượng bằng cách nhấn vào các nút cộng/trừ ở bên phải.

### (2) Chọn định dạng đầu ra
Hai định dạng đầu ra sau đây được hỗ trợ:
1. **Raw**: Hiển thị ULID dưới dạng văn bản thuần túy, thuận tiện cho việc xem và sử dụng trực tiếp.
2. **JSON**: Xuất các ULID đã tạo dưới dạng JSON, giúp dễ dàng gọi và phân tích bởi các chương trình.

### (3) Tạo và thao tác
Nhấn vào nút "Refresh" để tạo ULID mới; nhấn vào nút "Copy" để sao chép các ULID đã tạo vào clipboard, sau đó bạn có thể dán chúng vào bất kỳ đâu khi cần sử dụng.

## 3. Ví dụ

### Ví dụ 1: Tạo một ULID đơn lẻ (định dạng Raw)
Thiết lập "Quantity" thành 1 và chọn định dạng "Raw", sau đó nhấn "Refresh", một ULID tương tự như dưới đây sẽ được tạo ra:
```
01JTJFE7397K54Z6XD2ZQFHDD3
```

### Ví dụ 2: Tạo nhiều ULID (định dạng JSON)
Thiết lập "Quantity" thành 3 và chọn định dạng "JSON", sau đó nhấn "Refresh", các ULID sẽ được tạo theo định dạng JSON như sau:
```json
{
  "ulids": [
    "01JTJFE7397K54Z6XD2ZQFHDD3",
    "01JTJFE7397K54Z6XD2ZQFHDD4",
    "01JTJFE3797K54Z6XD2ZQFHDD5"
  ]
}