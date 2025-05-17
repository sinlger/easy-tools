# Tài liệu Hướng dẫn Công cụ Tạo địa chỉ IPv6 ULA

**1. Giới thiệu về Công cụ**

Công cụ tạo địa chỉ IPv6 ULA là một tiện ích trực tuyến được thiết kế để hỗ trợ người dùng tạo các địa chỉ IPv6 cục bộ không thể định tuyến trên Internet theo tiêu chuẩn RFC4193. Nó phù hợp để tạo các định danh mạng duy nhất trong phạm vi mạng nội bộ mà không bị trùng lặp hay xung đột với các địa chỉ công cộng.

**2. Các Tính năng Chính**

1. **Tạo địa chỉ ULA ngẫu nhiên dựa trên nhiều yếu tố**
   * Công cụ này sử dụng phương pháp đầu tiên do IETF khuyến nghị, kết hợp giữa thời gian hiện tại (timestamp) và địa chỉ MAC thông qua thuật toán băm SHA1, sau đó trích xuất 40 bit thấp hơn để tạo ra các địa chỉ ULA ngẫu nhiên. Điều này đảm bảo tính ngẫu nhiên cao và độ độc đáo của từng địa chỉ được sinh ra, giảm thiểu rủi ro xung đột địa chỉ và cung cấp các định danh mạng đáng tin cậy cho thiết bị trong môi trường mạng cục bộ.

2. **Nhập và xử lý địa chỉ MAC**
   * Người dùng có thể nhập thủ công địa chỉ MAC vào ô được chỉ định theo đúng định dạng tiêu chuẩn (ví dụ: "20:37:06:12:34:56"). Công cụ sẽ sử dụng địa chỉ MAC đã nhập như một tham số quan trọng trong quá trình tạo địa chỉ ULA, kết hợp cùng các yếu tố khác để cho ra đời một địa chỉ ULA gắn liền với địa chỉ MAC đó.

3. **Tạo địa chỉ ULA và các khối định tuyến tương ứng**

   * **IPv6 ULA**: Công cụ sẽ tạo ra một địa chỉ IPv6 ULA hoàn chỉnh bắt đầu bằng "fd", tuân thủ định dạng theo RFC4193 dành cho địa chỉ ULA cục bộ. Ví dụ: "fd1d:dba9:6f7b::/48", trong đó "/48" cho biết độ dài tiền tố của địa chỉ ULA là 48 bit, cung cấp định danh mạng duy nhất cho các thiết bị trong mạng nội bộ, có thể dùng để cấu hình hoặc truyền thông trong mạng cục bộ.
   * **Khối định tuyến đầu tiên**: Một khối địa chỉ có thể gán đầu tiên cũng được tạo ra, ví dụ như "fd1d:dba9:6f7b:0::/64", đại diện cho khối đầu tiên trong dải địa chỉ ULA có thể được phân bổ cho máy chủ (host) hoặc mạng con (subnet). Thông tin này giúp người dùng hiểu rõ phạm vi địa chỉ khả dụng ban đầu, từ đó dễ dàng lập kế hoạch mạng và quản lý địa chỉ hơn.
   * **Khối định tuyến cuối cùng**: Công cụ cũng tạo ra khối địa chỉ cuối cùng có thể gán, ví dụ "fd1d:dba9:6f7b:ffff::/64", đây là khối cuối cùng trong dải địa chỉ ULA có thể sử dụng. Nhờ vậy, người dùng nắm rõ giới hạn phân bố địa chỉ, thuận lợi cho việc triển khai mạng và cấu hình thiết bị.

**3. Các Trường hợp Sử dụng Thực tế**

1. Trong các mạng nội bộ doanh nghiệp, cấp phát địa chỉ IPv6 riêng biệt cho các thiết bị nhằm tránh xung đột với địa chỉ IPv6 công cộng đồng thời đảm bảo giao tiếp bình thường giữa các thiết bị trong mạng nội bộ.

2. Trong môi trường thử nghiệm mạng, tạo các địa chỉ ULA cục bộ không thể định tuyến được để mô phỏng các tình huống mạng, thực hiện kiểm tra cấu hình thiết bị mạng, kiểm thử ứng dụng mà không cần chiếm dụng tài nguyên địa chỉ IPv6 chính thức từ Internet.

3. Trong mạng gia đình, phân bổ địa chỉ ULA cho modem, router và các thiết bị thông minh, tăng cường sự ổn định và an toàn mạng, ngăn chặn truy cập trái phép từ bên ngoài mạng.

**4. Hướng Dẫn Sử dụng**

1. Truy cập trang web của công cụ tạo địa chỉ IPv6 ULA tại [https://atoolio.com/ipv6-ula-generator](https://atoolio.com/ipv6-ula-generator).
2. Nếu bạn đã biết địa chỉ MAC của thiết bị, hãy nhập nó theo đúng định dạng tiêu chuẩn (ví dụ: "20:37:06:12:34:56") vào ô "MAC address". Trường hợp chưa xác định được địa chỉ MAC, bạn có thể để trống ô này — công cụ có thể tự động sử dụng một địa chỉ MAC mặc định hoặc tạo địa chỉ MAC giả ngẫu nhiên (tùy thuộc vào logic hoạt động thực tế của công cụ).
3. Nhấn nút tạo (ví dụ: nút "Generate", tên nút có thể khác nhau tùy theo giao diện của công cụ), hệ thống sẽ tiến hành tính toán và sinh ra địa chỉ IPv6 ULA tương ứng, khối định tuyến đầu tiên và cuối cùng dựa trên địa chỉ MAC đã nhập (hoặc giá trị mặc định) và thời điểm hiện tại.
4. Kiểm tra thông tin các địa chỉ đã tạo và áp dụng chúng theo nhu cầu thực tế cho cấu hình thiết bị, quy hoạch mạng hoặc kiểm tra kết nối.

**5. Những Lưu ý Quan trọng**

1. Địa chỉ ULA đã tạo chỉ nên được sử dụng trong phạm vi mạng nội bộ, không thể định tuyến hay giao tiếp trực tiếp trên Internet. Đối với các thiết bị yêu cầu kết nối Internet, cần phải thiết lập địa chỉ IPv6 đơn hướng (unicast) có thể định tuyến toàn cầu.

2. Hãy chắc chắn rằng địa chỉ MAC được nhập chính xác. Bất kỳ sai sót nào cũng có thể ảnh hưởng đến tính duy nhất và liên kết của địa chỉ ULA đã tạo, gây ra các vấn đề tiềm ẩn trong quản lý cấu hình mạng.

3. Địa chỉ ULA cần luôn đảm bảo tính duy nhất trong phạm vi mạng cục bộ. Tuyệt đối tránh việc sử dụng lại cùng một địa chỉ ULA cho nhiều thiết bị, vì điều này có thể gây ra xung đột mạng và làm gián đoạn giao tiếp giữa các thiết bị.