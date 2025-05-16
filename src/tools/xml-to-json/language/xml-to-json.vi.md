# Công Cụ Chuyển Đổi XML Sang JSON

## 1. Giới Thiệu
Đây là công cụ trực tuyến chuyển đổi dữ liệu định dạng XML sang định dạng JSON. Nó nâng cao hiệu suất phát triển và phù hợp với các tình huống cần chuyển đổi giữa các định dạng dữ liệu XML và JSON.

## 2. Các Chức Năng Chính

### (1) Nhập Nội Dung XML
Dán hoặc viết dữ liệu XML bạn muốn chuyển đổi vào khu vực nhập liệu. Ví dụ, bạn có thể nhập nội dung XML sau:
```
<a x="1.234" y="It's"/>
```

### (2) Xuất Dữ Liệu JSON
Sau khi nhấn nút chuyển đổi, công cụ sẽ hiển thị dữ liệu JSON tương ứng trong khu vực đầu ra. Ví dụ, XML ở trên sẽ được chuyển thành dữ liệu JSON như sau:
```json
{
  "a": {
    "_thuộc tính": {
      "x": "1.234",
      "y": "It's"
    }
  }
}
```

### (3) Chức Năng Sao Chép
Trong khu vực xuất dữ liệu JSON, bạn có thể nhấn nút sao chép để chép dữ liệu JSON đã tạo vào bộ nhớ đệm, giúp dễ dàng dán và sử dụng ở nơi khác.