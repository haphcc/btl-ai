# Chương 3: Mạng cục bộ LAN

## Nội dung chính
- Khái niệm và đặc trưng của mạng LAN.
- Chia sẻ tài nguyên trong LAN.
- Các chuẩn và công nghệ LAN như Ethernet, FDDI, IEEE 802.
- Các topo mạng LAN: star, ring, bus, mesh và kết hợp.
- Ưu điểm, nhược điểm của từng hình trạng mạng.

## Tổng quan
Mạng cục bộ LAN (`Local Area Network`) kết nối các máy tính trong phạm vi nhỏ như phòng, tòa nhà hoặc cơ quan. Chương này trình bày đặc trưng LAN, các kỹ thuật phổ biến và các dạng topology thường gặp khi thiết kế mạng cục bộ.

## Khái niệm mạng LAN

### LAN là gì

**Khái niệm chính:**
- LAN là mạng kết nối máy tính trong phạm vi địa lý nhỏ.
- LAN cho phép chia sẻ dữ liệu, máy in, máy quét và thiết bị ngoại vi.
- LAN thường thuộc sở hữu của một tổ chức hoặc cá nhân.

**Giải thích:**
LAN được dùng rộng rãi trong văn phòng, trường học, phòng máy và doanh nghiệp. Do phạm vi nhỏ, LAN thường có tốc độ cao và tỷ lệ lỗi thấp hơn mạng diện rộng.

### Đặc trưng LAN

**Khái niệm chính:**
- Quy mô nhỏ, bán kính thường dưới vài km.
- Kết nối từ hai đến hàng trăm máy tính.
- Dùng cáp mạng hoặc truyền vô tuyến.
- Tốc độ cao, ít lỗi.
- Tuân theo các chuẩn IEEE 802.

**Ví dụ / Minh họa:**
- Ethernet 10 Mbps.
- Fast Ethernet 100 Mbps.
- Gigabit Ethernet.

## Công nghệ mạng cục bộ

### Ethernet và FDDI

**Khái niệm chính:**
- Ethernet là công nghệ LAN phổ biến, thuộc họ chuẩn IEEE 802.3.
- FDDI là công nghệ mạng vòng dùng cáp quang trong một số hệ thống tốc độ cao trước đây.

**Lưu ý:**
- Ethernet hiện là công nghệ LAN chủ đạo nhờ chi phí hợp lý, dễ triển khai và dễ mở rộng.

## Topology mạng LAN

### Mạng hình sao

**Mô hình / Quy trình / Cấu trúc:**
- Các máy trạm nối về thiết bị trung tâm như Hub hoặc Switch.
- Dữ liệu đi qua thiết bị trung tâm trước khi đến máy đích.
- Các chuẩn như 10BASE-T và 100BASE-T thường triển khai theo dạng sao vật lý.

**Ưu điểm:**
- Dễ lắp đặt, quản lý và mở rộng.
- Một đường nối hỏng thường chỉ ảnh hưởng đến một máy.

**Nhược điểm:**
- Thiết bị trung tâm là điểm lỗi quan trọng.
- Chi phí cáp và thiết bị trung tâm cao hơn bus trong một số trường hợp.

### Mạng dạng vòng

**Mô hình / Quy trình / Cấu trúc:**
- Các trạm nối thành vòng.
- Dữ liệu đi qua các trạm theo một chiều hoặc theo cơ chế vòng.
- Gói dữ liệu mang địa chỉ trạm đích; repeater có thể dùng để khuếch đại tín hiệu.

**Ưu điểm:**
- Truy cập đường truyền có thể được tổ chức trật tự.
- Phù hợp với một số công nghệ dùng token.

**Nhược điểm:**
- Sự cố trên vòng có thể ảnh hưởng nhiều trạm nếu không có vòng dự phòng.
- Khó mở rộng hơn mạng hình sao.

### Mạng hình tuyến

**Mô hình / Quy trình / Cấu trúc:**
- Các máy nối vào một đường cáp chính.
- Hai đầu cáp thường cần terminator để tránh phản xạ tín hiệu.

**Ưu điểm:**
- Cấu trúc đơn giản.
- Tiết kiệm cáp trong mạng nhỏ.

**Nhược điểm:**
- Khó xác định lỗi.
- Đứt cáp chính có thể làm gián đoạn toàn mạng.
- Khả năng mở rộng hạn chế.

### Mạng hình lưới

**Mô hình / Quy trình / Cấu trúc:**
- Các nút có nhiều liên kết trực tiếp với nhau.
- Có thể là lưới đầy đủ hoặc lưới một phần.

**Ưu điểm:**
- Độ tin cậy cao do có nhiều đường thay thế.

**Nhược điểm:**
- Chi phí kết nối lớn.
- Quản lý phức tạp khi số nút tăng.

### Mạng kết hợp

**Khái niệm chính:**
- Kết hợp nhiều topology để phù hợp với thực tế triển khai.
- Ví dụ: star/bus, nhiều mạng sao kết nối qua một trục chính.

## Quản lý và thiết kế LAN

### Các yếu tố cần chú ý

**Khái niệm chính:**
- Nhu cầu chia sẻ tài nguyên.
- Số lượng máy và phạm vi triển khai.
- Tốc độ yêu cầu.
- Thiết bị trung tâm, cáp mạng hoặc kết nối không dây.
- Khả năng mở rộng và bảo trì.

**Lưu ý:**
- Thiết kế LAN cần cân bằng giữa chi phí, hiệu năng, độ tin cậy và khả năng quản lý.

## Tóm tắt chương
- LAN là mạng phạm vi nhỏ, tốc độ cao và thường thuộc một tổ chức.
- LAN dùng để chia sẻ dữ liệu, thiết bị và dịch vụ.
- Ethernet là công nghệ LAN phổ biến.
- Các topology chính gồm star, ring, bus, mesh và dạng kết hợp.
- Mỗi topology có ưu điểm, nhược điểm riêng khi triển khai.

## Thuật ngữ quan trọng
| Thuật ngữ | Giải thích |
|---|---|
| LAN | Mạng cục bộ. |
| Ethernet | Công nghệ LAN phổ biến, chuẩn IEEE 802.3. |
| FDDI | Công nghệ mạng vòng dùng cáp quang. |
| Topology | Hình trạng/kết cấu kết nối mạng. |
| Star | Topology hình sao. |
| Ring | Topology dạng vòng. |
| Bus | Topology tuyến tính. |
| Mesh | Topology lưới. |
| Hub | Thiết bị tập trung tín hiệu trong LAN. |
| Switch | Thiết bị chuyển mạch trong LAN. |

## Câu hỏi ôn tập
1. LAN là gì?
2. Nêu các đặc trưng của mạng LAN.
3. LAN thường chia sẻ những loại tài nguyên nào?
4. Ethernet có vai trò gì trong mạng LAN?
5. Trình bày mạng hình sao và ưu nhược điểm.
6. Mạng bus cần terminator để làm gì?
7. Vì sao mạng mesh có độ tin cậy cao nhưng chi phí lớn?
8. Khi thiết kế LAN cần quan tâm những yếu tố nào?
