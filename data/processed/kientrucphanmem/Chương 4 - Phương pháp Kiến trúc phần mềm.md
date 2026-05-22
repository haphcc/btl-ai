# Chương 4 - Phương pháp Kiến trúc phần mềm



<!-- page 3 -->

# Phương pháp Kiến trúc phần mềm

- Phương pháp kiến trúc phần mềm (**Software Architecture Methodology**) là một cách tiếp cận hệ thống hóa và tổ chức các thành phần của một hệ thống phần mềm. Nó không chỉ tập trung vào việc thiết kế các thành phần cụ thể, mà còn quan tâm đến cách các thành phần này tương tác với nhau, cách chúng được triển khai và mở rộng trong thời gian.

- **What**: Functional Non-Functional Requirements
- **How**: Design
- **Why**: Rationale
- **A**

Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 16 -->

# Kiến trúc phân lớp từ những năm 2000 - nay

## User Interface

- Chịu trách nhiệm trong việc render và truyền tải thông điệp từ client tới server.
- Client ở đây có thể là người dùng hoặc những application khác.

---
**Các tầng trong sơ đồ:**
- User Interface
- Application
- Domain
- Infrastructure


<!-- page 18 -->

# Kiến trúc phân lớp từ những năm 2000 - nay

## Domain Layer
- Layer này chứa các logic liên quan đến nghiệp vụ của ứng dụng, các Entities, Events, và bất cứ object nào handle logic nghiệp vụ. Rõ ràng, nó giống như **Entiy** trong **EBI Architecture**; là **trái tim** của cả hệ thống.

## Infrastructure
- Các common technical facilities dùng chung cho cả hệ thống, ví dụ như logging, persistance, messaging,...

---

**Các lớp trong sơ đồ:**
- User Interface
- Application
- Domain
- Infrastructure

---
Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 20 -->

# ANTI-PATTERN: LASAGNA ARCHITECTURE

- Việc tổ chức, đóng gói layer theo chức năng kỹ thuật (functional) của nó, ví dụ như UI, Domain, DB,.. mà không chia theo chức năng nghiệp vụ (component) như Product, Payment, Checkout, làm mất đi khả năng module hóa và đóng gói (encapsulation) theo domain concept.

Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 21 -->

# Ưu điểm của Phân lớp

- Chúng ta chỉ cần hiểu những lớp bên dưới lớp chúng ta đang làm;
- Mỗi lớp có thể được thay thế bởi một thể hiện tương đương (equivalent implementation), không ảnh hưởng đến các lớp khác;
- Một lớp có thể được sử dụng bởi một số lớp cấp cao khác nhau


<!-- page 23 -->

# Kết luận

- Layered Architecture là một cách chia để trị mối quan tâm, đóng gói và tách riêng, bằng cách nhóm các đơn vị mã bằng vai trò chức năng của chúng trong ứng dụng.
- Tuy nhiên, như hầu hết mọi thứ trong cuộc sống, quá nhiều sẽ phản tác dụng! Vì vậy, quy tắc của ngón tay cái (rule-of-thumb) là: Chỉ sử dụng các lớp chúng ta cần, các lớp chúng ta cần, và không có gì nhiều hơn nữa! Chúng ta không được đuổi theo đuổi một chén thánh kiến trúc, cái không hề tồn tại. Những gì tồn tại là một nhu cầu, và sự phù hợp tốt nhất có thể cho nhu cầu đó. Đó là một phần của Lean, tiện thể.
- Hơn nữa, điều quan trọng cần lưu ý là phương pháp tiếp cận top/down này đã lỗi thời. Không còn là những gì chúng ta nên làm trong phát triển phần mềm hiện đại.


<!-- page 25 -->

# Thực trạng

- Phần mềm ngày nay đang ngày càng trở nên phức tạp và dường như đang vượt khỏi khả năng kiểm soát của các mô hình phát triển phần mềm hiện có
- Nguyên nhân:
  - sự xuất hiện của nhiều công nghệ mới tạo nên môi trường không đồng nhất, trong khi nhu cầu về trao đổi, chia sẻ, tương tác giữa các hệ thống không thể đáp ứng được trong một môi trường như vậy
  - vấn đề lập trình dư thừa và không thể tái sử dụng


<!-- page 26 -->

# Giải pháp

- Có một cách tiếp cận giải quyết khá toàn diện mọi khó khăn nêu trên và nó đã được triển khai trong thực tế.
- Cách tiếp cận đó gọi là “Kiến trúc hướng dịch vụ” - Service-oriented Architecture (SOA).


<!-- page 28 -->

# Kiến trúc hướng dịch vụ là gì?

- SOA là một hướng tiếp cận với việc thiết kế và tích hợp các phần mềm hay chức năng hệ thống theo dạng module, trong đó mỗi module đóng vai trò là một **“dịch vụ có tính kết nối lỏng lẻo”** và có khả năng truy cập thông qua môi trường mạng.
- SOA là hướng tiếp cận xây dựng phần mềm dựa trên sự kết hợp các dịch vụ

**SOA (Service Oriented Architecture)**

- **Process**: Align IT with Business Operations
- **Practice**: Employ Best Practices Methodology
- **Platform**: Increase Operational Efficiency
- **People**: Empower Decision Makers

Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 29 -->

# Kiến trúc hướng dịch vụ là gì?

*   **Service Broker**
*   **Service Consumer**
    *   Client
*   **Service Provider**
    *   Service
*   **Service Contract**
    *   ...
    *   ...

**Các mối quan hệ / tương tác:**
*   **Publish** (từ Service Provider đến Service Broker)
*   **Find** (từ Service Consumer đến Service Broker)
*   **Interact** (giữa Client và Service)

## Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 30 -->

# Các thành phần Kiến trúc hướng dịch vụ (1)

- **Dịch vụ (Service):** Là thành phần cơ bản của SOA, một dịch vụ là một phần của ứng dụng thực hiện một chức năng cụ thể và có khả năng tái sử dụng. Dịch vụ thường được truy cập thông qua các giao diện tiêu chuẩn như HTTP, SOAP hoặc REST.
- **Giao diện Dịch vụ (Service Interface):** Là cách mà các dịch vụ được truy cập và tương tác bên ngoài. Giao diện này định nghĩa các phương thức và tham số cần thiết để gọi và sử dụng dịch vụ.
- **Hợp đồng Dịch vụ (Service Contract):** Là một tài liệu hoặc một bản khai báo mà xác định các yêu cầu và cam kết giữa người sử dụng dịch vụ và nhà cung cấp dịch vụ. Hợp đồng này bao gồm các quy định về cách giao tiếp, định dạng dữ liệu và các điều kiện kỹ thuật khác.


<!-- page 33 -->

# SOA là hướng tiếp cận tiến bộ

```
       Software Reusability                      Communication

            Services <------------------------> Services
               ^                                    ^
       Distributed Objects                     Web Services
               ^                                    ^
          Components                           Proprietary Technologies
               ^                                    ^
            Modules                            Proprietary Technologies
```

*source: Sam Gentile*

---
Chương 4: Phương pháp Kiến trúc phần mềm


<!-- page 37 -->

# Nguyên tắc xây dựng kiến trúc hướng dịch vụ

**Sự phân định ranh giới rạch ròi giữa các dịch vụ:**

- Các dịch vụ thực hiện quá trình tương tác chủ yếu thông qua thành phần giao tiếp.
- Thành phần giao tiếp qui định về những định dạng thông điệp sử dụng trong quá trình trao đổi - cách duy nhất để các đối tượng bên ngoài có thể truy cập thông tin và chức năng của dịch vụ.
- Ta chỉ cần gửi các thông điệp theo các định dạng đã được định nghĩa trước mà không cần phải quan tâm đến cách xử lý của dịch vụ như thế nào


<!-- page 41 -->

# Ưu điểm của SOA

- Sử dụng lại những thành phần hoặc dịch vụ có sẵn giúp tiết kiệm chi phí và thời gian xây dựng ứng dụng
- Cung cấp giải pháp ứng dụng tổng hợp cho doanh nghiệp (tích hợp các ứng dụng rời rạc thành hệ thống đồng nhất)
- Tính loose coupling (kết nối lỏng lẻo) giúp tăng tính linh hoạt và khả năng triển khai cài đặt
- Thích ứng với những thay đổi trong tương lai (giảm rủi ro do có thay đổi hoặc lỗi trong thiết kế hệ thống)
- Hỗ trợ đa thiết bị và đa nền tảng
- Tăng khả năng mở rộng và khả năng sẵn sàng cung cấp


<!-- page 60 -->

# HỎI/ĐÁP

Question?

Chương 4 - Phương pháp Kiến trúc phần mềm
