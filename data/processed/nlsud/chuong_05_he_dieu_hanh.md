# Chương 5: Hệ điều hành

## Nội dung chính
- Bối cảnh ứng dụng công nghệ thông tin và phần mềm hiện nay.
- Khái niệm hệ điều hành và phần mềm hệ thống.
- Các chức năng chính của hệ điều hành: khởi động, quản lý CPU, tệp, tác vụ và bảo mật.
- Phần mềm hệ thống khác: trình điều khiển thiết bị và tiện ích.
- Giao diện người dùng, GUI, trợ giúp.
- Hệ điều hành Windows 10 và macOS.

## Tổng quan
Chương này giới thiệu hệ điều hành như thành phần chính của phần mềm hệ thống, đóng vai trò trung gian giữa người dùng, phần mềm ứng dụng và phần cứng. Người học cần nắm chức năng của hệ điều hành và cách các thành phần hệ thống hỗ trợ thiết bị số hoạt động.

## 1. Bối cảnh ứng dụng công nghệ thông tin

### Sự thay đổi của phần mềm và cách làm việc

**Khái niệm chính:**
- Công nghệ mới, phần mềm mới, điện thoại không dây và kết nối Internet tạo điều kiện biến ý tưởng thành hiện thực.
- Ứng dụng dựa trên đám mây làm thay đổi cách sử dụng phần mềm truyền thống.
- Người dùng ngày càng làm việc trên điện thoại thông minh, máy tính bảng và thiết bị di động.

**Giải thích:**
Trước đây phần mềm thường được cài đặt trực tiếp trên máy tính để bàn hoặc máy tính xách tay. Hiện nay nhiều ứng dụng được cung cấp qua đám mây, giúp cộng tác, truyền thông và xử lý tài liệu linh hoạt hơn.

**Ví dụ / ứng dụng:**
- Sử dụng ứng dụng văn phòng trực tuyến để viết tài liệu và cộng tác.
- Dùng phần mềm đám mây thay vì cài đặt toàn bộ trên máy cá nhân.

**Lưu ý:**
- Sự dịch chuyển sang đám mây không làm mất vai trò của hệ điều hành; hệ điều hành vẫn quản lý phần cứng, tệp và môi trường chạy ứng dụng.

## 2. Phần mềm ứng dụng và phần mềm hệ thống

### Phân biệt hai loại phần mềm

**Khái niệm chính:**
- Phần mềm ứng dụng giải quyết công việc cụ thể cho người dùng.
- Phần mềm hệ thống chạy ở mức cơ bản nhất của máy tính, cho phép phần mềm ứng dụng tương tác với phần cứng và tài nguyên.

**Giải thích:**
Người dùng thường làm việc trực tiếp với phần mềm ứng dụng, còn phần mềm ứng dụng phải thông qua phần mềm hệ thống để sử dụng phần cứng.

| Loại phần mềm | Vai trò | Ví dụ |
|---|---|---|
| Phần mềm ứng dụng | Thực hiện nhiệm vụ cụ thể cho người dùng | Soạn thảo văn bản, bảng tính, trình duyệt |
| Phần mềm hệ thống | Quản lý phần cứng, tài nguyên và môi trường chạy ứng dụng | Hệ điều hành, driver, tiện ích |

**Lưu ý:**
- Phần mềm hệ thống gồm hệ điều hành, trình điều khiển thiết bị và chương trình tiện ích.

## 3. Khái niệm hệ điều hành

### Định nghĩa hệ điều hành

**Khái niệm chính:**
- Hệ điều hành là thành phần chính của phần mềm hệ thống.
- Hệ điều hành là tập hợp các chương trình có nhiệm vụ đảm bảo tương tác giữa người dùng và máy tính, cung cấp phương tiện và dịch vụ để điều phối chương trình, quản lý tài nguyên và khai thác tài nguyên thuận tiện, tối ưu.

**Giải thích:**
Hệ điều hành giúp người dùng không phải điều khiển phần cứng trực tiếp. Nó quản lý bộ xử lý, bộ nhớ, tệp, thiết bị ngoại vi, bảo mật và giao diện tương tác.

**Ví dụ / ứng dụng:**
- Windows.
- macOS.
- Linux.
- MS-DOS.

**Lưu ý:**
- Hệ điều hành là nền tảng để phần mềm ứng dụng chạy được trên thiết bị.

### Một số hệ điều hành thông dụng

**Khái niệm chính:**
- MS-DOS: hệ điều hành giao diện dòng lệnh.
- Windows: hệ điều hành có giao diện đồ họa.
- macOS: hệ điều hành do Apple phát triển cho máy Macintosh.
- Linux: hệ điều hành và hạt nhân do Linus Torvalds khởi đầu, có nhiều bản phân phối.

**Giải thích:**
Các hệ điều hành khác nhau có giao diện, hệ sinh thái phần mềm và cách quản lý tài nguyên khác nhau nhưng đều phục vụ mục tiêu điều khiển phần cứng và hỗ trợ người dùng.

**Ví dụ / ứng dụng:**
- Ubuntu, Debian, Redhat, Fedora là các bản phân phối Linux.

**Lưu ý:**
- Người dùng nên chọn hệ điều hành phù hợp thiết bị, nhu cầu phần mềm và môi trường làm việc.

## 4. Các thành phần chính của hệ điều hành

### Kernel, Shell, Utilities và Applications

**Khái niệm chính:**
- Kernel là phần nhân, thực hiện chức năng cơ bản của hệ điều hành.
- Shell là giao diện giữa hệ thống và người dùng, gồm GUI và CLI.
- Utilities là các tiện ích cho người dùng.
- Applications là chương trình ứng dụng.

**Giải thích:**
Kernel quản lý lõi hệ thống; shell cho phép người dùng giao tiếp với hệ thống; tiện ích hỗ trợ bảo trì và quản lý; ứng dụng phục vụ công việc cụ thể.

| Thành phần | Vai trò |
|---|---|
| Kernel | Quản lý chức năng lõi của hệ điều hành |
| Shell | Giao tiếp giữa người dùng và hệ thống |
| GUI | Giao diện đồ họa |
| CLI | Giao diện dòng lệnh |
| Utilities | Tiện ích hỗ trợ quản lý và bảo trì |
| Applications | Chương trình ứng dụng |

**Lưu ý:**
- Người dùng thường thấy GUI, nhưng kernel là phần thực hiện nhiều chức năng quan trọng ở nền hệ thống.

## 5. Các chức năng chính của hệ điều hành

### Khởi động - Booting

**Khái niệm chính:**
- Booting là quá trình khởi động máy tính và nạp hệ điều hành vào bộ nhớ để sẵn sàng làm việc.

**Giải thích:**
Khi bật máy, hệ thống kiểm tra phần cứng, tìm hệ điều hành và nạp các thành phần cần thiết để người dùng có thể đăng nhập và chạy ứng dụng.

**Ví dụ / ứng dụng:**
- Khởi động máy tính Windows hoặc macOS.

**Lưu ý:**
- Lỗi khởi động có thể liên quan đến phần cứng, hệ điều hành hoặc thiết bị lưu trữ.

### Quản lý CPU - CPU Management

**Khái niệm chính:**
- Hệ điều hành điều phối việc sử dụng CPU cho các chương trình và tiến trình.

**Giải thích:**
Nhiều chương trình có thể cùng hoạt động, nhưng CPU phải được phân chia thời gian xử lý. Hệ điều hành quyết định tiến trình nào được chạy, tạm dừng hoặc ưu tiên.

**Ví dụ / ứng dụng:**
- Chạy trình duyệt, trình soạn thảo và phần mềm họp trực tuyến cùng lúc.

**Lưu ý:**
- Quản lý CPU ảnh hưởng trực tiếp đến tốc độ và độ ổn định của hệ thống.

### Quản lý tệp - File Management

**Khái niệm chính:**
- Hệ điều hành tổ chức, lưu trữ, truy xuất, sao chép, đổi tên và xóa tệp.

**Giải thích:**
Người dùng làm việc với thư mục và tệp qua giao diện hệ điều hành. Hệ điều hành quản lý vị trí lưu trữ và quyền truy cập tệp.

**Ví dụ / ứng dụng:**
- Tạo thư mục học tập.
- Sao chép tài liệu.
- Tìm kiếm tệp trong máy tính.

**Lưu ý:**
- Cần đặt tên và tổ chức tệp khoa học để dễ tìm lại.

### Quản lý tác vụ - Task Management

**Khái niệm chính:**
- Hệ điều hành quản lý các tác vụ, ứng dụng và tiến trình đang chạy.

**Giải thích:**
Chức năng này giúp người dùng theo dõi chương trình đang hoạt động, đóng chương trình bị treo hoặc kiểm tra mức sử dụng tài nguyên.

**Ví dụ / ứng dụng:**
- Task Manager trên Windows.

**Lưu ý:**
- Không nên đóng tiến trình hệ thống nếu không hiểu rõ vai trò của nó.

### Quản lý bảo mật - Security Management

**Khái niệm chính:**
- Hệ điều hành hỗ trợ đăng nhập, phân quyền, cập nhật bảo mật và bảo vệ tài nguyên hệ thống.

**Giải thích:**
Quản lý bảo mật giúp ngăn truy cập trái phép, bảo vệ tệp và đảm bảo chỉ người dùng có quyền mới thực hiện được thao tác nhất định.

**Ví dụ / ứng dụng:**
- Tài khoản người dùng.
- Mật khẩu đăng nhập.
- Quyền truy cập tệp.

**Lưu ý:**
- Cần cập nhật hệ điều hành và dùng mật khẩu mạnh để tăng an toàn.

## 6. Phần mềm hệ thống khác

### Trình điều khiển thiết bị - Device Drivers

**Khái niệm chính:**
- Driver là phần mềm giúp hệ điều hành giao tiếp với thiết bị phần cứng.

**Giải thích:**
Mỗi thiết bị như máy in, card mạng, card đồ họa cần driver phù hợp để hoạt động đúng.

**Ví dụ / ứng dụng:**
- Cài driver máy in để in tài liệu.

**Lưu ý:**
- Driver không phù hợp có thể làm thiết bị hoạt động lỗi hoặc không nhận thiết bị.

### Tiện ích - Utilities

**Khái niệm chính:**
- Utilities là chương trình hỗ trợ bảo trì, quản lý và tối ưu hệ thống.

**Giải thích:**
Tiện ích có thể giúp dọn dẹp tệp, nén dữ liệu, sao lưu, kiểm tra ổ đĩa hoặc bảo vệ hệ thống.

**Ví dụ / ứng dụng:**
- Công cụ sao lưu.
- Công cụ nén tệp.
- Công cụ kiểm tra ổ đĩa.

**Lưu ý:**
- Chỉ nên dùng tiện ích đáng tin cậy để tránh rủi ro bảo mật.

## 7. Giao diện người dùng

### GUI và Help

**Khái niệm chính:**
- GUI là giao diện đồ họa giúp người dùng thao tác bằng cửa sổ, biểu tượng, menu và con trỏ.
- Help là hệ thống trợ giúp hướng dẫn người dùng sử dụng chức năng.

**Giải thích:**
GUI làm máy tính dễ sử dụng hơn so với giao diện dòng lệnh. Tính năng Help giúp người dùng tìm hướng dẫn khi gặp vấn đề.

**Ví dụ / ứng dụng:**
- Start Menu trên Windows.
- Finder trên macOS.
- Hộp tìm kiếm trợ giúp trong phần mềm.

**Lưu ý:**
- Dù GUI thuận tiện, hiểu một số lệnh cơ bản vẫn hữu ích khi xử lý sự cố.

## 8. Windows 10 và macOS

### Windows 10

**Khái niệm chính:**
- Windows 10 là hệ điều hành phổ biến với giao diện đồ họa, hỗ trợ nhiều ứng dụng và thiết bị.

**Giải thích:**
Windows 10 cung cấp môi trường làm việc quen thuộc cho người dùng cá nhân, học tập và doanh nghiệp.

**Ví dụ / ứng dụng:**
- Quản lý tệp bằng File Explorer.
- Quản lý ứng dụng và thiết bị ngoại vi.

**Lưu ý:**
- Cần cập nhật Windows và phần mềm bảo mật thường xuyên.

### macOS

**Khái niệm chính:**
- macOS là hệ điều hành do Apple phát triển cho máy tính Apple.

**Giải thích:**
macOS tích hợp chặt chẽ với hệ sinh thái thiết bị và phần mềm của Apple, hỗ trợ giao diện đồ họa và nhiều công cụ sáng tạo.

**Ví dụ / ứng dụng:**
- Quản lý tệp bằng Finder.
- Làm việc với các ứng dụng trong hệ sinh thái Apple.

**Lưu ý:**
- Người dùng cần chọn hệ điều hành phù hợp với thiết bị và phần mềm cần dùng.

## Tóm tắt chương
- Hệ điều hành là thành phần chính của phần mềm hệ thống.
- Hệ điều hành quản lý phần cứng, CPU, tệp, tác vụ, bảo mật và giao diện người dùng.
- Phần mềm hệ thống gồm hệ điều hành, driver và tiện ích.
- GUI giúp người dùng thao tác dễ hơn; CLI vẫn có vai trò trong quản trị và xử lý kỹ thuật.
- Windows 10 và macOS là các hệ điều hành phổ biến.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Hệ điều hành | Phần mềm hệ thống quản lý tài nguyên và điều phối hoạt động của máy tính. |
| Kernel | Nhân hệ điều hành, thực hiện chức năng lõi. |
| Shell | Giao diện giúp người dùng tương tác với hệ thống. |
| GUI | Giao diện đồ họa người dùng. |
| CLI | Giao diện dòng lệnh. |
| Device Driver | Trình điều khiển giúp hệ điều hành làm việc với thiết bị phần cứng. |
| Utility | Tiện ích hỗ trợ quản lý, bảo trì hoặc tối ưu hệ thống. |
| Booting | Quá trình khởi động và nạp hệ điều hành. |

## Câu hỏi ôn tập
1. Phân biệt phần mềm ứng dụng và phần mềm hệ thống.
2. Hệ điều hành là gì?
3. Kernel và Shell có vai trò gì?
4. Trình bày các chức năng chính của hệ điều hành.
5. Booting là gì?
6. Vì sao hệ điều hành cần quản lý CPU?
7. Driver dùng để làm gì?
8. GUI khác CLI ở điểm nào?
9. Nêu ví dụ về hệ điều hành thông dụng.
