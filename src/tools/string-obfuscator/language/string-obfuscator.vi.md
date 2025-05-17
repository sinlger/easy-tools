# Tài liệu hướng dẫn người dùng công cụ làm mờ chuỗi A Toolio

## 1. Tổng quan về công cụ

Công cụ làm mờ chuỗi (string obfuscator) của A Toolio là một công cụ trực tuyến đơn giản và tiện lợi được thiết kế nhằm mục đích che giấu các chuỗi dữ liệu nhạy cảm (như mật khẩu, IBAN hoặc token), giúp chúng vẫn có thể nhận biết được khi chia sẻ nhưng đồng thời bảo vệ tính riêng tư và tránh rò rỉ thông tin.

## 2. Mô tả chức năng

### (1) **Ô nhập liệu**

* **String to obfuscate**: Nhập chuỗi cần làm mờ tại đây. Chuỗi này có thể là bất kỳ loại văn bản nào, ví dụ như số tài khoản, mật khẩu, số chứng minh thư, số thẻ ngân hàng, v.v.

### (2) **Tùy chọn cấu hình**

* **Keep first**: Xác định số lượng ký tự cần giữ nguyên ở đầu chuỗi. Giá trị mặc định là 4; bạn có thể điều chỉnh giá trị này bằng cách sử dụng các nút "−" hoặc "+" theo nhu cầu cá nhân.
* **Keep last**: Chỉ định số ký tự cần giữ lại ở cuối chuỗi. Cũng giống như trên, giá trị ban đầu là 4 và có thể thay đổi bằng các nút "−" hoặc "+".
* **Keep spaces**: Quyết định xem có nên giữ lại khoảng trắng trong chuỗi hay không. Khi tùy chọn này được bật (mặc định), vị trí khoảng trắng sẽ được giữ nguyên trong chuỗi đã xử lý; nếu tắt đi, khoảng trắng sẽ bị bỏ qua.

### (3) **Ô hiển thị kết quả**

* Hiển thị kết quả sau khi chuỗi đã được làm mờ. Những ký tự không được giữ lại sẽ bị thay thế bằng dấu "*".

### (4) **Nút sao chép**

* Nằm bên phải ô hiển thị kết quả, nhấn vào nút này sẽ sao chép chuỗi đã được làm mờ vào clipboard, giúp bạn dễ dàng dán vào nơi cần sử dụng sau này.

## 3. Các bước thực hiện

1. Truy cập trang web [A Toolio String Obfuscator](https://atoolio.com/string-obfuscator).
2. Tại ô **String to obfuscate**, nhập chuỗi văn bản mà bạn muốn làm mờ.
3. Điều chỉnh các giá trị **Keep first** và **Keep last** theo ý thích và xác định xem tùy chọn **Keep spaces** có nên được kích hoạt hay không.
4. Kiểm tra kết quả hiển thị trong ô xuất ra.
5. Nếu cần sử dụng kết quả đã xử lý, hãy nhấn vào nút sao chép bên phải để lưu chuỗi vào clipboard.