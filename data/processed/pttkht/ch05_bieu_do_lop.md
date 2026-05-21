# Chương 5: Biểu đồ lớp

## Nội dung chính
- Ý nghĩa của biểu đồ lớp trong phát triển phần mềm hướng đối tượng.
- Ký hiệu lớp gồm tên lớp, thuộc tính và phương thức.
- Phạm vi truy nhập public, private và protected.
- Các quan hệ trong biểu đồ lớp.
- Cách xây dựng biểu đồ lớp và ví dụ minh họa.

## Tổng quan
Biểu đồ lớp là một trong những biểu đồ quan trọng nhất trong phát triển phần mềm hướng đối tượng. Biểu đồ này dùng để mô hình hóa thuộc tính, hành vi và quan hệ giữa các lớp trong hệ thống.

## Ý nghĩa của biểu đồ lớp

### Vai trò

**Khái niệm chính:**
- Biểu đồ lớp có tính quyết định trong tiến trình phát triển phần mềm hướng đối tượng.
- Biểu đồ lớp mô hình hóa thuộc tính và hành vi của các đối tượng.
- Biểu đồ lớp giúp chuyển từ phân tích nghiệp vụ sang thiết kế phần mềm.

**Giải thích:**
Khi đã xác định được các đối tượng nghiệp vụ, biểu đồ lớp giúp tổ chức chúng thành các lớp, chỉ ra thuộc tính, phương thức và quan hệ giữa các lớp. Đây là cơ sở quan trọng cho thiết kế và cài đặt.

## Ký hiệu lớp

### Cấu trúc lớp

**Khái niệm chính:**
- Một lớp thường được biểu diễn bằng hình chữ nhật chia thành ba ngăn.
- Ba ngăn gồm tên lớp, thuộc tính và phương thức.

**Quy trình / Mô hình / Ký hiệu:**
| Ngăn | Nội dung |
|---|---|
| Class Name | Tên lớp. |
| Attribute | Các thuộc tính mô tả trạng thái của lớp. |
| Method | Các phương thức mô tả hành vi của lớp. |

### Phạm vi truy nhập

**Khái niệm chính:**
- `public`: thành phần có thể được truy cập từ bên ngoài lớp.
- `private`: thành phần chỉ được truy cập bên trong lớp.
- `protected`: thành phần được truy cập trong lớp và các lớp kế thừa.

**Quy trình / Mô hình / Ký hiệu:**
| Ký hiệu | Phạm vi | Ý nghĩa |
|---|---|---|
| `+` | public | Công khai. |
| `-` | private | Riêng tư. |
| `#` | protected | Bảo vệ. |

## Các quan hệ trong biểu đồ lớp

### Association

**Khái niệm chính:**
- Association là quan hệ liên kết giữa các lớp.
- Quan hệ có thể có tên liên kết và hướng liên kết.
- Cơ số thể hiện số lượng đối tượng tham gia quan hệ.

**Quy trình / Mô hình / Ký hiệu:**
| Cơ số | Ý nghĩa |
|---|---|
| `1` | Đúng một đối tượng. |
| `0..1` | Không có hoặc có một đối tượng. |
| `m..n` | Từ m đến n đối tượng. |
| `0..*` hoặc `*` | Không giới hạn, có thể không có đối tượng nào. |
| `1..*` | Ít nhất một đối tượng. |

### Aggregation và Composition

**Khái niệm chính:**
- Aggregation là quan hệ kết nhập, biểu diễn quan hệ toàn thể - bộ phận lỏng.
- Composition là quan hệ hợp thành chặt hơn, bộ phận phụ thuộc mạnh vào toàn thể.

**Giải thích:**
Trong aggregation, bộ phận có thể tồn tại độc lập với toàn thể. Trong composition, vòng đời của bộ phận thường gắn chặt với toàn thể.

### Generalization

**Khái niệm chính:**
- Generalization là quan hệ tổng quát hóa/kế thừa.
- Lớp con kế thừa đặc điểm của lớp cha và có thể bổ sung đặc điểm riêng.

### Dependency

**Khái niệm chính:**
- Dependency là quan hệ phụ thuộc.
- Một lớp sử dụng hoặc phụ thuộc vào thông tin/dịch vụ của lớp khác.

## Cách xây dựng biểu đồ lớp

### Các bước cơ bản

**Quy trình / Mô hình / Ký hiệu:**
1. Xác định các lớp ứng viên từ yêu cầu và mô hình nghiệp vụ.
2. Xác định thuộc tính của từng lớp.
3. Xác định phương thức hoặc hành vi chính.
4. Xác định quan hệ giữa các lớp.
5. Gán cơ số, tên quan hệ và hướng quan hệ nếu cần.
6. Rà soát lại mô hình để loại bỏ lớp dư thừa hoặc quan hệ không hợp lý.

**Lưu ý:**
- Biểu đồ lớp nên thể hiện đúng mô hình nghiệp vụ, không nên đưa quá sớm các chi tiết cài đặt không cần thiết.

## Tóm tắt chương
- Biểu đồ lớp mô hình hóa lớp, thuộc tính, phương thức và quan hệ.
- Lớp được biểu diễn bằng ba ngăn: tên lớp, thuộc tính và phương thức.
- Phạm vi truy nhập thường gồm public, private và protected.
- Các quan hệ chính gồm association, aggregation, composition, generalization và dependency.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Class diagram | Biểu đồ lớp mô tả lớp và quan hệ giữa các lớp. |
| Class | Lớp mô tả nhóm đối tượng có thuộc tính và hành vi chung. |
| Attribute | Thuộc tính mô tả trạng thái của lớp. |
| Method | Phương thức mô tả hành vi của lớp. |
| Association | Quan hệ liên kết giữa các lớp. |
| Multiplicity | Cơ số cho biết số lượng đối tượng tham gia quan hệ. |
| Generalization | Quan hệ tổng quát hóa hoặc kế thừa. |
| Dependency | Quan hệ phụ thuộc giữa các lớp. |

## Câu hỏi ôn tập
1. Biểu đồ lớp có ý nghĩa gì trong phát triển phần mềm hướng đối tượng?
2. Một ký hiệu lớp gồm những ngăn nào?
3. Phân biệt public, private và protected.
4. Association là gì?
5. Multiplicity dùng để biểu diễn điều gì?
6. Phân biệt aggregation và composition.
7. Generalization biểu diễn quan hệ gì?
8. Nêu các bước cơ bản để xây dựng biểu đồ lớp.
