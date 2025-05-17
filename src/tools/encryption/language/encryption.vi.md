# Tài liệu Hướng dẫn Sử dụng Công cụ Mã hóa/Giải mã Trực tuyến của A Toolio

## Tổng Quan về Chức Năng

Công cụ trực tuyến mã hóa và giải mã của A Toolio cho phép mã hóa và giải mã văn bản bằng nhiều thuật toán khác nhau (như AES, TripleDES, Rabbit hoặc RC4). Người dùng có thể dễ dàng mã hóa văn bản thường hoặc giải mã văn bản đã được mã hóa để đáp ứng nhu cầu sử dụng hàng ngày trong học tập hay phát triển phần mềm.

## Chức năng Mã hóa

1. **Nhập Văn bản Thường** - Trong phần "Encrypt" (Mã hóa), hãy nhập văn bản bạn muốn mã hóa vào ô "Your text" (Văn bản của bạn), ví dụ: "Lorem ipsum dolor sit amet".
2. **Thiết lập Khóa Bí mật** - Tại ô "Your secret key" (Khóa bí mật của bạn), hãy thiết lập một khóa sẽ được sử dụng để mã hóa, như "my secret key". Khóa là một thông số quan trọng trong quá trình mã hóa và cần được lưu trữ cẩn thận.
3. **Chọn Thuật toán Mã hóa** - Thông qua menu xổ xuống "Encryption algorithm" (Thuật toán mã hóa), hãy chọn thuật toán phù hợp như AES, TripleDES, Rabbit hoặc RC4. Các thuật toán khác nhau có những đặc điểm riêng về tính bảo mật và hiệu suất, vì vậy bạn có thể lựa chọn dựa trên nhu cầu thực tế của mình.
4. **Xem Kết quả Mã hóa** - Sau khi hoàn tất các bước trên, công cụ sẽ tự động hiển thị văn bản đã được mã hóa tại khu vực "Your text encrypted" (Văn bản đã mã hóa), ví dụ: "U2FsdGVkX19wCAAvFjYehC+Haqkp3/xRGF4yN17gt6/FgnlHRvikeCuOvDyAIBvG".

## Chức năng Giải mã

1. **Nhập Văn bản Đã Mã hóa** - Trong phần "Decrypt" (Giải mã), hãy nhập văn bản đã được mã hóa mà bạn muốn giải mã vào ô "Your encrypted text" (Văn bản đã mã hóa của bạn), ví dụ: "U2FsdGVkX1/EC3+6P5dbbkZ3e1kQ5o2yzuU0NHTjmrKnLBEwreV489Kr0DIB+uBs".
2. **Nhập Khóa Bí mật** - Nhập chính xác khóa đã sử dụng trước đó ở chức năng mã hóa vào ô "Your secret key" (Khóa bí mật của bạn), ví dụ: "my secret key". Việc nhập đúng khóa là rất quan trọng để giải mã thành công.
3. **Chọn Thuật toán Mã hóa** - Trong menu xổ xuống "Encryption algorithm" (Thuật toán mã hóa), hãy chọn lại thuật toán đã sử dụng lúc mã hóa, ví dụ: AES.
4. **Xem Kết quả Giải mã** - Công cụ sẽ hiển thị văn bản sau khi giải mã tại mục "Your decrypted text" (Văn bản đã giải mã), ví dụ: "Lorem ipsum dolor sit amet".

## Những Lưu ý Khác

* **An toàn Thông tin** - Mặc dù công cụ này tiện lợi và nhanh chóng, chúng tôi khuyến nghị bạn nên sử dụng nó trong môi trường mạng an toàn khi xử lý các thông tin nhạy cảm. Đồng thời hãy đảm bảo khóa bí mật không bị rò rỉ ra bên ngoài.
* **Lựa chọn Thuật toán** - Mỗi loại thuật toán mã hóa thích hợp với từng tình huống cụ thể. AES hiện đang là một trong những thuật toán phổ biến nhất và an toàn nhất; TripleDES tương đối cũ nhưng vẫn còn được áp dụng trong một vài hệ thống; Rabbit và RC4 cũng có những ưu điểm riêng biệt và phạm vi ứng dụng riêng. Bạn có thể lựa chọn thuật toán phù hợp dựa trên nhu cầu thực tế và mức độ an toàn yêu cầu.