# Chương 5: Cơ chế đa hình

## Nội dung chính
- Hàm ảo trong C++.
- Hàm thuần ảo.
- Lớp trừu tượng.
- Các thành viên ảo của một lớp.
- Ứng dụng đa hình trong bài toán tính chi phí phương tiện và gửi thông báo.

## Tổng quan
Đa hình cho phép cùng một lời gọi phương thức có thể dẫn đến các cách xử lý khác nhau tùy theo đối tượng thực tế. Trong C++, đa hình động thường được thực hiện thông qua hàm ảo, hàm thuần ảo và lớp trừu tượng.

## 5.1. Hàm ảo

Hàm ảo (virtual function) cho phép chương trình chọn đúng hàm của đối tượng thực sự đang dùng, thay vì chỉ dựa trên kiểu khai báo.

Trong C++, nếu có lớp cha và lớp con, lớp con có thể viết lại hàm của lớp cha. Nếu gọi hàm qua con trỏ hoặc tham chiếu của lớp cha, C++ mặc định có thể gọi hàm của lớp cha. Để C++ gọi đúng hàm của lớp con, cần dùng hàm ảo.

```cpp
class PhuongTien {
public:
    virtual double tinhChiPhi(double quangDuong) {
        return 0;
    }
};

class XeMay : public PhuongTien {
public:
    double tinhChiPhi(double quangDuong) override {
        return quangDuong * 8000;
    }
};

class XeOto : public PhuongTien {
public:
    double tinhChiPhi(double quangDuong) override {
        return quangDuong * 12000;
    }
};
```

**Ví dụ:** Slide nêu bài toán tính tiền trong đặt xe Grab với các loại phương tiện như xe máy và xe ô tô. Mỗi loại phương tiện có cách tính chi phí riêng, nhưng chương trình có thể gọi chung hàm tính chi phí.

## 5.2. Hàm thuần ảo

Hàm thuần ảo là hàm ảo đặc biệt: không có phần thân trong lớp cha mà chỉ có khai báo. Lớp cha chỉ đưa ra khuôn mẫu, bắt buộc lớp con phải viết lại.

Cú pháp:

```cpp
virtual void tenHam() = 0;
```

Dấu `= 0` cho biết đây là hàm thuần ảo.

Đặc điểm:

- Lớp chứa hàm thuần ảo gọi là lớp trừu tượng.
- Không thể tạo đối tượng trực tiếp từ lớp trừu tượng.
- Chỉ có thể tạo đối tượng từ lớp con, vì lớp con phải định nghĩa lại hàm thuần ảo.

## 5.3. Lớp trừu tượng

Lớp trừu tượng là lớp:

- Có ít nhất một hàm thuần ảo.
- Dùng làm khuôn mẫu cho các lớp con.
- Không thể tạo đối tượng trực tiếp.

Mục đích của lớp trừu tượng là ép các lớp con phải viết lại các hàm mà lớp cha quy định. Có thể hiểu rằng lớp con kế thừa thì phải thực hiện các điều khoản do lớp cha đưa ra.

### Khi nào dùng lớp trừu tượng?
Nên dùng lớp trừu tượng khi:

- Muốn các lớp con có hành vi chung nhưng mỗi lớp con thực hiện theo cách riêng.
- Muốn ép buộc các lớp con phải cài đặt một số chức năng nhất định.
- Cần đa hình: cùng một lệnh gọi nhưng hành vi khác nhau.

**Ví dụ:** Trong một trường đại học:

| Đối tượng | Hoạt động |
|---|---|
| Giảng viên | Giảng dạy |
| Sinh viên | Học tập |
| Cán bộ | Làm việc hành chính |

Các đối tượng này có thể cùng thuộc một nhóm tổng quát, nhưng mỗi nhóm có hành động cụ thể khác nhau.

## 5.4. Các thành viên ảo của một lớp

Trong C++, thành viên ảo thường gồm:

- Hàm ảo (virtual function).
- Hàm hủy ảo (virtual destructor).

Hàm ảo cho phép đa hình động, tức chương trình chọn hàm phù hợp trong lúc chạy thay vì lúc biên dịch.

Các thành viên sau không thể là ảo:

- Biến.
- Hàm tĩnh.
- Constructor.

### Cách hoạt động
- Khi một lớp có hàm ảo và lớp con ghi đè hàm đó, chương trình sẽ gọi hàm của lớp con nếu đối tượng thực tế là lớp con.
- Nếu không phải hàm ảo, chương trình gọi theo kiểu con trỏ hoặc tham chiếu.
- Khi xóa đối tượng bằng con trỏ lớp cha, hàm hủy nên là ảo để đối tượng lớp con được giải phóng đúng cách và tránh lỗi bộ nhớ.

```cpp
class Base {
public:
    virtual ~Base() {}
};
```

## Ví dụ ứng dụng: Gửi thông báo

Ứng dụng gửi thông báo có nhiều kênh như Email, SMS và Push Notification. Chương trình muốn gọi chung `guiThongBao()` cho mọi kênh, nhưng từng kênh có cách gửi khác nhau.

```cpp
class KenhThongBao {
public:
    virtual void guiThongBao() = 0;
};

class Email : public KenhThongBao {
public:
    void guiThongBao() override {
        // Gửi qua Email
    }
};

class SMS : public KenhThongBao {
public:
    void guiThongBao() override {
        // Gửi qua SMS
    }
};
```

## Bài tập cuối chương

Ứng dụng Grab cung cấp nhiều loại phương tiện:

| Phương tiện | Mô tả | Phí |
|---|---|---|
| GrabBike | Dành cho 1 khách, giá rẻ, di chuyển nhanh | 8.000 VNĐ/km |
| GrabCar | Dành cho tối đa 4 khách, tiện nghi hơn | 12.000 VNĐ/km |
| GrabCarPlus | Dành cho tối đa 7 khách, xe rộng rãi, phù hợp gia đình hoặc nhóm đông | 15.000 VNĐ/km |

Yêu cầu:

- Xây dựng lớp trừu tượng `PhuongTien` với các hàm thuần ảo:
  - `Hien_thi_thong_tin()`: hiển thị thông tin phương tiện.
  - `Tinhchiphi(double quangduong)`: tính chi phí chuyến đi.
- Xây dựng các lớp kế thừa:
  - `GrabBike`.
  - `GrabCar`.
  - `GrabCarPlus`.
- Viết chương trình chính:
  - Người dùng nhập số khách và quãng đường.
  - Hệ thống duyệt qua danh sách phương tiện để tìm phương tiện phù hợp.
  - In ra thông tin phương tiện gợi ý và chi phí dự kiến.

## Tóm tắt chương
- Hàm ảo giúp C++ gọi đúng phương thức theo đối tượng thực tế khi chạy chương trình.
- Hàm thuần ảo chỉ khai báo, không có phần thân và bắt buộc lớp con phải cài đặt.
- Lớp có ít nhất một hàm thuần ảo là lớp trừu tượng.
- Hàm hủy nên là ảo khi xóa đối tượng thông qua con trỏ lớp cha.
- Đa hình giúp gọi cùng một giao diện nhưng nhận hành vi khác nhau ở từng lớp con.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Polymorphism | Đa hình, cùng lời gọi nhưng hành vi phụ thuộc đối tượng thực tế |
| Virtual function | Hàm ảo, hỗ trợ gọi hàm theo kiểu động |
| Pure virtual function | Hàm thuần ảo, khai báo dạng `= 0` |
| Abstract class | Lớp trừu tượng, không tạo đối tượng trực tiếp |
| Override | Ghi đè phương thức ở lớp con |
| Virtual destructor | Hàm hủy ảo, giúp hủy đúng đối tượng qua con trỏ lớp cha |
| Dynamic binding | Kết gán muộn, chọn hàm lúc chạy |

## Câu hỏi ôn tập
1. Hàm ảo dùng để giải quyết vấn đề gì?
2. Vì sao gọi hàm qua con trỏ lớp cha có thể cần `virtual`?
3. Hàm thuần ảo có cú pháp như thế nào?
4. Lớp trừu tượng là gì?
5. Khi nào nên dùng lớp trừu tượng?
6. Những thành viên nào của lớp có thể là ảo?
7. Vì sao hàm hủy nên là ảo trong quan hệ kế thừa?
8. Bài toán Grab trong chương sử dụng đa hình như thế nào?
