# Chương 12-Phát triển hệ thống thông tin



<!-- page 1 -->

# **HỆ THỐNG THÔNG TIN QUẢN LÝ**
## Phát triển Hệ thống thông tin


<!-- page 2 -->

# TÌNH HUỐNG KHỞI ĐỘNG

**Bối cảnh:**
- Ares đang thảo luận về kế hoạch phát triển ARES.

**Nội dung thảo luận:**
- Sẽ tốn khoảng 200.000 đến 300.000 USD để tạo ra ứng dụng tích hợp ARES với 10 nhà sản xuất xe đạp hàng đầu, do các nhà sản xuất xe đạp đã có sẵn nền tảng hệ thống riêng của họ.
- Sau đó, cần phát triển ứng dụng cho tai nghe thực tế ảo với chi phí từ 100.000 đến 250.000 USD.

**Vấn đề:**
- Kế hoạch phát triển ARES như thế nào để tối thiểu hóa rủi ro với chi phí sản xuất thấp nhất ?


<!-- page 3 -->

# MỤC TIÊU BÀI HỌC

- Nắm được các giai đoạn trong vòng đời phát triển hệ thống thông tin trong doanh nghiệp
- Các mô hình phát triển hệ thống thông tin
- Mô phỏng và đánh giá được hiệu suất của quy trình


<!-- page 4 -->

# NỘI DUNG

- **12.1** Tổng quan về phát triển Hệ thống thông tin
- **12.2** Các giai đoạn trong vòng đời phát triển HTTT
- **12.3** Các mô hình phát triển HTTT
- **12.4** Mô phỏng quy trình HTTT với phần mềm bizagi


<!-- page 5 -->

# Tổng quan về phát triển Hệ thống thông tin?

- Nếu bạn là lãnh đạo bạn sẽ tham gia vào việc phát triển các ứng dụng công nghệ mới cho doanh nghiệp.
- Nếu bạn là nhân viên bạn sẽ là người thực hiện các quy trình và có thể đề xuất các thay đổi, cải tiến cho quy trình.
- Bạn có thể trở thành nhà phân tích nghiệp vụ và làm việc như một người liên lạc giữa người dùng và nhân viên kỹ thuật.
- Hoặc bạn có thể được cung cấp các yêu cầu và kiểm tra hệ thống để đảm bảo các yêu cầu đó được đáp ứng


<!-- page 6 -->

# Mối quan hệ giữa Quy trình nghiệp vụ, Hệ thống thông tin và Ứng dụng

- **Quy trình nghiệp vụ** bao gồm một hoặc nhiều hoạt động có liên quan với nhau, được thực hiện theo một trình tự nhất định nhằm đạt được một mục tiêu kinh doanh cụ thể.

## Sơ đồ quy trình

- **Business Process** (Quy trình nghiệp vụ):
    - Prepare Quotation
    - Verify Availability
    - Check Customer Credit
    - Approve Special Terms
    - Process Order

- **Information Systems** (Hệ thống thông tin):
    - CRM
    - Inventory IS
    - Customer Credit IS
    - Shipping IS

*Ghi chú: Các thành phần trong Business Process và Information Systems tương tác với nhau theo từng bước từ Prepare Quotation đến Process Order, kết nối giữa Customers và Orders.*


<!-- page 7 -->

# Mối quan hệ giữa Quy trình nghiệp vụ, Hệ thống thông tin và Ứng dụng

- Hệ thống thông tin là công cụ giúp số hóa quy trình nghiệp vụ. HTTT biến các quy trình nghiệp vụ thủ công, giấy tờ... thành quy trình điện tử, tự động và có thể quản lý được bằng công nghệ.

+ Một quy trình nghiệp vụ có thể sử dụng nhiều HTTT và một HTTT có thể hỗ trợ nhiều quy trình nghiệp vụ. Một quy trình nghiệp vụ không bắt buộc phải sử dụng HTTT nhưng mọi HTTT đều hỗ trợ ít nhất một quy trình nghiệp vụ.

| Business Process | | Information System |
| :--- | :---: | :--- |
| | ⊣—o | |


<!-- page 8 -->

# Mối quan hệ giữa Quy trình nghiệp vụ, Hệ thống thông tin và Ứng dụng

- **Ứng dụng** là một phần mềm được thiết kế để người dùng sử dụng **HTTT** nhằm thực hiện một hoặc nhiều chức năng cụ thể.


<!-- page 9 -->

# Phát triển HTTT là gì?

- Phát triển HTTT là quá trình phân tích, thiết kế, xây dựng, kiểm thử và triển khai một hệ thống thông tin nhằm hỗ trợ cho các hoạt động nghiệp vụ trong tổ chức hoặc doanh nghiệp.


<!-- page 10 -->

# Các giai đoạn trong vòng đời phát triển HTTT?

- **Phát triển HTTT** là tập hợp các giai đoạn được thực hiện tuần tự để xây dựng và triển khai một hệ thống thông tin hoàn chỉnh, từ bước khởi động đến khi vận hành và nâng cấp.
- Nhiều dự án đã bị thất bại khi không có hoặc không tuân thủ các giai đoạn trong vòng đời phát triển HTTT.
- Vòng đời phát triển HTTT không chỉ là quy trình kỹ thuật, mà còn giữ vai trò định hướng toàn bộ quá trình xây dựng và vận hành hệ thống:
    - Đảm bảo hệ thống phù hợp với nhu cầu thực tế
    - Tổ chức công việc có hệ thống, rõ ràng
    - Giảm rủi ro & phát hiện lỗi sớm
    - Tiết kiệm chi phí & thời gian triển khai
    - Hỗ trợ bảo trì & nâng cấp dễ dàng
    - Tạo cầu nối giữa kỹ thuật và nghiệp vụ


<!-- page 11 -->

# Các giai đoạn trong vòng đời phát triển HTTT?

1. Xác định hệ thống
2. Xác định và phân tích yêu cầu người dùng
3. Thiết kế hệ thống
4. Triển khai hệ thống
5. Bảo trì hệ thống


<!-- page 12 -->

# 1. Xác định hệ thống

Là bước quan trọng để tìm hiểu mục tiêu và phạm vi của hệ thống. Bao gồm các nội dung sau:

- Hiểu rõ mục tiêu của hệ thống: Hệ thống được tạo ra để giải quyết vấn đề gì? Phục vụ cho ai ví dụ người dùng, khách hàng, doanh nghiệp...
- Xác định phạm vi (scope) của hệ thống: Hệ thống gồm những phần nào? Giới hạn của hệ thống là gì? Những gì nằm ngoài phạm vi?
- Đánh giá tính khả thi
- Thành lập nhóm dự án

12


<!-- page 13 -->

# 1. Xác định hệ thống

Đánh giá **tính khả thi**:

- Khi chúng ta đã xác định được mục tiêu và phạm vi của dự án, bước tiếp theo là đánh giá **tính khả thi**.
- Bước này trả lời câu hỏi “Dự án này có ý nghĩa không?” Mục đích ở đây là loại bỏ các dự án không có ý nghĩa trước khi thành lập nhóm phát triển dự án và đầu tư kinh phí.
- **Tính khả thi** có bốn khía cạnh: chi phí, tiến độ, kỹ thuật và tổ chức.


<!-- page 14 -->

# 1. Xác định hệ thống

Thành lập nhóm dự án:

- Bao gồm chuyên gia IS và đại diện người dùng. Cụ thể: Người quản lý; Nhà phân tích nghiệp vụ; Nhà phân tích hệ thống; Lập trình viên; Người kiểm tra phần mềm và người dùng.
- Thành phần của đội thay đổi theo thời gian.
- Sự tham gia của người dùng là rất quan trọng trong suốt quá trình phát triển hệ thống.
- Nhiệm vụ chính đầu tiên của nhóm tập hợp là lập kế hoạch cho dự án.


<!-- page 15 -->

## 2. Xác định và phân tích yêu cầu người dùng

Là giai đoạn quan trọng nhất trong quy trình phát triển hệ thống thông tin. Bao gồm các nội dung sau:

- Phỏng vấn người dùng
- Đánh giá hệ thống hiện có
- Nhận diện các ứng dụng, chức năng mới
- Phân tích giao diện và dữ liệu của hệ thống
- Xem xét đủ các khía cạnh về 5 thành phần của HTTT.


<!-- page 16 -->

## 2. Xác định và phân tích yêu cầu người dùng

Khi xác định yêu cầu người dùng, một dạng phổ biến là thể hiện các yêu cầu dưới dạng câu hỏi ai làm gì và tại sao.

Ví dụ: trong phiên bản hệ thống ARES dành cho bác sĩ, một yêu cầu được thể hiện như sau:

- "Là một bác sĩ, tôi muốn xem hồ sơ tập luyện của bệnh nhân để có thể chắc chắn rằng anh ta không tập quá nhiều"
- Hoặc "Là một bác sĩ, tôi muốn xem hồ sơ tập luyện của bệnh nhân để có thể chắc chắn rằng cô ấy đang làm theo đơn thuốc của mình"


<!-- page 17 -->

## 3. Thiết kế hệ thống

Thiết kế hệ thống giống như bản vẽ kiến trúc của một tòa nhà với nhiệm vụ thiết kế liên quan đến từng thành phần trong năm thành phần của hệ thống thông tin.

- Đối với **phần cứng** nhóm xác định các thông số kỹ thuật mà hệ thống sẽ cần.
- Đối với **phần mềm** nếu có sẵn nhóm xác định sự phù hợp và xác định các thay đổi cần thiết; nếu cần xây dựng mới nhóm tạo tài liệu thiết kế để viết mã lệnh chương trình.
- Đối với **dữ liệu** nhóm thiết kế cơ sở dữ liệu để đảm bảo dữ liệu của hệ thống sẽ được quản lý chính xác và chuẩn hóa.
- Các **quy trình kinh doanh** của doanh nghiệp thường được xác định, phân tích và chuẩn hóa từ trước, giai đoạn thiết kế giúp số hóa quy trình bằng cách xây dựng các ứng dụng để người dùng sử dụng.
- Đối với **con người**, thiết kế liên quan đến việc phát triển các bản mô tả công việc cho các vai trò khác nhau.


<!-- page 18 -->

## 4. Triển khai hệ thống

Nhiệm vụ trong giai đoạn triển khai là xây dựng và kiểm thử các thành phần hệ thống và chuyển đổi người dùng sang hệ thống mới.

- **Kiểm thử** là hoạt động quan trọng bao gồm việc tạo ra các kịch bản chạy chương trình với các tập dữ liệu khác nhau để tìm ra các lỗi sai và khắc phục. Mục đích đảm bảo tính chính xác của hệ thống khi đến tay người dùng.
- Sau khi hệ thống đã vượt qua quá trình kiểm thử, hệ thống sẽ được cài đặt trên môi trường của người dùng; Có 4 hình thức triển khai gồm: Thí điểm, Theo từng giai đoạn, Song song và Trực tiếp.


<!-- page 19 -->

## 4. Triển khai hệ thống

- **Thí điểm**: Phương pháp này chỉ khởi động hệ thống mới cho một bộ phận cụ thể sử dụng chứ không phải tất cả bộ phận trong tổ chức. Ưu điểm là nếu hệ thống bị lỗi thì lỗi đó chỉ ảnh hưởng trong một giới hạn nhỏ và dễ dàng khắc phục hơn.
- **Theo từng giai đoạn**: Theo phương pháp này các thành phần của hệ thống mới được đưa vào hoạt động từ từ theo từng giai đoạn cho đến khi hệ thống mới ổn định thì hệ thống cũ sẽ bị loại bỏ hoàn toàn.
- **Song song**: hệ thống mới chạy song song với hệ thống cũ cho đến khi hệ thống mới được thử nghiệm và vận hành đầy đủ. Việc cài đặt song song rất tốn kém vì tổ chức phải chịu chi phí vận hành cả hai hệ thống.
- **Trực tiếp**: Phương pháp này thay thế hoàn toàn hệ thống cũ bằng hệ thống mới, tuy nhiên điều này sẽ gây ra những rủi ro nhất định nếu hệ thống mới vận hành không được thuận lợi.


<!-- page 20 -->

## 5. Bảo trì hệ thống

- **Bảo trì** là giai đoạn cuối cùng của chu kỳ phát triển hệ thống, liên quan tới các hoạt động kiểm tra, chỉnh sửa và nâng cấp hệ thống sau khi đã được đưa vào sử dụng nhằm tăng cường tính hiệu quả của hệ thống đối với các mục tiêu của tổ chức.
- Chi phí bảo trì phần mềm có thể chiếm khoảng 20% giá trị của phần mềm và là một phần tất yếu để vận hành hệ thống luôn phù hợp với người sử dụng.


<!-- page 21 -->

# Các mô hình phát triển HTTT

- Mô hình phát triển HTTT được định nghĩa như một tập hợp các bước cần phải thực hiện và các công cụ hỗ trợ, cho phép việc phát triển HTTT được tiến hành một cách chặt chẽ và hiệu quả.
- Các mô hình phát triển HTTT khác nhau sẽ có nội dung thực hiện và công cụ hỗ trợ khác nhau nhưng phải tuân thủ theo nội dung các pha trong vòng đời phát triển hệ thống thông tin.

21


<!-- page 22 -->

# Các mô hình phát triển HTTT

**Mô hình thác nước – waterfall**: là mô hình phát triển hệ thống tuần tự, kết thúc pha trước rồi mới được thực hiện pha tiếp theo.

- **Ưu điểm**: Phản ánh công nghệ theo lối tư duy tự nhiên, đơn giản, dễ hiểu, dễ thực hiện. Trình tự thực hiện rõ ràng, thích hợp với các hệ thống vừa và nhỏ với các yêu cầu đã được tìm hiểu rõ ràng và ít thay đổi.
- **Nhược điểm**: Gặp khó khăn khi có thay đổi xảy ra trong quá trình phát triển hệ thống. Sự tham gia của người dùng trong quá trình phát triển bị giới hạn (chỉ tham gia trong giai đoạn xác định yêu cầu).


<!-- page 23 -->

# Các mô hình phát triển HTTT

**Phương pháp làm bản mẫu–Prototyping**: dùng các công cụ phần mềm tự động hóa các bước trong vòng đời phát triển hệ thống để xây dựng bản mẫu.

- Các bước thực hiện như sau: Xác định các yêu cầu cơ bản của hệ thống và xây dựng một nguyên mẫu dựa trên các yêu cầu đó. Khách hàng dùng thử và đánh giá nguyên mẫu. Tinh chỉnh nguyên mẫu qua nhiều phiên bản cho đến khi thỏa mãn các yêu cầu của người dùng.
- Ưu điểm: Cải thiện mối liên hệ giữa người dùng và đội phát triển phần mềm, cho phép người dùng sớm hình dung về chức năng và đặc điểm của hệ thống; Giảm thiểu rủi ro; Phù hợp với các hệ thống lớn.
- Nhược điểm: Cần phải có các công cụ và ngôn ngữ đặc biệt dành cho việc tạo bản mẫu.


<!-- page 24 -->

# Các mô hình phát triển HTTT

**Phương pháp phát triển linh hoạt-Agile**: cùng nhóm với các phương pháp và phương pháp luận phát triển ứng dụng dựa trên nguyên tắc phát triển phân đoạn lặp (iterative) và tăng trưởng (incremental).

- Agile cố gắng cực tiểu hóa rủi ro bằng cách phát triển ứng dụng trong các khung thời gian ngắn, gọi là các bước lặp, mỗi bước lặp từ 1 đến 4 tuần để có thể dễ dàng phản hồi lại với các thay đổi trong quá trình phát triển.
- Agile nhấn mạnh vào tầm quan trọng của giao tiếp thời gian thực, giao tiếp trực tiếp mặt-đối-mặt với tất cả các thành viên trong đội phát triển ứng dụng bao gồm cả khách hàng.
    + Nhóm họp hàng ngày trong 15 phút: Việc tôi đã làm ngày hôm qua; Hôm nay tôi sẽ làm gì; Tôi đang gặp những khó khăn gì
- Agile là một cách tiếp cận tốt khi không biết trước hoàn toàn các yêu cầu của hệ thống đang cần xây dựng hoặc sửa chữa.


<!-- page 25 -->

# GIẢI QUYẾT TÌNH HUỐNG

**Làm thế nào để tối thiểu hóa rủi ro với chi phí sản xuất ARES thấp nhất?**

**Giải pháp thực hiện:**
Phân tích và xác định mô hình phát triển HTTT phù hợp.
- Mô hình bản mẫu


<!-- page 26 -->

# THỰC HÀNH MÔ PHỎNG QUY TRÌNH HỆ THỐNG THÔNG TIN

Sinh viên thực hành Thực hiện mô phỏng quy trình nghiệp vụ trên phần mềm Bizagi tại Sách bài tập thực hành
