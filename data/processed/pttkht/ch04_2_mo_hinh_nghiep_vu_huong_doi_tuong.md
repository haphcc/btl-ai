# Chương 4.2: Mô hình nghiệp vụ hướng đối tượng

## Nội dung chính
- Tổng quan về phát triển hệ thống hướng đối tượng.
- Khái niệm object, class, trạng thái, hành vi và định danh.
- Ngôn ngữ mô hình hóa thống nhất UML.
- Biểu đồ ca sử dụng và các thành phần.
- Biểu đồ tuần tự và cách mô tả tương tác.

## Tổng quan
Chương này giới thiệu cách phân tích nghiệp vụ theo hướng đối tượng. Phương pháp này ánh xạ các đối tượng trong thế giới thực vào mô hình hệ thống, kết hợp cả dữ liệu và hành vi trong cùng một đơn vị mô hình hóa.

## Tổng quan về hướng đối tượng

### Cách tư duy hướng đối tượng

**Khái niệm chính:**
- Hệ thống được chia thành các đối tượng tương đối độc lập.
- Mỗi đối tượng có dữ liệu và hành vi.
- Các đối tượng tương tác với nhau thông qua thông điệp.

**Giải thích:**
Khác với phương pháp hướng cấu trúc chỉ tập trung nhiều vào dữ liệu hoặc luồng xử lý, hướng đối tượng xem xét đồng thời dữ liệu và hành vi. Phần mềm được xây dựng bằng cách kết hợp các đối tượng thông qua quan hệ và tương tác.

### Đối tượng

**Khái niệm chính:**
- Đối tượng là khái niệm mô tả sự vật, hiện tượng trong thế giới thực.
- Một đối tượng chứa thành phần dữ liệu và các hành động có thể thực hiện trên dữ liệu đó.
- Đối tượng được xác định bởi trạng thái, hành vi và định danh.

**Quy trình / Mô hình / Ký hiệu:**
| Yếu tố | Ý nghĩa |
|---|---|
| Trạng thái | Tập hợp thuộc tính của đối tượng tại một thời điểm. |
| Hành vi | Chức năng hoặc cách thức hoạt động của đối tượng. |
| Định danh | Yếu tố thể hiện sự tồn tại duy nhất của đối tượng. |

### Lớp

**Khái niệm chính:**
- Lớp là mô tả của một nhóm đối tượng có chung thuộc tính, hành vi và quan hệ.
- Đối tượng là một thể hiện của lớp.
- Lớp là định nghĩa trừu tượng của đối tượng.

**Giải thích:**
Trong mô hình hướng đối tượng, trạng thái của đối tượng thường được cài đặt thành thuộc tính của lớp, còn hành vi được cài đặt thành phương thức của lớp.

## Ưu điểm của phương pháp hướng đối tượng

### Lợi ích

**Khái niệm chính:**
- Mô hình hóa trực quan các sự vật và quan hệ trong thế giới thực.
- Hỗ trợ sử dụng lại các thành phần đã xây dựng.
- Phù hợp với các hệ thống lớn và phức tạp.
- Dễ mở rộng khi nghiệp vụ thay đổi.

**Lưu ý:**
- Hướng đối tượng yêu cầu người phân tích nhận diện đúng đối tượng, thuộc tính, hành vi và quan hệ.

## UML

### Ngôn ngữ mô hình hóa thống nhất

**Khái niệm chính:**
- UML là viết tắt của `Unified Modeling Language`.
- UML là ngôn ngữ mô hình hóa dùng để mô tả, trực quan hóa và đặc tả hệ thống phần mềm.
- UML được hình thành từ các phương pháp Booch, OOSE và OMT, gắn với Grady Booch, Ivar Jacobson và Jim Rumbaugh.

**Giải thích:**
UML cung cấp tập ký hiệu chung để các bên liên quan hiểu mô hình hệ thống. UML không phải là ngôn ngữ lập trình mà là ngôn ngữ mô hình hóa.

## Biểu đồ ca sử dụng

### Use Case Diagram

**Khái niệm chính:**
- Biểu đồ ca sử dụng mô tả các chức năng hệ thống nhìn từ góc độ người dùng hoặc tác nhân ngoài.
- Thành phần cơ bản gồm actor, use case và quan hệ.

**Quy trình / Mô hình / Ký hiệu:**
| Thành phần | Ý nghĩa |
|---|---|
| Actor | Vai trò bên ngoài tương tác với hệ thống. |
| Use case | Chức năng hoặc dịch vụ hệ thống cung cấp cho actor. |
| Quan hệ | Liên kết giữa actor và use case hoặc giữa các use case. |

**Giải thích:**
Use case giúp xác định phạm vi chức năng của hệ thống. Mỗi use case biểu diễn một mục tiêu có ý nghĩa đối với actor.

## Biểu đồ tuần tự

### Sequence Diagram

**Khái niệm chính:**
- Biểu đồ tuần tự mô tả tương tác giữa các đối tượng theo thời gian.
- Thành phần thường gặp gồm đối tượng, lifeline và message.

**Quy trình / Mô hình / Ký hiệu:**
| Thành phần | Ý nghĩa |
|---|---|
| Object | Đối tượng tham gia tương tác. |
| Lifeline | Đường sống biểu diễn thời gian tồn tại của đối tượng trong tương tác. |
| Message | Thông điệp gửi từ đối tượng này đến đối tượng khác. |

**Lưu ý:**
- Biểu đồ tuần tự thường dùng để làm rõ luồng xử lý của một use case.

## Tóm tắt chương
- Hướng đối tượng mô hình hóa hệ thống bằng object và class.
- Object có trạng thái, hành vi và định danh.
- Class mô tả nhóm đối tượng có chung đặc điểm.
- UML là ngôn ngữ mô hình hóa thống nhất.
- Use case diagram mô tả chức năng, sequence diagram mô tả tương tác theo thời gian.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Object | Đối tượng mô tả sự vật, hiện tượng trong hệ thống. |
| Class | Lớp mô tả nhóm đối tượng có chung thuộc tính, hành vi và quan hệ. |
| State | Trạng thái của đối tượng tại một thời điểm. |
| Behavior | Hành vi hoặc chức năng của đối tượng. |
| Identity | Định danh duy nhất của đối tượng. |
| UML | Ngôn ngữ mô hình hóa thống nhất. |
| Use case | Chức năng hệ thống cung cấp cho actor. |
| Sequence diagram | Biểu đồ mô tả tương tác giữa các đối tượng theo thời gian. |

## Câu hỏi ôn tập
1. Phát triển hệ thống hướng đối tượng có đặc điểm gì?
2. Đối tượng được xác định bởi những yếu tố nào?
3. Lớp là gì? Đối tượng và lớp khác nhau như thế nào?
4. Nêu các ưu điểm của phương pháp hướng đối tượng.
5. UML là gì và dùng để làm gì?
6. Actor trong biểu đồ ca sử dụng là gì?
7. Use case biểu diễn điều gì?
8. Biểu đồ tuần tự dùng để mô tả nội dung gì?
