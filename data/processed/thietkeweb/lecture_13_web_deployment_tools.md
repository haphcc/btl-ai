### BÀI 13

#### BÀI GIẢNG 13: WEB DEPLOYMENT TOOLS

## TRANG 1

Thiết kế Web - Bài giảng 13: Web Development Tools

Giảng viên: Vũ Trọng Sinh


## TRANG 2

Nội dung

8.1. Tổng quan về web deployment. 8.2. Git & GitHub. 8.3. Domain & Hosting. 8.4. Deployment & Testing.


## TRANG 3

8.1. Tổng quan về web deployment

Deploy website là quá trình chuyển source code của website từ môi trường phát triển (local) sang môi trường production (server) để user có thể truy cập qua Internet.

Mục tiêu:

- Đảm bảo website hoạt động ổn định.
- Giúp website dễ update và maintain.


## TRANG 4

Các bước chung để deploy website

Chuẩn bị source code -> hoàn thiện file HTML, CSS và JS, test local.

Quản lý source code -> dùng Git để lưu trữ và theo dõi thay đổi trong code.

Chọn hosting platform -> ví dụ: Vercel, Netlify, VPS hoặc private server.

Kết nối domain (nếu có) -> cấu hình domain name để user truy cập dễ hơn.

Upload hoặc sync source code lên server -> dùng Git, FTP hoặc deployment tool tích hợp của hosting platform.

Test website sau khi deploy -> test trên nhiều thiết bị và sửa các vấn đề phát hiện được.


## TRANG 5

8.2. Git & GitHub

Git intro. Git concept. GitHub. GitHub basics. GitHub Pages.


## TRANG 6

Git intro

Git là version control system.

Git giúp bạn theo dõi thay đổi của code.

Git được dùng để cộng tác khi viết code.

Git và GitHub là hai thứ khác nhau.


## TRANG 7

Git làm gì?

- Quản lý project bằng repository
- Clone project để làm việc trên local copy
- Kiểm soát và theo dõi thay đổi bằng staging và committing
- Branch và merge để làm việc trên các phần và phiên bản khác nhau của project
- Pull phiên bản mới nhất của project về local copy
- Push update local lên project chính


## TRANG 8

Vì sao dùng Git?

- Hơn 70% developer dùng Git.
- Developer có thể làm việc cùng nhau từ bất kỳ đâu trên thế giới.
- Developer có thể xem toàn bộ history của project.
- Developer có thể revert về phiên bản trước của project.

https://www.youtube.com/watch?v=e9lnsKot_SQ


## TRANG 9

Cài đặt Git

Download Git miễn phí từ website:

https://www.git-scm.com/

- Với Windows, bạn có thể dùng Git Bash đi kèm Git for Windows.
- Với Mac và Linux, bạn có thể dùng terminal tích hợp.

Cấu hình Git:

- git config --global user.name "w3schools-test"
- git config --global user.email "test@w3schools.com"


## TRANG 10

Thực hành

Cài Git for Windows trên máy của bạn. Đăng ký tài khoản GitHub (nếu cần). Cấu hình Git global username & email.

- Thời lượng: 10 phút


## TRANG 11

Git concept

- Initialize Git: https://www.w3schools.com/git/git_getstarted.asp?remote=github
- Adding New Files: https://www.w3schools.com/git/git_new_files.asp?remote=github
- Staging Environment: https://www.w3schools.com/git/git_staging_environment.asp?remote=github
- Commit: https://www.w3schools.com/git/git_commit.asp?remote=github
- Branch: https://www.w3schools.com/git/git_branch.asp?remote=github
- Merge Branches: https://www.w3schools.com/git/git_branch_merge.asp?remote=github

Video tutorial:

https://www.youtube.com/watch?v=MFtsLRphqDM&list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR&index=2


## TRANG 12

Git quiz

https://www.w3schools.com/git/git_quiz.asp?remote=github


## TRANG 13

GitHub là gì?

- Git không giống GitHub.
- GitHub tạo ra các tool sử dụng Git.
- GitHub là nơi hosting source code lớn nhất thế giới và thuộc sở hữu của Microsoft từ năm 2018.


## TRANG 14

Thực hành GitHub

Đăng ký tài khoản GitHub. Tạo một directory cho group project. Push local repository lên GitHub.


## TRANG 15

GitHub basics

Pulling để cập nhật thay đổi:

- Git Fetch
- Git Merge
- Git Pull

https://www.w3schools.com/git/git_pull_from_remote.asp?remote=github


## TRANG 16

GitHub basics

Push change lên GitHub:

https://www.w3schools.com/git/git_push_to_remote.asp?remote=github


## TRANG 17

GitHub basics

Create a new branch on GitHub:

https://www.w3schools.com/git/git_remote_branch.asp?remote=github

Pulling a branch from GitHub:

https://www.w3schools.com/git/git_branch_pull_from_remote.asp?remote=github

Push a branch to GitHub:

https://www.w3schools.com/git/git_branch_push_to_remote.asp?remote=github


## TRANG 18

GitHub Pages

Với GitHub Pages, GitHub cho phép bạn host một webpage từ repository của bạn.

1. Tạo một repository mới.
2. Push local repository lên GitHub Pages.
3. Kiểm tra GitHub Page của bạn.

https://www.w3schools.com/git/git_remote_pages.asp?remote=github

https://www.w3schools.com/git/git_exercises.asp?remote=github

https://docs.github.com/en/pages/quickstart


## TRANG 19

Git exercise

https://www.w3schools.com/git/git_exercises.asp?remote=github

Push local project của bạn lên một GitHub repo, sau đó tạo GitHub Page từ repo.

- Thời lượng: 20 phút
- 3 nhóm đầu tiên ở mỗi lớp trình bày: cộng 1 contribution
- Các nhóm không trình bày: -1 contribution
- Mỗi nhóm tối đa 2 phút
- Show nhanh source code trang web hiện tại của nhóm trên máy local (VS Code mở cả project folder)
- Show repo của nhóm trên GitHub, các lần commit, mỗi thành viên đã commit những gì
- Show trang web đã upload lên GitHub Pages


## TRANG 20

8.3. Domain & Hosting

DNS hoạt động như thế nào. Domain name best practice. Chọn hosting.


## TRANG 21

DNS hoạt động như thế nào


## TRANG 22

DNS hoạt động như thế nào

1. User nhập web address hoặc domain name vào browser.
2. Browser gửi một message gọi là recursive DNS query tới network để tìm IP hoặc network address tương ứng với domain.
3. Query đi tới recursive DNS server, còn gọi là recursive resolver, thường do Internet Service Provider (ISP) quản lý. Nếu resolver có address, nó trả address cho user và webpage sẽ load.
4. Nếu recursive DNS server không có answer, nó sẽ query một chuỗi server theo thứ tự: DNS root name server, top-level domain (TLD) name server và authoritative name server.
5. Ba loại server phối hợp và tiếp tục redirect cho đến khi lấy được DNS record chứa IP address được query. Thông tin này được gửi tới recursive DNS server và webpage user cần sẽ load.
6. Recursive server lưu hoặc cache A record cho domain name, record này chứa IP address. Lần sau khi nhận request cho domain name đó, nó có thể trả lời trực tiếp thay vì query server khác.
7. Nếu query tới authoritative server nhưng không tìm thấy thông tin, server trả về error message.


## TRANG 23

Domain name best practice

1. Giữ tính độc đáo và đúng brand.
2. Chọn top-level domain extension cẩn thận.
3. Kết hợp targeted keyword.
4. Đảm bảo domain dễ phát âm và dễ đánh vần.
5. Tránh hyphen, abbreviation và doubled letter.
6. Giữ domain name ngắn.
7. Chọn domain name linh hoạt.
8. Kiểm tra lịch sử domain.
9. Nghiên cứu social media handle.
10. Bảo vệ brand bằng nhiều domain.

https://www.dreamhost.com/blog/how-to-choose-the-right-domain-name/


## TRANG 24

Domain name cho site của bạn?

Chủ đề website final project của bạn là gì?

Nghĩ ra 3-5 domain name có thể dùng. Kiểm tra availability của các domain name đó.


## TRANG 25

Chọn hosting

https://www.hostinger.com/tutorials/how-to-choose-a-web-hosting-provider

Hiện tại chưa quá quan trọng, nhưng sẽ cần cho môn Web Programming. Có lựa chọn thay thế nào không? Liệt kê một số lựa chọn để lấy contribution point.


## TRANG 26

8.4. Deployment & Testing

Deploy site lên Vercel. Deploy lên hosting khác. FileZilla. WinSCP. Test visualization trên nhiều thiết bị và chỉnh sửa nếu cần. Đăng ký với search engine:

https://www.google.com/webmasters/tools

https://www.bing.com/webmasters/about


## TRANG 27

Deploy static website lên Vercel

https://www.youtube.com/watch?v=X6boIuWzBhg
