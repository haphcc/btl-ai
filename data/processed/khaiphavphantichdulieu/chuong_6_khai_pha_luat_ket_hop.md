### BÀI 6

#### CHƯƠNG 6 KHAI PHÁ LUẬT KẾT HỢP

## TRANG 1

Khai phá mẫu phổbi ến và luật kết hợp

## TRANG 2

Câu chuyện “bim” và “bia”?

ưm all Í

## TRANG 3

Mining association rules between sets of items in large databases

Full Text: flppr 7: Get this Article ==

Authors: Ra kesh Agrawal IBM Almaden Research Center, 650 Harry Road, San © 1993 Article Jose, CA Tomasz Imielinski Computer Science Department, Rutgers University, New Brunswick,NJ Arun Swami IBM Almaden Research Center, 650 Harry Road, San - Bibliometrics Jose, CA - Citation Count: 3,365

- Do wnloads (cumulative):

## ` A 20,307

Published in:: Do wnloads (12 Months): 1,704 === + proceeding: Do wnloads (6 Weeks): 209 SIGMOD '93 Proceedings of the 1993 ACM SIGMOD international conference on Management of data ca Sha Pages 207-216

Fast Algorithms for Mining Association Rules in Large Databases

Authors: Ra kesh Agrawal Ra makrishnan Srikant 1994 Article

Published in:

: Proceeding 1 Bibliometrics VLDB '94 Proceedings of the 20th International Conference on Very Large - Citation Count: 4,164 Data Bases -- Gearon ir Pages - Do wnloads (12 Months): n/a 487-499 - Do wnloads (6 Weeks): n/a

September 12 - 15, 1994 Morgan Kaufmann Publishers Inc. San Francisco, CA, USA ©1994 table of contents ISBN:1-55860-153-8

## TRANG 4

= Google Scholar O__ SIGNIN

Ra kesh Agrawal GET MY OWN PROFILE

Technical Fellow, Microsoft Research

Verified email at microsoft. com

Data Mining Web Search Education Privacy Cited by VIEW ALL

All Since 2013

TILE CITED BY YEAR Citations 114789 34215 h-index 100 57 i10-index 264 171 Fast algorithms for mining association rules 24041 1994 R Agrawal, R Srikant Proc. 20th int. conf. very large data bases, VLDB 1215, 487-499 8000

Mining association rules between sets of items in large databases 20661 1993 6000 R Agrawal, T Imieli ñski, A Swami Acm sigmod record 22 (2), 207-216 4000

Mining sequential patterns 7035 1995 R Agrawal, R Srikant 2000 Data Engineering, 1995. Proceedings of the Eleventh International Conference... ữ Privacy-preserving data mining 3675 2000 2011 2012 2013 2014 2015 2016 2017 2018 © R Agrawal, R Srikant ACM Sigmod Record 29 (2), 439-450

## TRANG 5

## Nội dung

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh giá luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 6

## Nội dung

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh giá luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 7

Khái niệm luật kêt hợp (association rule)

. „ mứt thịt bò, as BEng sữa, mat trứng, thịt seeư ờng, 4 bò, gia, mỳ uc banhmy,... mm ites ` 7 a = = kháchhàngm “ Rms Big

## )EEEEEI 73 "a

khách hang 3

kháchhàng2 khách hàng1

e Luật kết hợp: Mối quan hệkết hợp giữa các tập thuộc tính trong cơ sở dữ liệu.

e Ví dụ:

» {bánh mỳ, bơ, mứt dâu} > {sữa tươi} (phổbi ên: 3%, tin cậy: 80%) > {tuôi > 45, gia đình có lịch sửti êu đường, huyét áp cao} -&gt; {mắc bệnh tiêu đường} (phổbi ền: 1.5%, tin cậy: 76%)

## TRANG 8

Tập mục, giao dịch, và cơ sở dữ liệu giao dịch (Itemset, Transaction, and Transactional Database)

e Ký hiệu I = {xi,xa,..., xa} là tập n mục (item). Ví dụ:

> Tập tat cảcác mặt hàng thực phẩm trong siêu thị: I = {sữa, trứng, đường, bánh mỳ, mật ong, mut, bơ, thịt bò, gid,...}.

>» Tập tât cảcác bộphim: I = {pearl harbor, fast and furious 7, fifty shades of grey, spectre,... }.

e Một tập X CI được gọi là một tap mục (itemset).

e Nếu X có k mục (tức |X| = k) thì X được gọi là k-itemset.

e Ký hiệu D = {TỊ, To,..., Tm} là cơ sở dữ liệu gồm m giao dịch (transaction). Mỗi giao dịch T; € D là một tập mục, tức T; C I.

## TRANG 9

Ví dụvềcơ sở dữ liệu giao dịch

Tập tất cảcác mục I:

## I = {A,B, C, D, E} |

Cơ sở dữ liệu giao dich D:

D = {TI, To, T3, Ta, Ts, Tạ}, cụ thể:

e Tị={A,B,D,E} § T13 -=. B. bị

## e 73 = {A, B,D, E}

e Tạ={A,B,C,E}

e s-{A,B,C,D,E} 6 Ts-={H,C,P}

## TRANG 10

Tập /mẫu phổbi én (frequent itemset/pattern)

e Cho tập mục X (C1).

e Độh ỗtr ợ(support) của X, ký hiệu là sup(X, D), là sô lượng giao dịch trong D chứa X:

sup(X,D)= |{T|T e D và X C T}| (1)

e Độh ỗtr ợtương đôi (relative support) của X, ký hiệu là rsup(X, D), là số phần trăm các giao dịch trong D chứa X:

rsup(X. D) = sup(X,X,DD) (2)

|D|

e Tập mục X được gọi là tập (mục) phổbi ên (frequent itemset) trong D nếu sup(X,D) > minsup, với minsup là một ngưỡng độh ỗtr ợt ối thiêu (minimum support threshold) do người dùng định nghĩa.

e Ký hiệu F là tập tat cảcác tập phổbi ến.

e Ký hiệu F(*) là tập tất cảcác tập phổbi ến có độd ài k (frequent k-itemsets).

## TRANG 11

Các tập phô biên (với minsup = 3) từcơ sở dữ liệu D

D= 1171, To, Ts, Ta, Ts, Te}:

## ® Tị-{A,B,D,E}

® i; ={6,C,E}

## @ T; = {A,B,D,E}

## ® Tạ={A,B,C,E}

## ® T; ={A,B,C,D,E}

@ t= {B, Cc; D}

Tập tất cảcác tập phổbi ến F và các FŒ):

## @ F = {A, B, C, D, E, AB, AD, AE, BC, BD, BE, CE, DE,

## ABD, ABE, ADE, BCE, BDE, ABDE}

## @ F = {A, B, C, D, E}

## e F?) = {AB, AD, AE, BC, BD, BE, CE, DE}

## eở) = {ABD, ABE, ADE, BCE, BDE}

## e F = {ABDE}

## TRANG 12

Luật kết hợp (association rule) e Luật kết hợp có dạng:

## X+Y (3)

với X vàY là hai tập mục (X, Y Cl) và Xñ Y =Ú.

e Độh ỗtr ợ(support) của luật X + Y trong cơ sở dữ liệu D, ký hiệu là sup(X - Y,D), là số giao dịch chứa cảX vàY:

sup(X > Y,D) = sup(X U Y,D) (4)

e Độh ỗtr ợtương đôi (relative support) của luật X -&gt; Y trong cơ sở dữ liệu D, ký hiệu rsup(X -› Y,D), là số phan trăm các giao dịch trong D chứa cảX vàY:

rsup(X XUY,D > Y,D) =eo (5)

e Luật X > Y được gọi là phổbi én (frequent) nếu:

sup(X - Y,D) > minsup (6)

## TRANG 13

Luật kết hợp (association rule) - tiếp

e Độ tin cậy (confidence) của luật X - Y trong D, ký hiệu conf(X -› Y,D), là tỉl ệgi ữa sô giao dịch chứa cảX vàY trên số giao dịch chỉch ứa X:

f(X sup(X U Y,D) conf > Y,D)=-----_--VD) =~ sup(X,D) ạ7 e Một cách diễn giải khác: conf(X - Y,D) là xác suât có điều kiện mà một giao dịch trong D chứa Y khi nó đã chứa X:

conf(X + Y,D) = P(Y|X). Tuy nhiên bản chất vẫn là mức độ tin cậy của luật.

e Luật X - Y được gọi là mạnh (strong) nêu độ tin cậy của nó lớn hơn hoặc bằng một ngưỡng minconf nào đó do người dùng định nghĩa:

conf(X - Y,D) > minconf (8)

e Ngoài độ tin cậy (độm ạnh) của luật kết hợp, còn các tiêu chí khác đê danh giá mức độgi á trị của luật (sẽb àn luận sau).

## TRANG 14

Ví dụminh họa luật kết hợp

ID -= {Tì, To, Ts, Ta, FE; Tạ}:

## e T,; = {A,B,D,E}

e Tạ-={B,C,E}

## e T3= {A,B,D,E}

## e T, = {A, B,C, E}

e Tạ={B,C,D}

e Xét luật {B, C} -› {E} (ngắn gon là BC -› E):

> sup(BC + E,D) = sup(BCE,D) = 3 > conf(BC - E,D) = SG) = 3 = 0.75 (tức 75%) e Xét luật {A, D} -› {B, E} (ngắn gọn là AD -› BE):

> sup(AD -› BE,D) = sup(ABDE,D) = 3

> conf(AD -› BE,D) = BUT) = 3 = 1.0 (tức 100%)

## TRANG 15

## Nội dung

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh giá luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 16

Các phương pháp khai phá

|. Các bước trong khai phá luật kết hợp

2. Phương pháp brute-force

3. Phương pháp Apriori

4. Phương pháp FP-Growth

5. Các phương pháp khác

## TRANG 17

Các bước khai phá luật kêt hợp

Hai bước khai phá luật kết hợp từCSDL giao dịch D:

e Mining frequent itemsets/patterns: Khai phá tất cảcác tập phổ biên từcơ sở dữ liệu D với ngưỡng hỗtr ợt ôi thiểu minsup.

e Generating strong rules from mined frequent itemsets/patterns:

Sinh tat cảcác luật mạnh từcác tập phô biên được khai phá ởb ước trước với ngưỡng tin cậy tôi thiêu minconf.

e Bước một có độph ức tạp tính toán cao hơn và thường chiêm phần lớn thời gian khai phá luật kêt hợp.

e Số lượng các tập mục (itemsets) là rât lớn. Ví dụvới I = {Xị,Xa,..., Xioo} chúng ta có 2109 - 1 1.27 x 10°° tập con (không tính tập ().

## TRANG 18

Các phương pháp khai phá

|. Các bước trong khai phá luật kết hợp

2. Phương pháp brute-force

3. Phương pháp Apriori

4. Phương pháp FP-Growth

5. Các phương pháp khác

## TRANG 19

Dàn các tập mục (itemset lattice)

@ Cho tập các mục Il = {xị,x¿,..., Xn}, Có 2lll = 2n tập mục (bao gồm cảtập rỗng).

e Các tập mục được kết nôi với nhau thành một giàn các tập mục (itemset lattice):

> Tập mục X va Y được kết nối với nhau trên giàn nêu và chỉn êu X là tập con trực tiêp của Y, nghĩa là X C Y và |Y| = |X| +1.

e Các tập mục trên giàn có thểđược duyệt theo chiều rộng (breadth-first search - BFS) hoặc chiều sâu (depth-first search - DFS) trên cây tiên tô.

e Với tập các mục I = {A, B, C, D, E}, chúng ta có giàn bao gồm 2° = 32 tập mục bao gồm tập rỗng () và chính nó (ABCDE) 6

trang sau.

## TRANG 20

Minh họa dàn các tập mục

(0) oo IX.

RRSS >SEKaa &lt;P Am hs ¬= SSK

## TRANG 21

Tìm các tập phô biên bang p. pháp vét cạn (brute-force)

1: procedure BRUTEFORCE(D = {TI, T›,..., Tm}, Ï= {x1, x2,..., Xn}, minsup) 2: Khởi tao tập các tập phổbi én: F < 0;

3: for each X CI do 4: sup(X,D) - Compute Support(X, D);

5: if sup(X,D) > minsup then

## 6: F¢ FU{X};

7: end if

8: end for

Q: return F;

10: end procedure

1: procedure COMPUTESUPPORT(X, D = { T1, T2,..., Tm}) 2: Khởi tạo: sup(X,D) < 0;

3: for each T € D do

4: if X C T then 5: sup(X,D) «+ sup(X,D) + 1;

6: end if

T: end for 8: return sup(X, D);

9: end procedure

## TRANG 22

Kêt quảkhai phá các tập phổbi ên

D={ÏTq, Tz, T3, Tạ, Ts, Tạ}:

## @ T¡ị={A,B,D,E}

## @ Tạ-{B,C,E}

## @ T; ={A,B,D,E}

## ® Tạ= {A,B,C,E}

## ® T; = {A,B,C,D,E}

## ® Tạ={B,C,D}

Các tập phổbi ên khai phá được từD với minsup = 3:

® sup = 6: {B} @ sup =5: {E, BE}

## @ sup =4: {A, C, D, AB, AE, BC, BD, ABE}

## @ sup = 3: {AD, CE, DE, ABD, ADE, BCE, BDE, ABDE}

## TRANG 23

Hiệu quảcủa phương pháp vét cạn

e Thuật toán tính độh ỗtr ợ(Compute Support) có độph ức tạp tính toán O(|I| - |D|).

e Vì có 2l tập con của Il nên thuật toán Brute Force có độph ức tạp tính toán là O(II - |DỊ- 21).

e Dé phức tạp vào ra (I/O complexity) là O(2!"!) lần quét cơ sở dữ liệu giao dịch D.

@ Phai duyét hét toan bộkh ông gian các tập mục (toàn bộcác nút trên giàn).

e Thời gian tính toán và quét dữ liệu rất lớn.

e Kiểm tra rất nhiều tập mục không tiềm năng là tập phổbi ến.

## TRANG 24

Các phương pháp khai phá

|. Các bước trong khai phá luật kết hợp

2. Phương pháp brute-force

3. Phương pháp Apriori

4. Phương pháp FP-Growth

5. Các phương pháp khác

## TRANG 25

Một sô tinh chat su dụng trong phương pháp Apriori

e Cho hai tập mục X, Y CI và cơ sở dữ liệu D.

e Nêu X C Y thì sup(X,D) > sup(Y, D).

Hai tính chất Apriori:

e Nếu Y là tập phổbi ến (frequent) thì mọi tập con X (C Y) của Y đều phổbi ến.

e Nếu X là tập không phổbi ến (infrequent) thì mọi tập cha Y (D X) của X đều không phổbi ến.

e Phương pháp Apriori dựa vào hai tính chất trên đểc ải tiễn phương pháp vét cạn bằng cách cắt tỉa các nhánh không cần thiết trên giàn tập mục.

e Cụth ể, khi duyệt theo bé rộng (BFS) trên giàn tập mục, thuật toán Apriori cắt tỉa hét tat cảcác tập cha của tập không phổbi ên.

## TRANG 26

Cắt tỉa trên giàn tập mục trong Apriori (minsup = 3)

GÀ

Level1 Cay Co) Cm WM) TED

Level2

Level 3 =. Ờ NGG

Lee

[Nguồn: Data Mining and Analysis: Fundamental Concepts and Algorithms by Zaki and Jr]

## TRANG 27

Cắt tỉa trên giàn tập mục trong Apriori (minsup = 3) - tiêp

e Ởh ình trước, các nút màu sậm là các tập mục không phổbi ến.

e Tất cảcác tập cha của chúng trên giàn (các nút vạch đứt) đầu bịc ắt tỉa, dẫn đến toàn bộcác nhánh vạch đứt được cắt tỉa.

e Ví dụ: tập AC có sup(AC,D) = 2 < minsup nên các tập cha của AC có tiền tô là AC sẽb ịc ắt tia, dan đến toàn bộc ây con dưới nút AC bịc ắt tỉa.

## TRANG 28

CSDL giao dịch D minh hoa cho thuật toán Apriori

Tập tất cảcác mục I:

1 = {A, B,C, D, E}

Cơ sở dữ liệu giao dịch D:

D= {Th, Tạ, Ta, Tạ, Tạ, Tạ}, cụ thể:

## e T, ={A,B,D,E}

e Tạ-={B,C,E}

## e T3 = {A,B,D,E}

## e T4 = {A,B,C,E}

## ® Tạ={B,C,D;

® Với minsup = 3.

## TRANG 29

Minh2 họa thuật A toán⁄ Apriori..

Tập các tập mụcứng viên CÚ Tập các tập mục phổbi ến F0

1-itemset | support 1-itemset | support

fy 4 fay 4 Quét CSDL tinh {B} 6 Kiểm tra độh ỗtr ợ {B} 6 -&lt;d6 hỗtr ợcho các-&gt; {C} 4 của các tapứng viên-&gt; {C} 4 tập mụcứng viên {D} 4 với ngưỡng minsup {D} 4

## {E} 5 {E} 5

Tập các tập mụcứng viên C® Tập các tập mụcứng viên C)

## ^ F ^ Ä L:Á (2)

2-itemset 2-itemset support Tập các tập mục pho biên F {AB} {AB} 4 2-itemset | Support

## {AC} {AC} 2 {AB} 4

## {AD} {AD} 3 {AD} 3

## ¬ {AE}.; {AE} 4 2 x1. {AE) 4

Sinh tập các {BC} Quét CSDL tính {BC} 4 Kiêm tra độh ỗtr ợ {BC} 4 tập mụcứng -=&gt; BD -&lt;d6 hỗtr ợcho các-&gt; BD 4 của các tapứng vien&gt; BD 4 viên C® từF {BD} tập mụcứng viên {BD} với ngưỡng minsup {BD}

## {BE} {BE} 5 {BE} 5

## {CD} {CD} 2 {CE} 3

## {CE} {CE} 3 {DE} 3

## {DE} {DE} 3

Sinh tap cac tập mụcứng -=&gt; viên C#) từF?

## TRANG 30

Minh„ họa thuậta toán7 Apriori5. (2)

a ^ “:A (3) Tập các tập mụcứng viên C Tập các tập mụcứng viên C®) Tập các tập mục phổbi ến F®) s-itemset 3-itemset support 3-itemset support Sinh (ABE, {ABD} 3 {ABD} 3- tập các {ADE} Quét CSDL tinh {ABE} 4 Kiểm tra độh ỗtr ợ {ABE} 4 tap mụcứng -&gt; -<6 hỗtr ợcho cac-&gt; {ADE) 3 “của các tập ứng vien® {ADE} 3 viên C® từF2) bó) tập mụcứng viên {BCE} 3 với ngưỡng minsup {BCE} 3

## (BDE) {BDE} 3 {BDE} 3

Tập các tập mụcứng viên C Tập các tập mụcứng viên CÉ) Tập các tập mục phổbi ến F)

Sinh 4-itemset 4-itemset support. 4-itemset support tap cac Quét CSDL tinh + Kiểm tra độh ỗtr ợ + tập mụcứng -&gt; {ABDE} --d6 hỗtr ợcho các-&gt; {ABDE} 3 “của các tập ứng vién® {ABDE} 3 viên C từF9) tập mụcứng viên với ngưỡng minsup:

## TRANG 31

Thuật toán Apriori

1: procedure APRIORI(D = { 71, T2,..., Tm}, Ï = {xi,xa,..., Xa}, minsup) 2: Khởi tao tập các tập phổbi ển: F < Ú;

3: FY «+ Find Frequent1ltemsets(D, I, minsup);

4: for (k = 2; F€= 4Ú; k++) do 5: C) - Apriori Gen(EŒ=1));

6: for (each transaction T € D) do 7: Cr + Subsets Of T(C, T);

8: for (each C € Cr) do Q: C. count++;

10: end for

11: end for 12: FY - {C € C\|C. count > minsup};

13: end for

144. Fe FOUR? U---UFM);

15: return F;

16: end procedure

## TRANG 32

Thuật toán Apriori (2)

1: procedure APRIORIGEN(Ef Œ=) 2: Khởi tạo tập các tập mụcứng viên: Cứ) < Ú;

3: for (each itemset F¡ c F“~)) do 4: for (each itemset Fy € F-”)) do 5: if ((Fy[1] = Fa[1]) A... A (Falk - 2] = Folk - 2]) A (ilk - 1] < Folk - 1])) then 6: Ce F, x F›;

7: if (Has Infrequent Subset(C, F(“~"))) then 8: remove C;

9: else

## 10: CH - CH U {Cc}:

11: end if

12: end if

13: end for 14: end for 15: return C(*):

16: end procedure

## TRANG 33

Thuật toán Apriori (3)

1: procedure HASINFREQUENTSu BSET(C, =®)) 2: for (each (k - 1)-subset S of C) do 3: if (S ø F“~)) then 4: return TRUE;

5: end if

6: end for

7: return FALSE;

8: end procedure

## TRANG 34

Sinh luật kêt hợp phô biên và mạnh từcác tập phd biên

e Input: Tập tất cảcác tập phổbi én F.

e Output:Tập tất cảcác luật phổbi ến (frequent) và mạnh (strong): R.

1: procedure GŒ ENEREQUENTSTRONGRULES(E, minconf) 2: Khởi tạo R + 9;

3: for (với mỗi tập mục phổbi ên F € F và |F| > 2) do

## A: X&lt;c {X|X CF,X FO};

5: while (X 4 @) do 6: Y < maximal element in X;

## 7: X¢+X\Y;

8: if (conf(Y -&gt; F \ Y) > minconf) then

## 0: R¢RU{Y >F\Y};

10: else

## 11: X= X\{Z|Zc Y}

12: end if

13: end while

14: end for

15: return R;

16: end procedure

## TRANG 35

Ưu và nhược điềm của phương pháp Apriori

e Ưu điểm:

> Nhờcác tính chất Apriori đểc ắt tia được nhiều nhánh trên giàn (lattice), giảm bớt đáng ké việc sinh các tập mụcứng viên và kiêm tra tính phô biên của các tập ứng viên đó.

e Nhược điểm:

> Vẫn cần sinh ra một lượng lớn các tập ứng viên. Ví dụ, nêu có 10 tâp mục phô biên gồm một mục (1-itemsets), thuật toán Apriori can sinh ra hơn 10’ tập mụcứng viên có hai mục (2-itemsets).

» Cần quét cơ sở dữ liệu nhiều lần đểd ém độh ỗtr ợcủa các tập ứng viên trong quá trình thực hiện thuật toán.

## TRANG 36

Các phương pháp khai phá

|. Các bước trong khai phá luật kết hợp

2. Phương pháp brute-force

3. Phương pháp Apriori

4. Phương pháp FP-Growth

5. Các phương pháp khác

## TRANG 37

Phương pháp FP-Growth

e Câu trúc dữ liệu FP-Tree (Frequent Pattern Tree)

e Sinh cây FP-Tree từcơ sở dữ liệu e Sinh tập phổbi ến từFP-Tree e Ưu và nhược điểm của phương pháp FP-Growth

## TRANG 38

Câu trúc dữ liệu FP-Tree

e Mỗi nốt trên cây được gắn nhãn là một mục (item).

e Các nét con của một nốt đại diện cho các mục khác nhau.

e Mỗi nét cũng lưu thông tin về độh ỗtr ợ(support) của tập mục (itemset) bao gồm tat cảcác mục trên đường đi từn ôt gôc đền nó.

e Có một bảng lưu tất cảcác mục và con trỏ(node-link) đểli ên kết tât cảcác vịtr í xuât hiện của mỗi mục trong cây.

## TRANG 39

Thuật toán sinh cây FP-Tree T từCSDL giao dịch D

1: procedure BUILDFPTREE(D = {T, To,..., Tm}) 2: Khởi tạo cây FP-Tree T chỉch ứa nốt géc Ú va. support <- 0;

3: for (với mỗi giao dịch T € D) do 4: T’ = {x',...,x"} © sắp xếp các mục phổbi ên € T giảm dan theo support;

5: p Node + 0;

6: for (i = 1;¡ < h;i++) do 7: if (c Node € Children(p Node) and c Node. label = x') then 8: c Node. support++;

9: p Node + c Node;

10: else 11: Tao nốt c Node là một nốt con mới của p Node;

12: c Node. label - x’:

13: c Node. support <- 1;

14: p Node < c Node;

15: end if 16: end for 17: Ú. support-L-L;

18: end for

19: return cây FP-Tree T;

20: end procedure

## TRANG 40

CSDL giao dịch D minh họa phương pháp FP-Growth

Tập tat cảcác mục I:

## I = {A,B,C,D,E}

Cơ sở dữ liệu giao dịch D:

D = {Th, Tz, T3, Ta, Ts, Tạ}, cụ thể:

## e 7, = {A,B,D,E}

§ f5=16,C,E}

## e T3={A,B,D,E}

## e T, = {A, B,C, E}

## e T; = {A,B,C,D,E}

5 16-{6,C,0}

e Với minsup = 3.

## TRANG 41

Sắp xếp lại các mục (items) đểx ây dựng cây FP-Tree

Tập tất cảcác mục I:

## I = {B(6), E(5). A(4). C4). D(4)}

Cơ sở dữ liệu giao dich D:

D = {Tq, Tạ, T3, Ta, Ts, Tạ}, cụ thể:

## e 7, = {B,E,A, D}

## ® Tạ-={1B,E,C}

## e 73= {B,E,A,D}

e Ts = {B,E,A,C}

## e T; = {B,E,A,C,D}

e Ts = {B,C,D}

## TRANG 42

Minh họa thuật toán sinh cây FP-Tree T từCSDL D @®) @) @® o D

Cw) Ge) Ge) Cw)

## C0) C@) C0) CW)

Go) 4M Co) Ge Cc Ge) Ca)

uw) @w) @e) Cw) @e)

## woe GIAN PO | REND

Gs) 0)

0) C300)

CO) Cw) Co)

a) CY CH GH) CH

Ce) @e) Ce) @e)

@w) Cw)

Q&smơni one

[Nguồn: Data Mining and Analysis: Fundamental Concepts and Algorithms by Zaki and Jr]

.

## TRANG 43

Một vài đặc điểm của cây FP-Tree

e Chỉc ần quét toàn bộcơ sở dữ liệu D 2 lần đểx ây dựng cây FP-Tree

T.

e Cây FP-Tree là một dạng biểu diễn cô do ng (compressed) của cơ sở dữ liệu giao dịch D.

e Cây FP-Tree càng nhỏg ọn càng tốt.

° Các mục (items) càng phổbi ến (có độh ỗtr ợcao) càng nằm phía gần gôc cây.

e Tất cảcác tập phổbi ến (frequent itemsets) có thểđược khai phá trực tiêp từc ây FP-Tree T thay vì từCSDL D.

## TRANG 44

Cây FP-Tree T được xây dựng từCSDL D

[Nguồn: Data Mining and Analysis: Fundamental Concepts and Algorithms by Zaki and Jr]

## TRANG 45

2 ⁄ Thuật toán đệquy sinh các tập phô biên từc ây FP-Tree T

1: procedure FPGRow TH(T, P, F, minsup) 2: Loại bỏcác mục không phổbi ến (infrequent items) trong T;

3: if (Is Path(T)) then 4: for (với mỗi tập con Y C T) do

## 5: X&lt;PUY;

6: X. support - minxcy{cnt(x)};

## f: E€FU{X};

8: end for 9: else 10: for (mỗi mục y € T với thứt ựđ ã sắp xếp tăng dan theo sup(y)) do 11: X «+ PU ty};

12: X. support < sup(y); > sup(y) là tổng cnt(y) tại mọi nốt có nhãn y trong T 13: F¢ Fu {x X};

14: Khởi tạo FP-Tree Tx + 9;

15: for (với mỗi đường di path từg ôc xuông nốt có nhãn y trong cây T) do 16: cnt(y) - đêm tần suất của y trong path;

17: Chén path (ngoại trừn ốt y) vào cây FP-Tree Tx với cnt(y);

18: end for 19: if (Tx # 0) then 20: FPGrowth(Tx, X, F, minsup);

21: end if 22: end for 23: end if 24: end procedure

## TRANG 46

Sinh tập phổbi ến từFP-Tree: một số khái niệm

e Lời gọi hàm đầu tiên FPGrowth(T, P + Ú, F - 0, minsup).

e Phép chiêu chọn (projection) cây FP-Tree T theo một mục (item) nào đó.

e Cây FP-Tree T có thé là một đường tuyên tính (path).

e Loại bỏcác mục không phổbi ến (infrequent items) trong một cây FP-Tree.

## TRANG 47

Cây FP-Tree chiêu chọn (projected) theo mục (item) D

ch Oy) 2) C7 = CD) Ga) đo

## ca GD DGD DGD

ED (4) GD (a) add BC, cnt = 1 Gu) Ga)

Ce) @e) GW) Œu) ca) (b) add BEAC, cnt = 1 (c) add BEA, ent =2

[Nguén: Data Mining and Analysis: Fundamental Concepts and Algorithms by Zaki and Jr]

## TRANG 48

Loại bỏcác mục không phổbi ên (infrequent items) trong FP-Tree

Oa) (4)

Cú) Cú)

## CHE -+ Cð4ÓŒ6)

Ge) Ge)

Gy Coe)

e Bên trái: cây FP-Tree Tp chiêu theo mục D từc ây FP-Tree T.

e Bên phải: Cây FP-Tree Tp sau khi đã loại bỏm ục C không phổbi ến do cnt(C) = 1+ 1= 2< minsup = 3.

## TRANG 49

Minh họa thuật toán FP-Growth e Với lời gọi đầu tiên: FPGrowth(T, P + 0, ©- Ú, minsup = 3).

> Không xóa bỏđược mục không phổbi ên nào (tat cảđ ều phổbi ến).

> T không phải dạng đường tuyên tính path.

>» Tién tô (prefix) P = 0.

> y sẽl ần lượt nhận D(4), C(4), A(4), E(5), B(6).

"Trước tiên y nhận D:

## * X{© PUf{y} =0U{D}= {D}.

## * FOFU{X} =0U{{D(4)}} ={{D(4)}}.

* Có 3 đường di tuyên tinh (path) từg ôc của T đền nôt D: BCD, cnt(D) = 1; BEACD, cnt(D) = 1; và BEAD, cnt(D) = 2.

* Tạo cây FP-Tree Tp} từ3 paths nói trên.

* Goi đệquy hàm FPGrowth(T(py, {D}, {{D(4)}}, minsup = 3).

>» y nhận C:

>» y nhận A:

>» y nhận E:

>» y nhận 8:

## TRANG 50

Minh họa thuật toán FP-Growth (2)

e Với lời gọi FPGrowth(Trpy, P = {D}, F = {{D(4)}}, minsup = 3):

> Loại bỏtat cản ốt C ra khỏi Trp} vì ent(C) = 1+ 1=2< minsup = 3.

> Cây FP-Tree T(py bây giờtr ởthành một đường tuyén tính (path):

## B(4) - E(3) - A(3):

* Liệt kê tất cảcác tập con của đường tuyén tính:

## B, E,A, BE, BA, EA, BEA.

+ Ghép với tiền tôP = {D} tao thành các tập phổbi ến DB(4), DE(3),

## DA(3), DBE(3), DBA(3), DEA(3), DBEA(3).

* Thêm các tập phô biên vào trong ta được F = {D(4), DB(4),

## DE(3), DA(3), DBE(3), DBA(3), DEA(3), DBEA(3)}.

* Lời gọi FPGrowth(Tpy, P = {D}, F = {{D(4)}}, minsup = 3) kết thúc.

## TRANG 51

Minh họa thuật toán FP-Growth (3)

e Khi y nhận các mục khác:

>» y nhận C:

## * F = {D(4), DB(4), DE(3), DA(3), DBE(3), DBA(3), DEA(3),

## DBEA(3)} U {C(4), CB(4), CE(3), CBE(3)}.

> y nhận A:

## + F = {D(4), DB(4), DE(3), DA(3), DBE(3), DBA(3), DEA(3),

## DBEA(3)} U {C(4), CB(4), CE(3), CBE(3)} U

## {A(4), AE(4), AB(4), AEB(4)}.

>» y nhận E:

## * F = {D(4), DB(4), DE(3), DA(3), DBE(3), DBA(3), DEA(3),

## DBEA(3)} U {C(4), CB(4), CE(3), CBE(3)} U

## {A(4), AE(4), AB(4), AEB(4)} U {E(5), EB(5)}.

> y nhận B:

## * F = {D(4), DB(4), DE(3), DA(3), DBE(3), DBA(3), DEA(3),

## DBEA(3)} U {C(4), CB(4), CE(3), CBE(3)} U

## {A(4), AE(4), AB(4), AEB(4)} U {E(5), EB(5)} U {B(6)}.

## TRANG 52

Minh họa thuật toán FP-Growth (4)

e Vậy F bao gồm các tập phổbi ên với các mức hỗtr ợkh ác nhau:

> Support = 6: B > Support = 5: E, BE >» Support = 4: D, C, A, DB, CB, AE, AB, ABE

## >» Support = 3: DE, DA, CE, DBE, DBA, DAE, CBE, DBEA

## TRANG 53

Ưu và nhược điểm của phương pháp FP-Growth

e Ưu điểm:

>» Nén được cơ sở dữ liệu trong một câu trúc cây gọn nhẹFP-Tree.

> Chi cân quét co sở dữ liệu 2 lần.

> Hiéu quảk ê cảkhi ngưỡng minsup bé.

e Nhược điểm:

>» Thuật toán cài đặt phức tap hơn so với Apriori.

> Khi cơ sở dữ liệu lớn: FP-Tree lớn và khó lưu vừa trong bộnh ớ.

> Sử dụng đệquy (có thê khửđ ệquy).

## TRANG 54

6.3. Khám phá các mẫu thường xuyên

So sánh giữa giải thuật Apriori và giải thuật FP-Growth

Co giãn tuyến tính với số giao dịch

1

## TRANG 55

2

6.4. Khám phá các luật kết hợp từ các mẫu thường xuyên

-Strong association rules AB

Support(AB) = Support(A U B) >= min_sup

Confidence(AB) = Support(A U B)/Support(A) = P(B|A) >= min_conf

Support(AB) = Support_count(A U B) >= min_sup

Confidence(AB) = P(B|A) = Support_count(AUB)/Support_count(A) >= min_conf

## TRANG 56

3

6.4. Khám phá các luật kết hợp từ các mẫu thường xuyên

Quá trình tạo các strong association rules từ tập các frequent itemsets

Cho mỗi frequent itemset l, tạo các tập con không rỗng của l.

Support_count(l) >= min_sup

Cho mỗi tập con không rỗng s của l, tạo ra luật “s (l-s)” nếu Support_count(l)/Support_count(s) >= min_conf

## TRANG 57

6.4. Khám phá các luật kết hợp từ các mẫu thường xuyên

## I1 I2 I5

Min_conf = 50%

## I1 I5 I2

## I2 I5 I1

## I5 I1 I2

4

## TRANG 58

Các phương pháp khai phá

|. Các bước trong khai phá luật kết hợp

2. Phương pháp brute-force

3. Phương pháp Apriori

4. Phương pháp FP-Growth

5. Các phương pháp khác

## TRANG 59

## Nội dung

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh gia luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 60

66 Interestingness”r 99 va^ 66 ‘Usefulness 99

Interestingness Measures

- Mined SN Interesting

ming Patterns Patterns

57

## TRANG 61

Một số ti êu chí đánh giá

|. Conciseness

2. General/Coverage (Support)

3. Reliability (Confidence)

4. Peculiarity

5. Diversity

6. Novelty

7. Surprisingness/Unexpectedness

8. Utility

9. Actionability/Applicability

## TRANG 62

Luật mạnh (strong) chưa chắc đã thú vị(interesting)

e Xét một cơ sở dữ liệu giao dịch về đồđi ện tửAl IElectronics trong đó có hai mặt hang games và videos.

e Giảsửtrong 10000 giao dịch được phân tích có:

> 6000 giao dịch mua games, >» 7500 giao dich mua videos, va > 4000 giao dich mua ca games lẫn videos.

e Giảsửđộh ỗtr ợt ôi thiểu minsup = 30% và độ tin cậy tối thiểu minconf = 60%.

e Luật games -&gt; videos có sup = 40% và conf = 66.67% là luật phổ biên và mạnh (strong).

e Tuy nhiên, luật này không phan ánh đúng bản chất vì xác sudt mua của videos trong CSDL là 75%, cao hơn cảđộ tin cậy của luật này.

## TRANG 63

Độdo ft của luật

e Xét luật kết hợp A > B.

e Dé do lift(A - B) được xác định như sau:

lift(A > B) - COnt(Af(A -&gt;B AUB sup(B)&gt; B) _ _sup(AUsup(A)sup(B)B) (9)

e Theo cách nhìn xác suất:

## . P(AU B)

lift(Aift(A -&gt; B) B) = ---_~P(A)P(B) (10)1

e Nếu /ift(A > B) = 1: Ava B độc lập, không nên có mỗi quan hệ tương quan giữa A và 8.

e Nếu /ift(A > B) > 1: luật A B có ý nghĩa (tương quan dương - positive correlation).

e Nếu fif(A > B) < 1: luật A&gt; B và cảlu ật B > A không có ý nghĩa (tương quan âm - negative correlation).

## TRANG 64

Conviction

Conviction P(A) P(B) (A- B) = --~--..

## P (AB)

= Giá trịtrong khoảng [0, +00) " Conviction = |:A va B độc lập

" Conviction < |: luật ít y nghĩa " Conviction lớn: luật có nhiêu ý nghĩa = Nhận xét: điều kiện qua chặt (strict)

61

## TRANG 65

Improve

Improve (A- B) = [P (B | A)- P(B)].

B' occurring Bnotoccuring Total Do ccurring Dnotoccurring Total A’ occurring 8000 1000 9000 Coccurring 3600 700 4300 A’ not occurring 500 500 1000 =C not occurring 3700 2000 5700 Total 8500 1500 10000 Total 7300 2700 10000

Improve (A'- B') = |P(B' | A')-P(B’)] = 0.03,

Improve(C- D) = [P(D | C)- P(D)] = 0.11.

= P(B’ | A’) - P(B | not A’) = P(D | C)-P(D | not C)

62

## TRANG 66

## Nội dung

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh giá luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 67

r N ˆ~ Phan z ~ on a Ww e tích dữ liệu ho trợra quyết định

How can we make it happen?

Prescriptive Analytics dối) What will happen? S 208 Predictive Ce) Analytics ‹ ư ớc % LS sở Why did"it happen? co?

= Diagnostic la Analytics ®& FWhat happened? CS Kở Descriptive = Analytics) oe Cs Ny at

‹ x S v

Difficulty (độkh ó) 64

## TRANG 68

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 69

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 70

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 71

ca il Ryerss £ <4 4 Ỷ wan `.

¬ề. Ắ ẻ.'-::.

\\ _--=<= >| Er Ay 8blsi= 7a| LÝ. decors

Ca S 2

- --- 7

68

## TRANG 72

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 73

Checkout Go online t+ * ˆ Am f F ge Data aa Data Se ° M Recommendations re) Oo w T Ne

and Product Recommendations `.

Cross sell PS vo

## OOQ.

Market Basket Analysis

70

## TRANG 74

Tư vấn, khuy ến nghịtr ực tuyến

|. Tu vấn, khuyến nghị

Sản phẩm phù hợp và khách hàng có thểquan tâm Sản phẩm khách hàng có ý định mua

Cross-sell

Up-sell

2. Phương pháp

Phân tích ý định mua sắm (purchase intent)

Lọc cộng tác (collaborative filtering) Tư vấn dựa trên nội dung Tư vấn dựa trên patterns mua sắm (frequent patterns, association rules)

71

## TRANG 75

amazon. com Frequently Bought Together ~~)

m(ied =-- - Price for all three: $46.96 (2: ONE + (Add all three to Cart | | Add all three to Wish List Pa Am Show availability and shipping details

#' This item: The Lean Startup: How Today's Entrepreneurs Use Continuous Innovation to Create Ra dically Successful... by Eric Ries Hardcover $14.64

¥%| Zero to One: Notes on Startups, or How to Build the Future by Peter Thiel Hardcover $16.20

' The Hard Thing About Hard Things: Building a Business When There Are No Easy Answers by Ben Horowitz Hardcover $16.12

Frequently Bought Together

Price for all three: $48.78 didi ‘ ’ (GAddalithreeto Cart)| Add al three to Wish List =: Show availability and shipping details

“ This item: Golden Rose Matte Lipstick Set of 6 (SET1) $24.99

) NYX Cosmetics Long Lasting Slim Lip Liner Pencils 6 Colors $15.99

¥) Italia Eyeliners Set of 12 $7.80:72

## TRANG 76

Constructivism: Theo ry, Perspectives, and Practice Paperback - February, 1996 = by Teachers College Press (Author), Catherine Twomey Fosnot (Editor)

- Be the first to review this item

êm 10 New ftom $8.75 - 27 Used from S001 ` g) e

= PERSPECTIVES, Hardcover pend PRACTICE L) Paperback

-_ | oe There is a newer edition of this item:

aaa Twooty 120s EON Constructivism: Theo ry, Perspectives And Practice rowmor IS] wk teks (1)

## easiness_ FREE TWO-DAY SHIPPING FOR COLLEGE STUDENTS

> Learn more amazon-': Jent

Part |, which covers the theo retical aspects of constructivism, includes chapters from Emst von

Glasersfeld, Catherine Twomey Fosnot, and Paul Cobb. In Part II, Candace Julyan, Eleanor Duckworth,

Deborah Schifter, June S. Gould, Rheta De Vries, Betty Zan, and Maxine Greene provide perspectives

from the field. Part Ill, which explores practices in the classroom, features work from Jill Bodner Lester,

Susan Cowey, George Forman, Dewey Dykstra, Jr.

Customers Who Viewed This Item Also Viewed

wot po " com mop bad E07]:

a4

= Constructivism: Theo ry Constructivism in Education - Constructivism and In Search of Understanding Perspectives And Practice Lesie P. Steffe Educstion The.

Catherine Twomey Paperback Marie Larochetle Jacqueline Grennon "tư w‹:: 908.95 Prine tek tek | *ưw t4 73 Paperback Paperback Paperback 346.20 Prine $11.32 Prime

## TRANG 77

Các mặt hàng thường được xem cùng nhau

Số lan được xem cùng nhau: 5

Aquaphor - Kem Váng sữa MEKONGZON - Thuộc bo bà bau Thuốc Siro ho trái THUỐC ELEVIT-

tri ham, cham hoặc MONTBLANC Thuốc Loi Sữa Pregnacare cây tiêt xuat tửl á VITAMIN CHO khô da vani MOTHERLOVE Conception - 30 thường xuân ME TRƯỚC KHI More Milk Plus 60 viên PROSPAN. SINH Viên

SET 2 TÃ VAI Sữa bột Dumex

(QUAN) CHO NG Gold 1 - 800g (cho HAM bẻd ưới 6 thang)

Số lan được xem cùng nhau: 6

` ae ' |jìi =

= $4 3b % 4

Dam SN bông chan Áo So mi pha ren Bộ do bay ngăn AO CHAM BI TAY YD 186-Ke hong Full size that eo DAI CÁCH DIEU

74

## TRANG 78

Các mặt hàng thường được mua cùng nhau

Số lần được mua cùng nhau: 6

r7 TH

Bộ quan ao bẻgai Bộ quan ao bé gai

Eko BN42 Eko BN44

Số lan được mua cùng nhau: 9 Số lần được mua cùng nhau: 9

Áo Sơ mi pha ren HAPPY F - Đảm SHOP THANH Áo thun nam héng Full size Xòe 3 mau TAM- ÁO THUN Abercrombie& NAM COCO Fitch

## BURBERRY

75

## TRANG 79

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user

understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 80

The Joy of Tech:. by Nitrozac & Snaggy

## WHAT IT’S LIKE WHEN YOU

## READ A NEWSPAPER...

## WHAT IT’S LIKE WHEN YOU

## READ NEWS ONLINE...

## AD NETWORK:

## THE NSA ket 3w 4 --- MORENETWORKAD

AD >. | Ụ ANOTHER ~~ M= QU sé FP ø _- FOLKS! NETWORK GUY eee ~ a N Đ SG YAHOO! P= SS RZoe __ TWITTER

## AMAZON - ie \YQ? _ GOOGLE

## ANOTHER @ »

NSA GUY - th z z=) R ips, ___ your Isp

## FACEBOOK - ` x a" ‹

## r2bil =<“§ 1ƒ \OURND SPOUSEDON'T FORGETCHECKING

## “ YOUR HisTORY!

77

## TRANG 81

Hiểu người dùng trực tuyến 5 6 Crt y

Basic information (sex, age, marital status, lived places,...)

ID & contact information (global id, device ids, Ips, email,...)

Education & Employment (schools, employers, skills,...)

Preferences (hobbies, topics of interests, things of interests)

Assets & Income (assets, income,...)

Family and social relationships _ (spouse, family members, friends,...)

Current context information (location, condition, intent,...)

History conditions & actions (purchases, sufferings, birth delivery,...)

78

## TRANG 82

User A:

Sex: female; Age: from 25 to 35 ý 4 Bộ chắn ga gốicó chun Tui Thởi Trang Hãng Zara i Sipe mia hé kiêu Korea Mini Cao Cắp. - an = penn ee: “MAE 299.000VND #99. 0000ND mo Áo sơ mi voan xinh xắn 5:

3449.000 VMD.

## TRANG 83

User A:

Sex: female; Age: from 25 to 35 “J H Bộ chắn gagếicó chun Tui Thởi Trang Hãng Zara II“ solely -2-- NUNG hè kiêu Korea Mini Cao Cấp ` _ -..:-.:›- = Perrine y TẾ cửa Z2060xnp #99,000VND: oe, 299.000VND pune Ao sơ mi voan xinh xắn 349.000 VNO.

User A:

Sex: female; Age: from 25 to 35 lo f.

Marital status: just married Đỗgia dung thủy tinh - Bộ chăn ga gối có chua

- ‘Guetta “ rey THA Ne liêu Korea

= play Ads - reerciel vi E - 6= + ~-

## ị 699.000VNĐ = ì = -.. 299.000VND

h THý © Đảm Và he Tran Cho Cập Di

## TRANG 84

User A:

Sex: female; Age: from 25 to 35 ` ri Ý 4 Bộ chắn 92 gối có chun Tai Thởi Trang Hãng Zara mia hè kiểu Korea Mini Cao Cấp - muachunglb. vr co: “ 299.000VNĐ nan tâyawe Cao Gái Đ Bóng HOB48 Ảo so mi voan xinh xắn 349.000 VNO.

User A:

Sex: female; Age: from 25 to 35 Marital status:: just married Đỏgia dung thủy tính- t Bộ chăn ga gốilucó chun mn;:. Gua” R mùa hé kiểu Korea splay Ads } - -.... "¬neke

## 699.000VNĐ k 299.000VNĐ

L

pies ng " © Đảm Và he Tran Cho Cập Di

User A:

Marital Sex: female;status:Age:marriedfrom 25 to 35 7 Q EEou Condition: being pregnant 2 Bộ chanm ùa hè kiéuga gối Koreacó chun 1Ì toa Í Đô=1...gia đụng thủy tinh-

## „ Fs 299,000VND "; 249k 699,000VND

Đầm bau công sở Sữa PI hysiol ac,

769 0008

## TRANG 85

User A:

Sex: female; Age: from 25 to 35 € ri hg Bỏch ắn ga dối có chun Tai Thởi Trang Hãng Zara mia hè kiểu Korea Mini Cao Cấp - muachunglb. vr co š

Câ ệy 499.000VNO Esvoi Cao Git wb Đứng HOA Ảo sơ mi voan xinh xắn ru 349.000 VNO.

User A:

Sex: female; Age: from 25 to 35 Marital status: just married | chun::: ra giat àng!tà tính - Ea eral berth splay Ads GQ - estes tebe FERED

## 699.000VNĐ. 299.000VNĐ

j

pri ¬ng F © Đảm Và he Tran Cho Cập Di

User A:

Marital status: married „ ` Sex: female; Age: from 25 to 35 7Q EE Condition: being pregnant Bộ chan ga gối có chun. „ Đô gia dụng thủy tĩnh - 2 mùa hè kiéu Korea > Gon | =1...

muachungid vn - i L azadavn:: 720-00046B 259k Soe > 4 5 h el 699,000VND wi 299.000VNĐ Re = 249k Dam bau công sở liệp Lieysiol Hổ 030810 Mom(400g) - 769 0008

User A:

Sex: female; Age: from 25 to 35 Pom ^ Marital status: married ~ 3 -¬ i a | 3 ice -? eu Condition: having baby l Actmni t hoo đa \ - Baa):

i c Tike he P g2) Y Pa, <= -: eee fk Bo ' See “ a ity 7 “£® = 485.000đ GOES ON Mà hột úy họa tức k¿ưng đa dân ng mực Máy chạy bộđi ện Bip 2020

## TRANG 86

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 87

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dụng trong các bài toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyền.

8. Phân tích dữcấu trúc mạng.

## TRANG 88

Churn predictione e

- Demographic data E&gt; Input Information Gathering:

=) - Customer purchases history tent - Service usage

- Product information tw - Billingdata - Marketing data

~~ High Re ‡ Ỉ aah, an” tte of!

of Churn Very Loyal Moderately Loya

Data Analytics Intelligent Segmentation

85

## TRANG 89

z `" ® z ^ z ‘wa 66 xe ° 99 Các bài toán phân tích vê v/d “rời dịch vụ

How can we make it happen?

Prescriptive Analytics dối) What will happen? dộ&gt; -o© Predictive Ce) Analytics ‘ Cy ` LS sở Why did"it happen? co?

= Diagnostic hơi Analytics 2 What h d? ag 2 at happene eo Kở Descriptive = Analytics) 9 Sy Ny sỏi Cy w

Difficulty (độkh ó) 86

## TRANG 90

Dữ liệu viễn thông

|. Thông tin khách hang (customer data)

Thông tin tĩnh

Thông tin động

2. Thông tin thuê bao (contract/plan data)

3. Thông tin sử dụng dịch vụ(call/service detail data)

Hành vi sử dụng Thay đổi trong sử dụng dịch vụ

Ngừng phát sinh cước 4, Lịch sửy êu cầu chăm sóc khách hang (customer care history data)

## .V.V.

87

## TRANG 91

Highly imbalanced data

*

*

a * * * oar i =" * # 5 re +} het gt + É * * ai aint.

* x *

L2

*

*

88

## TRANG 92

Nhận biết vấn đềvà giải pháp

|. Dw liệu rất lớn

2. Quan tâm đặc biệt đến “True positive”

3. Kho khăn khi lấy mẫu (sampling)

4. Khó khăn khi xây dựng mô hình học (thống kê) cho

dữ liệu mất cân bằng (nghi êm trọng)

5. Có thể rời ra c hoá dữ liệu?

6. Khai phá luật hiếm va tin cậy xấp xỉ

Từtập mẫu (sau khi sampling) Luật “xấp xỉ” cho lớp dương (positive)

Lọc với độdo: Conviction Whitebox: dễhi ểu, dễđ ánh giá, và điều chỉnh

89

## TRANG 93

Cácứng dụng thực tiễn

|. Phân lớp, phân loại (classification/decision rules)

2. Phân tích dữ liệu bán lẻ(market basket analysis)

3. Tư vấn trực tuyến (online recommendation)

4. Hiểu người dùng trực tuyến (user understanding)

5. Phân tích tìm ngoại lệ(outlier detection)

6. Ứng dung trong các bai toán viễn thông

(vd: churn prediction)

7. Phân tích dữ liệu di truyên.

8. Phân tích dữcấu trúc mạng.

## TRANG 94

Ứng dụng khai phá dữ liệu viễn thông

|. Dữ liệu

Customer data

Call detail data

Log and content data

Network data

2. Các bai toán khai pha dữ liệu

Spam filtering

Churn prediction

Fraud detection (subscription vs. superimposition)

Customer profiling and segmentation (for marketing)

Network fault isolation and prediction

Service/content recommendation

91

## TRANG 95

Tổng kết bài giảng

|. Khái niệm và định nghĩa

Tap mục, giao dịch, CSDL giao dịch Tập phổbi ến (TPB) và luật kết hợp (LKH)

2. Các phương pháp khai phá TPB và LKH

Phương pháp Apriori

Phương pháp FP-Growth Các phương pháp khác

3. Đánh giá luật kết hợp

4. Cácứng dụng thực tiễn

## TRANG 96

Tài liệu tham khao

@ J. Han, M. Kamber, and J. Pei.

Data Mining: Concepts and Techniques (Chapter 6. Mining Frequent Patterns, Associations, and Correlations: Basic Concepts and Methods; Chapter 7. Advanced Pattern Mining).

The 3rd Edition, Morgan Kaufmann, Elsevier, 2012.

DQ A. Ra jaraman, J. Leskovec, and J. D. Ullman.

Mining of Massive Datasets (6. Frequent Itemsets).

The 2nd Edition, Cambridge University Press, 2013.

@ M. J. Zaki and W. M. Jr.

Data Mining and Analysis: Fundamental Concepts and Algorithms (Il.

Frequent Pattern Mining).

Cambridge University Press, 2013.
