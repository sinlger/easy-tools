# Tài liệu Hướng dẫn Sử dụng Công cụ Chuyển đổi từ Docker Run sang Docker-Compose

## 1. Tổng Quan về Công cụ

Công cụ Chuyển đổi từ Docker Run sang Docker-Compose là một tiện ích trực tuyến tiện lợi giúp các nhà phát triển chuyển đổi các lệnh dòng lệnh "docker run" thành các tệp tin Docker-Compose một cách nhanh chóng. Điều này giúp đơn giản hóa quá trình cấu hình cho việc quản lý container và nâng cao hiệu suất phát triển phần mềm.

## 2. Các Chức Năng Chính

1. **Chuyển Đổi Lệnh**
   * Người dùng có thể dán vào ô nhập liệu chuyên dụng những lệnh Docker phức tạp, ví dụ như: "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx".
   * Công cụ sẽ tự động phân tích toàn bộ các tham số trong lệnh "docker run", bao gồm ánh xạ cổng ("-p 80:80"), gắn kết volume ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), chính sách khởi động lại ("--restart always"), tùy chọn ghi log ("--log-opt max-size=1g") và tên image ("nginx").

2. **Tạo Tệp Tin Docker-Compose**
   * Dựa trên các tham số đã được trích xuất từ lệnh "docker run", công cụ sẽ tạo ra nội dung tương ứng cho tệp tin Docker-Compose.
   * Tệp tin YAML được sinh ra sẽ bao gồm khai báo phiên bản (ví dụ "version: '3.9'"), định nghĩa dịch vụ ("services"), chỉ định image ("image"), cấu hình ghi log ("logging" cùng với "options"), thiết lập khởi động lại ("restart"), ánh xạ thư mục ("volumes") và ánh xạ cổng ("ports"). Như vậy, toàn bộ thông tin liên quan đến việc điều phối container sẽ được trình bày đầy đủ, giúp người dùng có thể sử dụng trực tiếp hoặc chỉnh sửa theo nhu cầu cụ thể.

3. **Tải Về Tệp Tin**
   * Một nút bấm có nhãn "Download docker-compose.yml" cho phép người dùng tải về tệp tin Docker-Compose đã được tạo chỉ với một cú nhấp chuột duy nhất, từ đó dễ dàng áp dụng trong môi trường dự án thực tế.