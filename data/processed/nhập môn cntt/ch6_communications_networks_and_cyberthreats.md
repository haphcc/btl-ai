# Chapter 6: Communications, Networks, & Cyberthreats

## Nội dung chính
- Chuyển từ thời đại tương tự (Analog) sang thời đại số (Digital).
- Digital convergence và vai trò của mạng máy tính (Network).
- Các loại mạng và thành phần mạng cơ bản.
- Phương tiện truyền thông có dây và không dây.
- Cyberintruders, cyberattacks, malware.
- Quyền riêng tư (Privacy) và đánh cắp danh tính (Identity Theft).

## Tổng quan
Chương này trình bày cách dữ liệu được truyền qua mạng và các rủi ro an ninh mạng. Nội dung giải thích sự hội tụ số, các loại mạng, phương tiện truyền dữ liệu có dây và không dây, đồng thời giới thiệu các nhóm kẻ xâm nhập mạng, tấn công mạng, phần mềm độc hại và vấn đề quyền riêng tư.

## Unit 6A: Communications, Networks, & Media

### 6.1 From the Analog to the Digital Age

**Khái niệm chính:**
- Analog biểu diễn thông tin liên tục.
- Digital biểu diễn thông tin bằng số, thường là 0 và 1.
- Digital convergence là xu hướng nhiều công nghệ hợp nhất trên nền tảng số.

**Giải thích:**
Trong thời đại số, dữ liệu văn bản, âm thanh, hình ảnh và video đều có thể được mã hóa thành dữ liệu số. Điều này cho phép các thiết bị và dịch vụ khác nhau kết nối, trao đổi và xử lý thông tin dễ hơn.

**Thuật ngữ cần nhớ:**
- `Analog`: dạng tín hiệu liên tục.
- `Digital`: dạng dữ liệu số.
- `Digital convergence`: hội tụ số, nhiều công nghệ hợp nhất trên nền số.

**Ví dụ / ứng dụng:**
- Smartphone tích hợp điện thoại, máy ảnh, máy nghe nhạc, bản đồ và truy cập Internet trong một thiết bị.

### 6.2 Networks

**Khái niệm chính:**
- Mạng máy tính (Network) là hệ thống kết nối các máy tính và thiết bị để chia sẻ dữ liệu, tài nguyên và dịch vụ.
- Mạng có thể phân loại theo phạm vi như LAN, MAN, WAN.
- Mạng cần phần cứng, phần mềm, giao thức và phương tiện truyền dẫn.

**Giải thích:**
Mạng giúp nhiều thiết bị giao tiếp với nhau. Trong gia đình, mạng có thể kết nối laptop, điện thoại, TV và máy in. Trong tổ chức, mạng kết nối máy trạm, server, thiết bị lưu trữ và Internet.

| Loại mạng | Mô tả |
|---|---|
| `LAN` | Local Area Network, mạng cục bộ trong phạm vi nhỏ |
| `MAN` | Metropolitan Area Network, mạng đô thị |
| `WAN` | Wide Area Network, mạng diện rộng |
| `PAN` | Personal Area Network, mạng cá nhân |

**Thuật ngữ cần nhớ:**
- `Network`: mạng máy tính.
- `Node`: thiết bị tham gia mạng.
- `Router`: thiết bị định tuyến dữ liệu.
- `Switch`: thiết bị kết nối các node trong mạng.
- `Protocol`: quy tắc truyền thông.

**Ví dụ / ứng dụng:**
- Mạng LAN trong phòng máy giúp các máy tính dùng chung máy in và truy cập server.

### 6.3 Wired Communications Media

**Khái niệm chính:**
- Phương tiện truyền thông có dây dùng cáp vật lý để truyền dữ liệu.
- Các loại thường gặp gồm twisted-pair wire, coaxial cable và fiber-optic cable.

**Giải thích:**
Kết nối có dây thường ổn định và bảo mật hơn kết nối không dây. Cáp xoắn đôi được dùng nhiều trong điện thoại và Ethernet. Cáp đồng trục dùng trong truyền hình cáp. Cáp quang truyền dữ liệu bằng ánh sáng, tốc độ cao và ít nhiễu.

| Phương tiện | Đặc điểm |
|---|---|
| `Twisted-pair wire` | Cáp xoắn đôi, phổ biến trong mạng và điện thoại |
| `Coaxial cable` | Cáp đồng trục, dùng trong truyền hình cáp |
| `Fiber-optic cable` | Cáp quang, truyền bằng ánh sáng, tốc độ cao |

**Thuật ngữ cần nhớ:**
- `Wired media`: phương tiện truyền có dây.
- `Fiber optics`: công nghệ truyền dữ liệu bằng sợi quang.
- `Bandwidth`: băng thông.

**Ví dụ / ứng dụng:**
- Kết nối Internet cáp quang trong gia đình dùng fiber-optic network của nhà cung cấp dịch vụ.

### 6.4 Wireless Communications Media

**Khái niệm chính:**
- Truyền thông không dây dùng sóng điện từ thay vì cáp vật lý.
- Các công nghệ gồm microwave, satellite, infrared, Bluetooth, Wi-Fi và mạng di động.
- Wi-Fi là nhóm chuẩn không dây 802.11.

**Giải thích:**
Không dây giúp thiết bị di chuyển linh hoạt, nhưng có thể bị ảnh hưởng bởi khoảng cách, vật cản, nhiễu và bảo mật. Wi-Fi phổ biến trong gia đình, trường học và nơi công cộng. Bluetooth phù hợp kết nối phạm vi ngắn. Mạng di động phục vụ thiết bị di chuyển ở phạm vi rộng.

| Công nghệ | Ứng dụng |
|---|---|
| `Wi-Fi` | Mạng không dây nội bộ dựa trên 802.11 |
| `Bluetooth` | Kết nối tầm ngắn giữa thiết bị |
| `Satellite` | Truyền dữ liệu qua vệ tinh |
| `Cellular network` | Mạng di động |
| `Infrared` | Truyền dữ liệu bằng tia hồng ngoại |

**Thuật ngữ cần nhớ:**
- `Wireless media`: phương tiện truyền không dây.
- `Wi-Fi`: mạng không dây theo chuẩn 802.11.
- `Bluetooth`: kết nối không dây tầm ngắn.
- `Cellular`: mạng di động.

**Ví dụ / ứng dụng:**
- Tai nghe Bluetooth kết nối với điện thoại.
- Laptop truy cập Internet qua Wi-Fi.

## Unit 6B: Cyberthreats: Intruders, Attacks, Malware & Privacy

### 6.5 Cyberintruders

**Khái niệm chính:**
- Cyberintruders là những người hoặc nhóm xâm nhập hệ thống máy tính.
- Các nhóm có thể gồm hacker, cracker, script kiddie, insider hoặc cybercriminal.
- Mục đích có thể là tò mò, phá hoại, trộm dữ liệu hoặc kiếm tiền.

**Giải thích:**
Không phải mọi người xâm nhập hệ thống đều có cùng mục đích. Một số thử nghiệm kỹ thuật, một số phá hoại hoặc đánh cắp thông tin. Người trong nội bộ cũng có thể trở thành mối đe dọa nếu lạm dụng quyền truy cập.

**Thuật ngữ cần nhớ:**
- `Hacker`: người có kỹ năng kỹ thuật cao, tùy ngữ cảnh có thể tốt hoặc xấu.
- `Cracker`: người phá hoại hoặc xâm nhập trái phép.
- `Insider`: người trong tổ chức gây rủi ro.
- `Cybercriminal`: tội phạm mạng.

**Ví dụ / ứng dụng:**
- Nhân viên sử dụng quyền truy cập để lấy dữ liệu khách hàng trái phép là insider threat.

### 6.6 Cyberattacks & Malware

**Khái niệm chính:**
- Cyberattack là hành vi tấn công hệ thống, mạng hoặc dữ liệu.
- Malware là phần mềm độc hại.
- Các dạng malware gồm virus, worm, Trojan horse, spyware, ransomware.

**Giải thích:**
Tấn công mạng có thể làm gián đoạn dịch vụ, đánh cắp dữ liệu, phá hủy file hoặc chiếm quyền hệ thống. Malware có thể lây qua email, website, file tải về hoặc thiết bị lưu trữ.

| Mối đe dọa | Giải thích |
|---|---|
| `Virus` | Mã độc gắn vào file hoặc chương trình |
| `Worm` | Mã độc tự lan truyền qua mạng |
| `Trojan horse` | Chương trình giả có ích nhưng chứa mã độc |
| `Spyware` | Theo dõi hoạt động người dùng |
| `Ransomware` | Mã hóa dữ liệu và đòi tiền chuộc |
| `Denial-of-service` | Làm dịch vụ không thể phục vụ người dùng |

**Thuật ngữ cần nhớ:**
- `Cyberattack`: tấn công mạng.
- `Malware`: phần mềm độc hại.
- `Firewall`: tường lửa kiểm soát lưu lượng mạng.
- `Antivirus`: phần mềm chống mã độc.

**Ví dụ / ứng dụng:**
- Email đính kèm file lạ có thể chứa Trojan.
- Tấn công từ chối dịch vụ làm website không truy cập được.

### 6.7 Concerns about Privacy & Identity Theft

**Khái niệm chính:**
- Privacy là quyền riêng tư khi dữ liệu cá nhân được thu thập, lưu trữ và sử dụng.
- Identity theft là đánh cắp danh tính để giả mạo người khác.
- Người dùng cần bảo vệ thông tin cá nhân và tài khoản.

**Giải thích:**
Khi sử dụng mạng, người dùng có thể để lộ tên, email, địa chỉ, tài khoản, lịch sử mua hàng hoặc vị trí. Nếu dữ liệu này bị lạm dụng, kẻ xấu có thể giả mạo danh tính, mở tài khoản, mua hàng hoặc truy cập dịch vụ trái phép.

**Thuật ngữ cần nhớ:**
- `Privacy`: quyền riêng tư.
- `Identity theft`: đánh cắp danh tính.
- `Personal information`: thông tin cá nhân.
- `Authentication`: xác thực người dùng.

**Ví dụ / ứng dụng:**
- Dùng mật khẩu mạnh, không dùng lại mật khẩu và cảnh giác với email lừa đảo giúp giảm nguy cơ mất tài khoản.

## Tóm tắt chương
- Thời đại số biến nhiều loại thông tin thành dữ liệu số.
- Digital convergence làm nhiều công nghệ hội tụ trong cùng thiết bị hoặc dịch vụ.
- Network cho phép thiết bị chia sẻ dữ liệu và tài nguyên.
- Truyền thông có dây ổn định; truyền thông không dây linh hoạt.
- Cyberintruders và malware gây rủi ro cho hệ thống và dữ liệu.
- Privacy và identity theft là vấn đề quan trọng khi dùng Internet.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| Analog | Tín hiệu liên tục |
| Digital | Dữ liệu số |
| Digital Convergence | Hội tụ số |
| Network | Mạng máy tính |
| LAN | Mạng cục bộ |
| WAN | Mạng diện rộng |
| Wi-Fi | Mạng không dây theo chuẩn 802.11 |
| Bluetooth | Kết nối không dây tầm ngắn |
| Cyberintruder | Người xâm nhập hệ thống |
| Malware | Phần mềm độc hại |
| Firewall | Tường lửa |
| Identity Theft | Đánh cắp danh tính |

## Câu hỏi ôn tập
1. Analog và digital khác nhau như thế nào?
2. Digital convergence là gì?
3. Mạng máy tính giúp ích gì cho tổ chức?
4. LAN và WAN khác nhau thế nào?
5. So sánh wired media và wireless media.
6. Wi-Fi và Bluetooth khác nhau ở phạm vi sử dụng nào?
7. Cyberintruder là gì?
8. Nêu ba loại malware và tác hại của chúng.
9. Identity theft là gì và vì sao nguy hiểm?
