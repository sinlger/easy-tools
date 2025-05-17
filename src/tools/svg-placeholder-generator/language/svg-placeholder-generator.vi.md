# Tài liệu hướng dẫn người dùng công cụ tạo mã giữ chỗ SVG

## 1. Tổng quan về công cụ

Công cụ tạo mã giữ chỗ SVG là một công cụ trực tuyến tiện lợi, cho phép nhanh chóng tạo ra các hình ảnh SVG có thể tùy chỉnh để làm hình ảnh tạm thời. Những mã giữ chỗ này có thể được sử dụng trong quá trình phát triển ứng dụng nhằm hiển thị hình ảnh sơ bộ, hỗ trợ các nhà phát triển trong việc xây dựng bố cục giao diện và xem trước thiết kế trước khi có nội dung hình ảnh thực tế.

## 2. Mô tả chức năng

### (1) **Thiết lập kích thước**

* **Chiều rộng và chiều cao**: Bạn có thể thiết lập chiều rộng và chiều cao của mã giữ chỗ (theo đơn vị pixel) thông qua các ô nhập liệu. Ngoài ra còn có các nút "+" và "-" để điều chỉnh kích thước nhanh chóng.
* **Sử dụng kích thước chính xác**: Khi bật tùy chọn này, mã giữ chỗ SVG được tạo sẽ tuân thủ chặt chẽ theo chiều rộng và chiều cao đã chỉ định.

### (2) **Tùy chỉnh màu sắc**

* **Màu nền**: Nhập mã màu thập lục phân (ví dụ: "#cccccc") để tùy biến màu nền của mã giữ chỗ.
* **Màu chữ**: Tương tự, bạn cũng nhập mã màu thập lục phân (ví dụ: "#333333") để đặt màu của văn bản hiển thị trên mã giữ chỗ.

### (3) **Thiết lập văn bản**

* **Cỡ chữ**: Nhập giá trị số và chọn đơn vị phù hợp (ví dụ như pixel) để thay đổi cỡ chữ của văn bản hiển thị trên mã giữ chỗ.
* **Văn bản tùy chỉnh**: Nhập nội dung bạn muốn hiển thị vào ô văn bản; mặc định, nó sẽ hiển thị ở dạng "chiều rộng x chiều cao" (ví dụ: "600x350").

### (4) **Xem trước và đầu ra**

* **Xem trước trực tiếp**: Trong khu vực xem trước ở bên phải, bạn có thể theo dõi hiệu ứng của mã giữ chỗ SVG được tạo ra theo thời gian thực dựa trên các thông số đã thiết lập.
* **Phần tử HTML SVG**: Hiển thị đoạn mã SVG đã được tạo, có thể sao chép trực tiếp và sử dụng trong phát triển web.
* **SVG dưới dạng Base64**: Cung cấp chuỗi mã hóa Base64 của hình ảnh SVG, hữu ích trong những trường hợp cần định dạng đặc biệt này.

## 3. Các bước sử dụng chi tiết

1. Truy cập trang web của [công cụ tạo mã giữ chỗ SVG](https://atoolio.com/svg-placeholder-generator).
2. Thiết lập chiều rộng và chiều cao mong muốn cho mã giữ chỗ. Ví dụ, nếu bạn muốn tạo một mã giữ chỗ với chiều rộng 800 pixel và chiều cao 450 pixel, hãy nhập "800" vào ô "Width (in px)" và "450" vào ô "Height (in px)".
3. Tùy chỉnh màu nền và màu chữ. Nếu bạn muốn nền là màu xanh nhạt (ví dụ "#e6f7ff") và chữ là màu xanh đậm (ví dụ "#1890ff"), hãy nhập các mã màu tương ứng vào các ô thích hợp.
4. Thiết lập cỡ chữ và nội dung chữ tùy chỉnh. Giả sử bạn muốn cỡ chữ là 20 pixel và nội dung hiển thị là "Sample", hãy nhập "20" vào ô "Font size" và "Sample" vào ô "Custom text".
5. Kiểm tra vùng xem trước ở phía bên phải để xác nhận rằng hình ảnh mã giữ chỗ hiển thị đúng như kỳ vọng.
6. Dựa vào nhu cầu thực tế, bạn có thể chọn cách sao chép đoạn mã từ "SVG HTML element" hoặc chuỗi mã hóa Base64 sau đó dán vào dự án đang phát triển tương ứng. Ngoài ra, bạn cũng có thể nhấn vào nút "Download svg" để tải trực tiếp tệp SVG đã tạo.