# Nội dung trình bày

- **Một số khái niệm**
- Tại sao cần xây dựng Kiến trúc phần mềm?
- Kiến trúc phần mềm là gì?
- Nguyên tắc Kiến trúc phần mềm

# Kiến trúc phần mềm (1)

- **Kiến trúc phần mềm (SA)** là thiết kế mức khái quát của một hệ thống phần mềm, chỉ ra những đặc tính hệ thống mong muốn đạt được, và lý do cần đạt được chúng.

*H. Washizaki¹ cho rằng SA là “một tập các cấu trúc cần thiết để suy luận về hệ thống, trong đó bao gồm các thành phần phần mềm, mối quan hệ giữa chúng và thuộc tính của chúng”*

¹*Tác giả của cuốn “Guide to the Software Engineering Body of Knowledge (SWEBOK Guide)”*

**Sơ đồ:**
- **What**: Functional, Non-Functional Requirements
- **How**: Design
- **Why**: Rationale
- **A**: (Giao điểm của What, How, Why)

# Kiến trúc phần mềm (2)

- SA có vai trò giúp mô tả:
    - **Chức năng hoặc mục đích** (Function or Purpose): được mô tả bởi một số trường hợp trong các kịch bản, chức năng hoặc thành phần logic
    - **Cấu trúc** (Structure): mô hình của hệ thống, vật lý hoặc các thành phần của hệ thống và mối quan hệ giữa chúng
    - **Nguyên tắc** (Principles) hoặc **Khuôn mẫu** (Patterns)

## Kiến trúc phần mềm (3)

- SA có vai trò giúp mô tả:
    - Mối quan tâm của các bên liên quan.
    - Khoảng cách giữa thiết kế hệ thống hiện tại và thiết kế của nó trong tương lai.
    - Đánh giá các thuộc tính chi phối thiết kế và sự phát triển của hệ thống.
    - Các quyết định cơ bản đóng góp tạo ra tiện ích, chi phí, nỗ lực xây dựng và rủi ro khi sử dụng trong môi trường cụ thể.
    - Tìm ra được điều gì khó thay đổi.

## Lịch sử Kiến trúc phần mềm (I)

*   Những kiến thức cơ bản về kiến trúc phần mềm được Dijkstra giới thiệu (1968) và Parnas (1970).
    *   Vai trò then chốt của cấu trúc một hệ thống phần mềm.
    *   Việc xác định cấu trúc phù hợp cho một hệ thống nhất định khó đến mức nào?

BAV HỌC VIỆN
NGÂN HÀNG
1961

# Lịch sử Kiến trúc phần mềm (2)

- Rất nhiều nghiên cứu đã được tiến hành về kiến trúc phần mềm bắt đầu từ những năm 90, chủ yếu tập trung vào:
  - Cách giải quyết các vấn đề kiến trúc tái diễn (mẫu - patterns)
  - Những hình thức kiến trúc nào phổ biến hơn (phong cách - style)
  - Xác định ngôn ngữ mô tả kiến trúc phần mềm (ADL)
  - Làm sao để tài liệu hoá kiến trúc của một hệ thống phần mềm (các khung nhìn - views)
- ... tuyên bố đã đưa ra định nghĩa về một ngành học.

# Nội dung trình bày

- Một số khái niệm
- Tại sao cần xây dựng Kiến trúc phần mềm?
- Kiến trúc phần mềm là gì?
- Nguyên tắc Kiến trúc phần mềm

BAV HỌC VIỆN NGÂN HÀNG
1961

## Giảm thiểu độ phức tạp (1)

*   Hệ thống phần mềm lớn hơn và phức tạp hơn
    *   Năm 2007, hệ điều hành Windows có quy mô lên tới 60 triệu dòng mã (LoC) từ 15 triệu dòng vào năm 1995
    *   Năm 2011, quy mô phần mềm BMW 7 Series đạt 200 triệu LoC
    *   Năm 2011 quy mô phần mềm của Airbus 380 đạt 1 tỷ LoC.
    *   Năm 2015 Google là 2 tỷ LoC

## Giảm thiểu độ phức tạp (2)

*   Thiết kế quy mô lớn trở thành quy luật chung
*   Từ đối tượng và phương thức...
    *   Đến các module và các thành phần ...
    *   ... Đến với các hệ thống lớn và phức tạp ...
    *   ... ... Đến hệ thống của hệ thống ...
    *   ... ... ... Đến ...

BAV HỌC VIỆN NGÂN HÀNG BANKING ACADEMY OF VIETNAM
# Bối cảnh phần mềm ngày một lớn

## Kiểu phần mềm
- Middleware
- Embedded
- Open Source
- Web Services
- Mobile (e.g. applet)
- Data Mining, Search engine
- Agents
- Social software (e.g. Web 2.0)
- Software ecosystems
- ...

## Chuẩn phần mềm
- Chuẩn IEEE: phương thức phát triển
- Chuẩn OMG: UML and CORBA
- Chuẩn W3C: Các công nghệ Web
- Chuẩn OASIS: quy trình nghiệp vụ

01/12/202
Chương 1: Tổng quan Kiến trúc phần mềm

## Sản xuất phần mềm khó khăn (1)

- Sự phức tạp bắt nguồn từ
  - Đổi mới kỹ thuật, công nghệ nhanh chóng
  - Cạnh tranh quốc tế mạnh mẽ
  - Vấn đề tâm lý
  - Vấn đề tổ chức
  - Thiếu chuyên gia được đào tạo về thiết kế và phát triển phần mềm

# Sn xut phn mm kh khn (2)

*   Nhng tht bi in hnh: qun l d n km, yu cu sai, thit k tm thng, chi ph qu cao
*   Cc bn lin quan c li ch tri ngc nhau
*   D n mi khi u ri ro cao, t c phn tch

**NHNG QUYT NH SAI LM TRONG VIC XY DNG KIN TRC PHN MM CA H THNG L NGUYN NHN CHNH KHIN D N B HY B**

## Mức độ tái sử dụng phần mềm

- Mẫu thiết kế
  - Tái sử dụng ý tưởng chứ không phải mã
- Mã nguồn mở
  - Các ứng dụng có thể tái sử dụng
- Nhân bản phần mềm
  - Sao chép và dán, pb là khả năng bảo trì và sở hữu trí tuệ
- Công nghệ phần mềm dựa trên thành phần
  - Thành phần có sẵn
- Dòng sản phẩm phần mềm
  - Tạo ra một thành viên mới trong gia đình tập trung vào phần biến đổi
- Kiến trúc phần mềm
  - Tái sử dụng các phần tử, mối quan hệ của chúng và các quyết định liên quan

# Kiến trúc phần mềm (1)

- Quá trình sáng tạo & ra quyết định chứ không phải là một hoạt động.
- Các quyết định cơ bản:
  - Dựa trên tác động lên các thuộc tính chất lượng và sự cân bằng giữa các thuộc tính chất lượng cạnh tranh
  - Ảnh hưởng sâu sắc đến phần mềm và quá trình phát triển

# Kiến trúc phần mềm (2)

- Kiến trúc phần mềm là kết quả của quá trình quyết định này:
    - Kiến trúc phần mềm là tập hợp các quyết định thiết kế mà nếu thực hiện không đúng có thể khiến dự án của bạn bị hủy bỏ (Eoin Woods)
    - Kiến trúc phần mềm đại diện cho “các quyết định quan trọng”, trong đó tầm quan trọng được đo bằng chi phí thay đổi (cost of change) (Grady Booch)

# Kiến trúc phần mềm vs Kỹ thuật phần mềm

| **Kiến trúc phần mềm** | **Kỹ thuật phần mềm** |
| :--- | :--- |
| - Nghiên cứu các quyết định chi phối việc thiết kế hệ thống phần mềm và nghiên cứu các phương pháp tái sử dụng phần mềm<br><br>- Tập trung vào ý tưởng giảm độ phức tạp của phần mềm thông qua việc trừu tượng hóa, tách biệt các mối quan tâm và tái sử dụng<br><br>- Còn khá non nớt: khó tìm được hai kiến trúc sư phần mềm đồng ý về cách thiết kế hệ thống phần mềm đúng đắn | - Nghiên cứu các phương pháp xây dựng hệ thống và sản phẩm phần mềm, các lý thuyết làm cơ sở và các công cụ hữu ích để phát triển và đo lường chất lượng của phần mềm<br><br>- Giải quyết các nguồn lực hạn chế<br><br>- Là một môn học mang tính thực nghiệm mạnh mẽ, dựa trên kinh nghiệm và các dự án trong quá khứ |

# Kiến trúc phần mềm vs Thiết kế phần mềm, Yêu cầu phần mềm (1)

| **Kiến trúc phần mềm**<br>(Software architecture) | **Thiết kế phần mềm**<br>(Software design) | **Yêu cầu phần mềm**<br>(Software requirements) |
| :--- | :--- | :--- |
| - Cái gì, ở đâu và tại sao (what, where, why) chứ không phải như thế nào (how)<br>- Góc nhìn tổng thể cho thấy hệ thống đáp ứng yêu cầu như thế nào, ghi lại các thành phần phần mềm chính và cách chúng tương tác với nhau<br>- Rất trừu tượng, cố tình che giấu chi tiết | - Là cách thức (how) của một quá trình phát triển phần mềm | - Nêu 'cái gì' (what) phần mềm nên làm chứ không phải 'làm thế nào' (how)<br>- Có thể có chức năng và không có chức năng |

# Nội dung trình bày

- Một số khái niệm
- Tại sao cần xây dựng Kiến trúc phần mềm?
- Kiến trúc phần mềm là gì?
- **Nguyên tắc Kiến trúc phần mềm**

# Kiến trúc phần mềm vs Thiết kế phần mềm, Yêu cầu phần mềm (2)

* Những yêu cầu nào là quan trọng nhất đối với thiết kế kiến trúc?

**Sơ đồ quy trình:**
* **Functional Requirements** $\rightarrow$ **Architectural Design** $\rightarrow$ **Software Architecture**
* **Design Constraints** $\rightarrow$ **Architectural Design**
* **Non-Functional Requirements = Quality Attribute** $\rightarrow$ **Architectural Design**

* Những yêu cầu nào là quan trọng nhất khi nói đến cấu trúc của một kiến trúc?

---
Chương 1: Tổng quan Kiến trúc phần mềm

# Những gì cần xem xét?

* Có gì sai khi thiết kế một hệ thống có một mô-đun mã nguồn lớn, một mô-đun đối tượng lớn và một mô-đun thực thi lớn miễn là nó hoạt động bình thường?

| | | |
| :--- | :---: | :--- |
| **buildability** | **Module** | **portability** |
| **modifiability** | 1 : ... | **reliability** |
| **testability** | 2 : ... | **distributability** |
| **complexity** | 3 : ... | **availability** |
| **maintainability** | . <br> . <br> . | **reusability** |
| | 1,999,999 : ... | |
| | 2,000,000 : ... | |
| | **Others?** | |

* Bạn nghĩ sẽ có những yêu cầu gì? bị ảnh hưởng tiêu cực bởi “thiết kế” này?

# Yêu cầu & Thiết kế kiến trúc

* Những yêu cầu nào là quan trọng nhất đối với thiết kế kiến trúc?

* Functional Requirements
* **Design Constraints**
* **Non-Functional Requirements = Quality Attribute**

$$\rightarrow \text{Architectural Design} \rightarrow \text{Software Architecture}$$

* Điều gì quyết định liệu những yêu cầu này có được đáp ứng hay không?

# Những ảnh hưởng khác đến Kiến trúc

* **Requirements** $\rightarrow$ **Architectural Design**
* **Technical**, **Business**, **Social** (influences) $\rightarrow$ **Architectural Design**
* **Architectural Design** $\rightarrow$ **Software Architecture**

# Ví dụ về những ảnh hưởng khác đến Kiến trúc

- Các bên liên quan
  - Khách hàng, người dùng, người quản lý, tiếp thị, nhà phát triển, người bảo trì, v.v.
- Tổ chức phát triển
  - Mục tiêu kinh doanh trước mắt và lâu dài cơ cấu tổ chức
- Môi trường Kỹ thuật
  - Hướng đối tượng, WWW, tác nhân thông minh, EJB, hướng dịch vụ, J2EE, máy khách mỏng, .NET, v.v.
- Bối cảnh và kinh nghiệm
  - Kinh nghiệm kiến trúc và tổ chức
  - Giáo dục và đào tạo

# Kiến trúc là nguồn ảnh hưởng

- Hiểu được chu kỳ ảnh hưởng giúp lập kế hoạch và quản lý sự thay đổi trong suốt vòng đời của hệ thống

### Sơ đồ chu kỳ ảnh hưởng:

- **Requirements** $\rightarrow$ **Architectural Design**
- **Technical, Business, Social** $\xrightarrow{\text{influences}}$ **Architectural Design**
- **Architectural Design** $\rightarrow$ **Software Architecture**
- **Software Architecture** $\xrightarrow{\text{influences}}$ **Technical, Business, Social**

# Kiến trúc & Bối cảnh thiết kế kiến trúc

## Quy trình thiết kế kiến trúc (Architectural Design Process)

### CONTEXT (Bối cảnh)
*   **Requirements gathering** (Thu thập yêu cầu)

### ARCHITECTURAL DESIGN (Thiết kế kiến trúc)
*   **Development of alternatives** (Phát triển các phương án thay thế)
*   **Evaluation of alternatives** (Đánh giá các phương án thay thế)
*   **Decision making** (Ra quyết định)
*   **Documenting** (Tài liệu hóa)

### Luồng tương tác (Flow)
*   **Requirements gathering** $\rightarrow$ *(Requirements, Context)* $\rightarrow$ **Development of alternatives**
*   **Development of alternatives** $\rightarrow$ **Evaluation of alternatives** $\rightarrow$ **Decision making** $\rightarrow$ *[Decision Point]*
*   *[Decision Point]* $\rightarrow$ *(Acceptable)* $\rightarrow$ **Documenting**
*   *[Decision Point]* $\rightarrow$ *(Unacceptable / Context refinement)* $\rightarrow$ **Requirements gathering**

---

https://www.iasaglobal.org/on-making-architectural-decisions/

---

## Bối cảnh kiến trúc (Architectural Context)

### Các phân vùng bối cảnh (Context Levels)
*   **NARROW CONTEXT** (Bối cảnh hẹp)
*   **WIDE CONTEXT** (Bối cảnh rộng)
*   **EXTENDED CONTEXT** (Bối cảnh mở rộng)

### Các yếu tố ảnh hưởng (Factors)
*   **External factors (Yếu tố bên ngoài):** Trends, Market, Economics, Politics, Technology, Methodology, ...
*   **Internal factors (Yếu tố bên trong):** Budget, Team, Infrastructure, Time, ...
*   **Constraints (Ràng buộc):** Chịu ảnh hưởng từ các yếu tố bên ngoài (External factors) và bên trong (Internal factors).

### Các vai trò và mối quan hệ (Roles & Relationships)
*   **Architect (Kiến trúc sư):**
    *   Sở hữu: Experience (Kinh nghiệm), Knowledge (Kiến thức), Preferences (Sở thích), ...
    *   *takes into account* (cân nhắc) Constraints (Ràng buộc).
    *   *makes* (đưa ra) Decisions (Quyết định).
    *   *creates* (tạo ra) Architecture (Kiến trúc).
    *   *elicits* (khai thác) Requirements (Yêu cầu).
*   **Analyst (Nhà phân tích):**
    *   *takes into account* (cân nhắc) Constraints (Ràng buộc).
    *   *elicits* (khai thác) Requirements (Yêu cầu).
*   **Stakeholders (Các bên liên quan):**
    *   *have* (có) Concerns (Mối quan ngại).
    *   *want to solve* (muốn giải quyết) Business problem, need (Vấn đề, nhu cầu kinh doanh).

### Mối quan hệ giữa các thành phần (Component Relationships)
*   **Concerns** $\rightarrow$ *Takes into account* $\rightarrow$ **Decisions**
*   **Decisions** $\rightarrow$ *is based on* $\rightarrow$ **Architecture**
*   **Architecture** $\rightarrow$ *describes* $\rightarrow$ **Business solution**
*   **Requirements** $\rightarrow$ *implements* $\rightarrow$ **Business solution**
*   **Requirements** $\rightarrow$ *are based on* $\rightarrow$ **Business problem, need**
*   **Business solution** $\rightarrow$ *solves* $\rightarrow$ **Business problem, need**

# Nguyên tắc Kiến trúc phần mềm (1)

- Thiết kế kiến trúc không có quy tắc dừng:
  - Không có tiêu chí nào cho biết khi nào kiến trúc hoàn thành
- Giải pháp cho các vấn đề kiến trúc không đúng hoặc sai:
  - Thông thường chúng tốt hoặc xấu; giải quyết một vấn đề rất có thể dẫn đến một vấn đề hoàn toàn khác ở nơi khác trong hệ thống
- Thiết kế kiến trúc liên quan đến sự cân bằng, chẳng hạn như sự cân bằng giữa tốc độ và độ bền:
  - Kết quả là có một số giải pháp có thể chấp nhận được, thay vì một giải pháp tốt nhất

# Nguyễn tắc Kiến trúc phần mềm (2)

- Các vấn đề về thiết kế kiến trúc không có một tập hợp các giải pháp tiềm năng được xác định rõ ràng?
- ➔ Kiến trúc sư phần mềm không thể khai thác một tập hợp các giải pháp làm sẵn mà phải áp dụng kiến thức, thực tiễn và tính sáng tạo để đi đến giải pháp thỏa đáng.

# HỎI/ĐÁP

Question?
