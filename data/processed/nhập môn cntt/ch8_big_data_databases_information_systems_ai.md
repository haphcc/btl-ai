# Chapter 8: The Era of Big Data: Databases, Information Systems, & Artificial Intelligence

## Nội dung chính
- File, database và cách quản lý file.
- Hệ quản trị cơ sở dữ liệu (Database Management System - DBMS).
- Các mô hình cơ sở dữ liệu (Database Models).
- Data mining và Big Data.
- Hệ thống thông tin (Information Systems) trong tổ chức.
- Trí tuệ nhân tạo (Artificial Intelligence - AI).
- Artificial life, Turing Test và Singularity.

## Tổng quan
Chương này giới thiệu cách dữ liệu được tổ chức, quản lý và khai thác trong thời đại dữ liệu lớn. Người học tìm hiểu từ file và database đến DBMS, data mining, Big Data, các hệ thống thông tin trong tổ chức và những ý tưởng nền tảng của trí tuệ nhân tạo.

## Unit 8A: Files & Databases

### 8.1 Managing Files

**Khái niệm chính:**
- File là tập hợp dữ liệu được lưu trữ dưới một tên.
- Dữ liệu có thể được tổ chức thành field, record và file.
- Quản lý file hiệu quả giúp tìm kiếm, cập nhật và bảo vệ dữ liệu.

**Giải thích:**
Trong quản lý dữ liệu, field là đơn vị dữ liệu chứa một hoặc nhiều ký tự, record là tập hợp các field mô tả một đối tượng, file là tập hợp các record liên quan. Khi dữ liệu tăng lên, chỉ dùng file rời rạc có thể gây trùng lặp, khó tìm kiếm và khó kiểm soát.

| Cấp dữ liệu | Giải thích |
|---|---|
| `Field` | Trường dữ liệu, ví dụ họ tên hoặc số điện thoại |
| `Record` | Bản ghi gồm nhiều field về một đối tượng |
| `File` | Tập hợp các record liên quan |
| `Database` | Tập dữ liệu có tổ chức và liên hệ với nhau |

**Thuật ngữ cần nhớ:**
- `Field`: trường dữ liệu.
- `Record`: bản ghi.
- `File`: file dữ liệu.
- `Database`: cơ sở dữ liệu.

**Ví dụ / ứng dụng:**
- Một record sinh viên gồm mã sinh viên, họ tên, lớp, email.

### 8.2 Database Management Systems

**Khái niệm chính:**
- DBMS là phần mềm dùng để tạo, lưu trữ, tổ chức, truy vấn và quản lý database.
- DBMS giúp giảm trùng lặp, tăng tính nhất quán và kiểm soát quyền truy cập.

**Giải thích:**
Khi dữ liệu được dùng bởi nhiều người hoặc nhiều ứng dụng, DBMS cung cấp cách quản lý tập trung. Người dùng có thể thêm, sửa, xóa, tìm kiếm và tạo báo cáo. DBMS cũng hỗ trợ bảo mật và sao lưu.

**Thuật ngữ cần nhớ:**
- `DBMS`: hệ quản trị cơ sở dữ liệu.
- `Query`: truy vấn dữ liệu.
- `Data integrity`: tính toàn vẹn dữ liệu.
- `Data security`: bảo mật dữ liệu.

**Ví dụ / ứng dụng:**
- Hệ thống quản lý thư viện dùng DBMS để lưu sách, độc giả và phiếu mượn.

### 8.3 Database Models

**Khái niệm chính:**
- Database model mô tả cách dữ liệu được tổ chức và liên hệ.
- Các mô hình phổ biến gồm hierarchical, network, relational và object-oriented.
- Relational database tổ chức dữ liệu thành bảng.

**Giải thích:**
Mô hình cơ sở dữ liệu quyết định cách lưu và truy xuất dữ liệu. Mô hình quan hệ (Relational Database) phổ biến vì dễ hiểu: dữ liệu nằm trong bảng, mỗi hàng là record, mỗi cột là field, các bảng liên hệ qua khóa.

| Mô hình | Đặc điểm |
|---|---|
| `Hierarchical database` | Tổ chức dạng cây cha-con |
| `Network database` | Cho phép quan hệ phức tạp hơn dạng cây |
| `Relational database` | Tổ chức thành bảng liên hệ |
| `Object-oriented database` | Lưu dữ liệu dưới dạng đối tượng |

**Thuật ngữ cần nhớ:**
- `Relational database`: cơ sở dữ liệu quan hệ.
- `Table`: bảng dữ liệu.
- `Primary key`: khóa chính định danh bản ghi.
- `Foreign key`: khóa ngoại liên kết bảng.

**Ví dụ / ứng dụng:**
- Bảng `Students` và bảng `Classes` có thể liên kết bằng mã lớp.

### 8.4 Data Mining

**Khái niệm chính:**
- Data mining là quá trình tìm mẫu, xu hướng hoặc quan hệ có ý nghĩa trong dữ liệu lớn.
- Data mining hỗ trợ ra quyết định trong kinh doanh, khoa học và quản lý.

**Giải thích:**
Tổ chức có thể có rất nhiều dữ liệu nhưng giá trị nằm ở việc phát hiện thông tin hữu ích. Data mining giúp tìm nhóm khách hàng, dự đoán hành vi, phát hiện gian lận hoặc phân tích xu hướng.

**Thuật ngữ cần nhớ:**
- `Data mining`: khai phá dữ liệu.
- `Pattern`: mẫu hoặc quy luật trong dữ liệu.
- `Prediction`: dự đoán dựa trên dữ liệu.
- `Data warehouse`: kho dữ liệu phục vụ phân tích.

**Ví dụ / ứng dụng:**
- Cửa hàng phân tích lịch sử mua hàng để đề xuất sản phẩm phù hợp.

## Unit 8B: Big Data, Information Systems, & Artificial Intelligence

### 8.5 The Evolving World of Big Data

**Khái niệm chính:**
- Big Data là dữ liệu có khối lượng rất lớn, tốc độ phát sinh nhanh và đa dạng.
- Big Data cần công nghệ lưu trữ, xử lý và phân tích đặc biệt.

**Giải thích:**
Dữ liệu từ giao dịch, mạng xã hội, cảm biến, thiết bị di động và website tăng nhanh. Big Data không chỉ là nhiều dữ liệu, mà còn là thách thức về tốc độ xử lý, độ đa dạng và khả năng khai thác thông tin có giá trị.

**Thuật ngữ cần nhớ:**
- `Big Data`: dữ liệu lớn.
- `Volume`: khối lượng dữ liệu.
- `Velocity`: tốc độ phát sinh và xử lý dữ liệu.
- `Variety`: độ đa dạng của dữ liệu.
- `Analytics`: phân tích dữ liệu.

**Ví dụ / ứng dụng:**
- Phân tích dữ liệu mạng xã hội để nhận biết xu hướng người dùng.

### 8.6 Information Systems in Organizations

**Khái niệm chính:**
- Hệ thống thông tin (Information System) kết hợp con người, quy trình, phần cứng, phần mềm và dữ liệu.
- Hệ thống thông tin hỗ trợ hoạt động, quản lý và ra quyết định trong tổ chức.

**Giải thích:**
Tổ chức dùng hệ thống thông tin để xử lý giao dịch, quản lý nguồn lực, hỗ trợ quyết định và phân tích chiến lược. Một hệ thống thông tin tốt giúp dữ liệu trở thành thông tin hữu ích.

| Loại hệ thống | Vai trò |
|---|---|
| `Transaction Processing System` | Xử lý giao dịch hằng ngày |
| `Management Information System` | Cung cấp báo cáo quản lý |
| `Decision Support System` | Hỗ trợ ra quyết định |
| `Executive Support System` | Hỗ trợ lãnh đạo cấp cao |

**Thuật ngữ cần nhớ:**
- `Information System`: hệ thống thông tin.
- `Transaction`: giao dịch.
- `Decision support`: hỗ trợ quyết định.
- `Report`: báo cáo.

**Ví dụ / ứng dụng:**
- Hệ thống bán hàng ghi nhận đơn hàng, tồn kho và doanh thu.

### 8.7 Artificial Intelligence

**Khái niệm chính:**
- Trí tuệ nhân tạo (Artificial Intelligence - AI) là lĩnh vực tạo hệ thống có khả năng thực hiện nhiệm vụ đòi hỏi trí thông minh.
- AI có thể liên quan đến học máy, xử lý ngôn ngữ tự nhiên, thị giác máy tính, robot và hệ chuyên gia.

**Giải thích:**
AI hướng đến việc giúp máy tính nhận biết, suy luận, học từ dữ liệu và hành động. Trong thực tế, AI được dùng trong gợi ý sản phẩm, nhận dạng giọng nói, nhận dạng khuôn mặt, tìm kiếm và hỗ trợ quyết định.

**Thuật ngữ cần nhớ:**
- `Artificial Intelligence`: trí tuệ nhân tạo.
- `Expert system`: hệ chuyên gia.
- `Natural language processing`: xử lý ngôn ngữ tự nhiên.
- `Machine learning`: học máy.
- `Robotics`: robot học.

**Ví dụ / ứng dụng:**
- Hệ thống gợi ý phim hoặc sản phẩm dựa trên lịch sử sử dụng.

### 8.8 Artificial Life, the Turing Test, & Singularity

**Khái niệm chính:**
- Artificial life nghiên cứu mô phỏng đặc tính của sự sống bằng hệ thống nhân tạo.
- Turing Test là ý tưởng kiểm tra khả năng máy thể hiện hành vi thông minh giống con người.
- Singularity là giả thuyết về thời điểm trí tuệ máy vượt xa trí tuệ con người.

**Giải thích:**
Các chủ đề này mở rộng AI từ ứng dụng thực tế sang câu hỏi triết học và xã hội: máy có thể suy nghĩ như con người không, sự sống nhân tạo có thể tồn tại dưới dạng nào, và xã hội sẽ thay đổi ra sao nếu máy trở nên thông minh hơn con người.

**Thuật ngữ cần nhớ:**
- `Artificial life`: sự sống nhân tạo.
- `Turing Test`: phép thử đánh giá khả năng máy mô phỏng đối thoại thông minh.
- `Singularity`: điểm kỳ dị công nghệ giả định khi trí tuệ máy vượt con người.

**Ví dụ / ứng dụng:**
- Chatbot được dùng để mô phỏng hội thoại với người dùng, liên quan đến ý tưởng của Turing Test.

## Tóm tắt chương
- Dữ liệu có thể được tổ chức theo field, record, file và database.
- DBMS giúp quản lý database hiệu quả, bảo mật và nhất quán.
- Mô hình database quan hệ tổ chức dữ liệu thành bảng.
- Data mining giúp tìm mẫu và tri thức từ dữ liệu.
- Big Data đặt ra thách thức về khối lượng, tốc độ và đa dạng dữ liệu.
- Information systems hỗ trợ hoạt động và ra quyết định trong tổ chức.
- AI nghiên cứu hệ thống có khả năng thực hiện nhiệm vụ thông minh.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Field | Trường dữ liệu |
| Record | Bản ghi |
| File | Tập hợp dữ liệu lưu dưới một tên |
| Database | Cơ sở dữ liệu |
| DBMS | Hệ quản trị cơ sở dữ liệu |
| Relational Database | Cơ sở dữ liệu quan hệ |
| Data Mining | Khai phá dữ liệu |
| Big Data | Dữ liệu lớn |
| Information System | Hệ thống thông tin |
| Artificial Intelligence | Trí tuệ nhân tạo |
| Turing Test | Phép thử đánh giá khả năng máy đối thoại như người |
| Singularity | Giả thuyết điểm kỳ dị công nghệ |

## Câu hỏi ôn tập
1. Field, record và file khác nhau như thế nào?
2. Database khác file dữ liệu rời rạc ở điểm nào?
3. DBMS có vai trò gì?
4. Mô hình cơ sở dữ liệu quan hệ tổ chức dữ liệu như thế nào?
5. Data mining dùng để làm gì?
6. Big Data có những đặc điểm chính nào?
7. Hệ thống thông tin gồm những thành phần nào?
8. AI là gì và có ứng dụng nào trong đời sống?
9. Turing Test nói về vấn đề gì?
