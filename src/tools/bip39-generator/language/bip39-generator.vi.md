# A Toolio - Trình tạo Câu Khóa BIP39 Tài liệu

## 1. Mô tả công cụ

Trình tạo câu khóa BIP39 là một công cụ trực tuyến có thể tạo ra các cụm từ khóa BIP39 từ các từ gợi nhớ (mnemonics) hiện có hoặc ngẫu nhiên, đồng thời hỗ trợ trích xuất các từ gợi nhớ từ các cụm từ khóa. Công cụ này cung cấp cho các nhà phát triển các thao tác liên quan đến mật khẩu một cách thuận tiện, phù hợp với nhiều tình huống ứng dụng khác nhau.

## 2. Các mô-đun chức năng và hướng dẫn sử dụng

### 1. **Lựa chọn ngôn ngữ**
   * **Chức năng**: Người dùng có thể lựa chọn các tùy chọn ngôn ngữ khác nhau trong menu xổ xuống theo nhu cầu. Hiện tại hỗ trợ "Chinese simplified", v.v., để thiết lập loại ngôn ngữ cho từ gợi nhớ.
   * **Các bước thực hiện**: Nhấp vào ô lựa chọn ngôn ngữ và chọn ngôn ngữ mong muốn cho từ gợi nhớ trong danh sách xổ xuống hiển thị, ví dụ như tiếng Trung (phiên bản giản thể), v.v.

### 2. **Tạo cụm từ gợi nhớ**
   * **Chức năng**: Dựa trên chuỗi entropy do người dùng nhập vào hoặc được tạo ngẫu nhiên, công cụ sẽ tạo ra cụm từ gợi nhớ BIP39 tương ứng theo ngôn ngữ đã chọn, cung cấp cho người dùng một phương pháp dễ nhớ để lưu trữ và sử dụng sau này.
   * **Các bước thực hiện**:
     1. Nhập chuỗi entropy mong muốn vào ô văn bản "Entropy (seed):". Nếu bạn không muốn nhập thủ công, hãy nhấp vào biểu tượng "ngẫu nhiên" bên cạnh ô này để tạo entropy ngẫu nhiên.
     2. Chọn ngôn ngữ cho từ gợi nhớ (đã được mô tả ở mô-đun lựa chọn ngôn ngữ) và nhấn nút "Tạo". Ô văn bản "Passphrase (mnemonic):" phía dưới sẽ tự động tạo ra cụm từ gợi nhớ tương ứng.