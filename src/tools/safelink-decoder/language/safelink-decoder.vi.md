# Tài liệu hướng dẫn người dùng công cụ giải mã Outlook Safelink

## 1. Giới thiệu về công cụ
**Công cụ giải mã Outlook Safelink** là một phần mềm được thiết kế để giải mã các đường link do dịch vụ email Microsoft Outlook tạo ra dưới tên gọi SafeLink. Công cụ này cho phép chuyển đổi các đường link đã được Outlook SafeLink mã hóa trở lại thành URL gốc, giúp người dùng dễ dàng xác định đích thực sự của những đường link này.

## 2. Mô tả chức năng
Chức năng chính của công cụ này là giải mã các đường link Outlook Safelink, tức là chuyển đổi các đường link đã được Microsoft Outlook mã hóa và chuyển hướng trở lại thành địa chỉ web ban đầu.

## 3. Hướng dẫn sử dụng

### Đầu vào
Dán đường link Outlook Safelink mà bạn muốn giải mã vào ô nhập liệu. Đường link này đã được Microsoft Outlook mã hóa vì lý do bảo mật và có một định dạng cụ thể.

### Đầu ra
Sau khi nhấn nút "Decode", công cụ sẽ xử lý đường link đã nhập và hiển thị URL gốc sau khi giải mã trong ô đầu ra. Nếu đường link không đúng định dạng hoặc không thể nhận diện được, hệ thống sẽ hiển thị thông báo lỗi: "Error: Invalid SafeLinks URL provided".

## 4. Ví dụ minh họa

### Ví dụ 1
Đầu vào (đường link Safelink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fexample.com&data=...`
Kết quả sau khi giải mã:
`https://example.com`

### Ví dụ 2
Đầu vào (đường link Safelink):
`https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fmicrosoft.com&data=...`
Kết quả sau khi giải mã:
`https://microsoft.com`

### Ví dụ 3
Nhập đường link không hợp lệ hoặc sai định dạng:
`https://nam02.safelinks.protection.outlook.com/?url=invalidurl&data=...`
Thông báo lỗi:
`Error: Invalid SafeLinks URL provided`

## 5. Lưu ý quan trọng
- Đảm bảo rằng đường link bạn nhập vào là một đường link Outlook Safelink đầy đủ.