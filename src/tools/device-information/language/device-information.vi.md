# Giới thiệu về chức năng Thông tin Thiết bị Trực tuyến

## Tổng Quan

Công cụ thông tin thiết bị trực tuyến thu thập thông tin chi tiết về thiết bị hiện tại, bao gồm dữ liệu màn hình và thiết bị, nhằm mục đích giúp các nhà phát triển hiểu rõ đặc điểm của thiết bị và hỗ trợ thiết kế cũng như gỡ lỗi bố cục trang web.

## Thông Tin Màn Hình

1. **Kích thước màn hình** - Hiển thị chiều rộng và chiều cao màn hình tính theo pixel, ví dụ 2560x1392 pixel. Thông tin này được sử dụng làm tài liệu tham khảo để thiết kế bố cục trang web và đảm bảo rằng các phần tử trên trang được hiển thị một cách hợp lý trên các kích thước màn hình khác nhau.
2. **Hướng màn hình** - Chỉ ra màn hình đang ở chế độ "landscape-primary" (ngang - hướng chính) hay "portrait-primary" (dọc - hướng chính). Điều này giúp tối ưu hóa việc hiển thị cho các hướng thiết bị khác nhau.
3. **Góc xoay màn hình** - Cho biết góc xoay của màn hình so với vị trí thẳng đứng. Giá trị 0° có nghĩa là màn hình không xoay, có thể được sử dụng làm tài liệu tham khảo khi thiết kế bố cục phản hồi (responsive).
4. **Độ sâu màu** - Hiển thị số lượng màu sắc mà màn hình có thể hiển thị, ví dụ màu 24-bit. Độ sâu màu càng lớn, màn hình có thể hiển thị càng nhiều màu sắc, ảnh hưởng trực tiếp đến chất lượng hình ảnh và video.
5. **Tỷ lệ pixel** - Phản ánh tỷ lệ giữa pixel vật lý và pixel CSS của thiết bị. Giá trị 1 dppx đại diện cho mối quan hệ 1:1 giữa hai loại pixel này, rất quan trọng để hiển thị hình ảnh chất lượng cao và độ chính xác trong quá trình render trang.
6. **Kích thước cửa sổ** - Hiển thị chiều rộng và chiều cao hiện tại của cửa sổ trình duyệt, ví dụ 1865x1316 pixel. Những dữ liệu này cung cấp thông tin hữu ích để thiết kế giao diện web thích ứng.