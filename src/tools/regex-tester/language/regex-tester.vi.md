# Tài liệu hướng dẫn người dùng Regex Tester của A Toolio

## 1. Giới thiệu công cụ

**Regex Tester của A Toolio** là một công cụ trực tuyến cho phép kiểm tra các biểu thức chính quy bằng cách nhập văn bản mẫu. Với giao diện đơn giản và chức năng thực tế, nó phù hợp với cả người mới bắt đầu và các nhà phát triển.

## 2. Mô tả chi tiết chức năng

### (1) Khu vực nhập biểu thức chính quy

Nhập vào ô văn bản biểu thức chính quy mà bạn muốn kiểm tra. Một liên kết đến bảng tham chiếu nhanh cho các biểu thức chính quy cũng được cung cấp để hỗ trợ bạn trong quá trình sử dụng. Ví dụ: biểu thức chính quy \w+ có thể được sử dụng để tìm một hoặc nhiều từ.

### (2) Các tùy chọn của Regex Tester

Các tùy chọn bao gồm: Tìm kiếm toàn cục (g), Bỏ qua chữ hoa/chữ thường (i), Chế độ nhiều dòng (m), Chế độ một dòng (s), Hỗ trợ Unicode (u) và Hỗ trợ tập hợp Unicode (v). Hãy chọn các tùy chọn phù hợp với nhu cầu sử dụng của bạn.

- Tìm kiếm toàn cục (g): Tìm tất cả các kết quả khớp trong toàn bộ văn bản.
- Bỏ qua chữ hoa/chữ thường (i): Tìm kết quả không phân biệt chữ hoa và chữ thường.
- Chế độ nhiều dòng (m): Xử lý dữ liệu đầu vào như một văn bản nhiều dòng, cho phép tìm kiếm ở đầu và cuối mỗi dòng.
- Chế độ một dòng (s): Coi toàn bộ văn bản như một dòng duy nhất, giúp việc tìm kiếm vượt qua nhiều dòng dễ dàng hơn.
- Hỗ trợ Unicode (u): Bật hỗ trợ cho các ký tự Unicode.
- Hỗ trợ tập hợp Unicode (v): Hỗ trợ các tập hợp ký tự Unicode nâng cao.

Ví dụ: Biểu thức chính quy \d{3}-\d{3}-\d{4} có thể tìm thấy nhiều số điện thoại trong cùng một văn bản khi chế độ tìm kiếm toàn cục được kích hoạt.

### (3) Khu vực nhập văn bản cần phân tích

Nhập nội dung mà bạn muốn tìm kiếm vào ô văn bản. Công cụ sẽ tìm kiếm dựa trên biểu thức chính quy đã nhập và các tùy chọn đã chọn. Ví dụ: sử dụng biểu thức chính quy \w+ trong văn bản "Tìm các từ trong đoạn này", bạn có thể dễ dàng tìm thấy từng từ riêng biệt.