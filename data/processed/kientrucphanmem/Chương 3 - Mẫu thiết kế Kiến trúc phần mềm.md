# Chương 3 - Mẫu thiết kế Kiến trúc phần mềm



<!-- page 1 -->

HỌC VIỆN NGÂN HÀNG
KHOA CÔNG NGHỆ THÔNG TIN VÀ KINH TẾ SỐ

# CHƯƠNG 3
# MẪU THIẾT KẾ KIẾN TRÚC PHẦN MỀM

Hà Nội - 2024


<!-- page 2 -->

# Nội dung trình bày

- **Mẫu thiết kế Kiến trúc phần mềm là gì?**
- **Giới thiệu các loại Mẫu thiết kế Kiến trúc phần mềm**

---
Chương 1: Tổng quan Kiến trúc phần mềm


<!-- page 3 -->

# Mẫu thiết kế là gì?

- Nhà kiến trúc Christopher Alexander nói: **“Mỗi mẫu mô tả một vấn đề xảy ra lặp đi lặp lại trong môi trường của chúng ta, sau đó mô tả cốt lõi của giải pháp cho vấn đề đó, theo cách mà bạn có thể sử dụng giải pháp đó hàng triệu lần mà không cần phải làm gì cả”**.
- Mặc dù Alexander đang nói về các mẫu trong các tòa nhà và thị trấn, nhưng những gì ông ấy nói là đúng về các mẫu thiết kế hướng đối tượng. Đây là ý tưởng để áp dụng cho nhiều ngành khác đặc biệt ngành Kiến trúc phần mềm.

4/16/24 Chương 3: Mẫu thiết kế Kiến trúc phần mềm 3


<!-- page 4 -->

# Mẫu thiết kế là gì?

Nói chung, một mẫu có bốn yếu tố thiết yếu. Mẫu có thể sử dụng để mô tả một vấn đề thiết kế, các giải pháp và hậu quả của nó.

- **Sự cố** mô tả thời điểm áp dụng mẫu. Nó giải thích các vấn đề và bối cảnh của nó.
- **Giải pháp** mô tả các yếu tố tạo nên thiết kế, mối quan hệ, trách nhiệm và sự hợp tác của chúng.
- **Hậu quả** là kết quả và sự đánh đổi của việc áp dụng mô hình.

Chương 3: Mẫu thiết kế Kiến trúc phần mềm


<!-- page 6 -->

# Mẫu thiết kế

| Mục đích | Mẫu thiết kế |
| :--- | :--- |
| - **Mẫu thiết kế Structural**: một nhóm các mẫu thiết kế được sử dụng để tạo ra các cấu trúc phức tạp từ các lớp và đối tượng, bằng cách kết hợp chúng một cách linh hoạt và hiệu quả. <br><br> - **Mẫu thiết kế Structural** thường tập trung vào cách các lớp và đối tượng tương tác với nhau để tạo ra các cấu trúc lớn hơn mà không làm thay đổi các thành phần cơ bản. | **Adapter Pattern (Mẫu Adapter)**: Chuyển đổi giao diện của một lớp thành giao diện khác mà một client mong muốn sử dụng. Điều này cho phép các lớp làm việc cùng nhau mặc dù chúng có các giao diện không tương thích. <br><br> **Bridge Pattern (Mẫu Bridge)**: Tách biệt một phần logic từ một lớp và đưa nó vào một lớp khác, với mục tiêu làm cho cả hai có thể thay đổi độc lập với nhau. <br><br> **Composite Pattern (Mẫu Composite)**: Tạo ra một cấu trúc cây để đại diện cho một nhóm các đối tượng. Điều này cho phép client xử lý các đối tượng đơn lẻ và các nhóm đối tượng theo cùng một cách. <br><br> **Decorator Pattern (Mẫu Decorator)**: Thêm các tính năng mới cho đối tượng mà không làm thay đổi giao diện của nó. Điều này cho phép mở rộng tính năng của một đối tượng mà không phải sửa đổi lớp đó. |


<!-- page 7 -->

# Mẫu thiết kế

| Mục đích | Mẫu thiết kế |
| :--- | :--- |
| - **Mẫu thiết kế Structural**: một nhóm các mẫu thiết kế được sử dụng để tạo ra các cấu trúc phức tạp từ các lớp và đối tượng, bằng cách kết hợp chúng một cách linh hoạt và hiệu quả.<br>- **Mẫu thiết kế Structural** thường tập trung vào cách các lớp và đối tượng tương tác với nhau để tạo ra các cấu trúc lớn hơn mà không làm thay đổi các thành phần cơ bản. | **Facade Pattern (Mẫu Facade)**: Cung cấp một giao diện đơn giản để truy cập một hệ thống phức tạp. Điều này giúp che dấu sự phức tạp của hệ thống và làm cho việc sử dụng nó dễ dàng hơn.<br><br>**Proxy Pattern (Mẫu Proxy)**: Cung cấp một đối tượng đại diện (proxy) để kiểm soát quyền truy cập đến đối tượng gốc. Điều này có thể được sử dụng để kiểm soát quyền truy cập, tải trước dữ liệu, hoặc làm các thao tác khác trước hoặc sau khi truy cập đối tượng gốc.<br><br>**Flyweigh Pattern (Mẫu Flyweight)**: hướng tới giảm lượng bộ nhớ được sử dụng hoặc giảm tải cho CPU bằng cách chia sẻ các thành phần có chung giữa các đối tượng khác nhau thay vì lưu trữ riêng lẻ cho mỗi đối tượng. |


<!-- page 8 -->

# Mẫu thiết kế

| Mục đích | Mẫu thiết kế |
| :--- | :--- |
| - **Mẫu thiết kế Behavioral**: là một nhóm các mẫu thiết kế trong lập trình hướng đối tượng, được sử dụng để tập trung vào cách các đối tượng tương tác với nhau và phân phối trách nhiệm giữa chúng một cách linh hoạt và hiệu quả.<br>- **Mục tiêu của mẫu thiết kế Behavioral** là tăng tính linh hoạt trong việc mô tả cách các đối tượng tương tác trong hệ thống, giảm sự phụ thuộc giữa các thành phần, và tăng tính tái sử dụng của mã. | **Observer Pattern (Mẫu Observer)**: Định nghĩa một quan hệ một-nhiều giữa các đối tượng sao cho khi một đối tượng thay đổi trạng thái, tất cả các đối tượng phụ thuộc của nó sẽ được thông báo và cập nhật tự động.<br><br>**Strategy Pattern (Mẫu Strategy)**: Định nghĩa một tập hợp các thuật toán, đóng gói mỗi thuật toán và làm cho chúng có thể thay đổi linh hoạt. Client có thể chọn một thuật toán cụ thể từ tập hợp và thay đổi nó theo nhu cầu của mình.<br><br>**Command Pattern (Mẫu Command)**: Biến một yêu cầu thành một đối tượng độc lập, cho phép bạn thực hiện các yêu cầu khác nhau, hoạt động hủy, hoặc lên lịch chúng.<br><br>**Chain of Responsibility Pattern (Mẫu Chain of Responsibility)**: Cho phép bạn xác định một chuỗi các đối tượng xử lý yêu cầu liên tiếp nhau, cho đến khi một trong số họ xử lý yêu cầu đó hoặc cho đến khi nó đến cuối chuỗi.<br><br>**Iterator Pattern (Mẫu Iterator)**: Cung cấp một cách để tuần tự truy cập các phần tử của một tập hợp mà không cần phải tiết lộ cấu trúc nội bộ của tập hợp đó. |


<!-- page 10 -->

# Mẫu thiết kế

| Mục đích | Mẫu thiết kế |
| :--- | :--- |
| - **Mẫu thiết kế Behavioral**: là một nhóm các mẫu thiết kế trong lập trình hướng đối tượng, được sử dụng để tập trung vào cách các đối tượng tương tác với nhau và phân phối trách nhiệm giữa chúng một cách linh hoạt và hiệu quả.<br><br>- **Mục tiêu của mẫu thiết kế Behavioral** là tăng tính linh hoạt trong việc mô tả cách các đối tượng tương tác trong hệ thống, giảm sự phụ thuộc giữa các thành phần, và tăng tính tái sử dụng của mã. | **Memento Pattern (Mẫu Memento)**: cho phép lưu trữ và phục hồi trạng thái trước của một đối tượng mà không tiết lộ chi tiết bên trong của nó.<br><br>Ví dụ, nó có thể được sử dụng trong các trình soạn thảo văn bản để lưu trữ trạng thái của văn bản trước khi người dùng thực hiện các thao tác chỉnh sửa, để sau đó có thể phục hồi lại trạng thái trước đó nếu cần.<br><br>**State Pattern (Mẫu State)**: cho phép một đối tượng thay đổi hành vi của mình khi trạng thái nội bộ của nó thay đổi. Mỗi trạng thái của một đối tượng được biểu diễn bởi một lớp riêng biệt và đối tượng này duy trì một tham chiếu đến trạng thái hiện tại của nó. Khi trạng thái của đối tượng thay đổi, nó thay đổi tham chiếu của mình đến đối tượng trạng thái tương ứng. |
