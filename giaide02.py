"""
1-A
2-A
3-A
3-A
4-A
5-A
6-A
7-A
8-A
9-A
10-A
11-A
12-A
13-A
14-A ()
15-A ()
16-A
17-A ()
18-A ()
19-A
20-A ()
21-A
22-A
23-A
24-A    
25-A
26-A
27-A()
28-A()
29-A
30-A 
Câu 31:
- Mục tiêu của tầng bronze là lưu trữ dữ liệu thô, chưa qua xử lý, từ các nguồn dữ liệu khác nhau. Dữ liệu ở tầng này thường được lưu trữ dưới dạng nguyên bản, không có bất kỳ biến đổi hay làm sạch nào. Tầng bronze giúp bảo tồn dữ liệu gốc và cung cấp một nguồn dữ liệu đáng tin cậy cho các tầng tiếp theo.
    + Bổ sung thêm cột metadata(siêu dữ liệu) để lưu trữ thông tin về nguồn dữ liệu, thời gian thu thập, và các thông tin liên quan khác. Điều này giúp dễ dàng theo dõi và quản lý dữ liệu trong quá trình xử lý.
    + Kiểu dữ liệu trong tầng bronze có thể bao gồm các định dạng như JSON, CSV, Parquet, hoặc các định dạng nhị phân khác. Việc lựa chọn định dạng phụ thuộc vào loại dữ liệu và yêu cầu xử lý sau này. Tác dụng là để tránh mất dữ liệu và đảm bảo tính toàn vẹn của dữ liệu trong quá trình lưu trữ và truy xuất.
    + Bảng phù hợp cho tầng bronze có thể là bảng lưu trữ dữ liệu thô, với các cột đại diện cho các trường dữ liệu từ nguồn gốc. Ví dụ, nếu dữ liệu đến từ một API, bảng có thể có các cột như "id", "timestamp", "data", và "metadata". Tác dụng là để tổ chức dữ liệu một cách có cấu trúc và dễ dàng truy xuất.
    + Bảng snapshot/Append-only có thể được sử dụng trong tầng bronze để lưu trữ dữ liệu theo thời gian. Bảng snapshot lưu trữ trạng thái dữ liệu tại một thời điểm cụ thể, trong khi bảng Append-only cho phép thêm dữ liệu mới mà không thay đổi dữ liệu cũ. Tác dụng là để theo dõi sự thay đổi của dữ liệu theo thời gian và duy trì lịch sử dữ liệu.
- Mục tiêu của tầng silver là làm sạch, chuẩn hóa và biến đổi dữ liệu từ tầng bronze. Dữ liệu ở tầng này thường được xử lý để loại bỏ các giá trị thiếu, chuẩn hóa định dạng, và thực hiện các biến đổi cần thiết để dữ liệu trở nên dễ sử dụng hơn. Tầng silver giúp tạo ra dữ liệu chất lượng cao hơn, sẵn sàng cho các phân tích và mô hình hóa.
    + Chuẩn hóa dữ liệu: Đổi string ở bronze thành dạng chuẩn, ví dụ: chuyển đổi tất cả các chuỗi thành chữ thường, loại bỏ khoảng trắng thừa, và chuẩn hóa định dạng ngày tháng. Tác dụng là để đảm bảo tính nhất quán của dữ liệu và dễ dàng so sánh giữa các bản ghi.
    + Làm sạch dữ liệu: Loại bỏ các giá trị thiếu hoặc không hợp lệ, và loại bỏ các bản ghi trùng lặp. Tác dụng là để nâng cao chất lượng dữ liệu và giảm thiểu lỗi trong quá trình phân tích.
    + Khóa và quan hệ : 
        - Tạo các khóa chính và khóa ngoại để duy trì tính toàn vẹn của dữ liệu. Ví dụ, nếu có bảng sản phẩm và bảng đơn hàng, có thể tạo khóa ngoại từ bảng đơn hàng đến bảng sản phẩm để đảm bảo rằng mỗi đơn hàng liên kết với một sản phẩm hợp lệ. Tác dụng là để duy trì mối quan hệ giữa các bảng và đảm bảo dữ liệu liên quan được liên kết đúng cách.
        - Tạo các chỉ mục (index) trên các cột thường xuyên được truy vấn để cải thiện hiệu suất truy vấn. Ví dụ, nếu thường xuyên tìm kiếm theo "product_id", có thể tạo chỉ mục trên cột này. Tác dụng là để tăng tốc độ truy vấn và giảm thời gian phản hồi.
    + Bảng thực tế (Fact table) : Dữ liệu giao dịch, sự kiện có hành động(đơn hàng, thanh toán ,,). Schema cần có các cột đo lường (metrics, measures) và các cột tham chiếu (dimension keys) để liên kết với các bảng dimension. Tác dụng là để lưu trữ dữ liệu chi tiết về các sự kiện và giao dịch, phục vụ cho việc phân tích và báo cáo.
    + Bảng mapping/Bridge : Dữ liệu mapping giữa các bảng dimension và fact. Schema cần có các cột khóa chính và khóa ngoại để duy trì mối quan hệ giữa các bảng. Tác dụng là để liên kết dữ liệu từ các bảng khác nhau và hỗ trợ việc phân tích dữ liệu phức tạp.
- Mục tiêu của tầng gold là cung cấp dữ liệu đã được xử lý và tối ưu
    + 

+ Bronzer : _id : string, time_stamp : datetime, user_id_db: string, devide_id : string, ip : string, user_agent: string, product_id : string, collection : string, optine : object sử dụng khi nào mua nhiều hàng, string sử dụng khi không có đơn hàng nào 
+ Silver  : product( product_id primary key, devide _id), USER(user_id_db primary key,  ), collection(collection primary key, product_id foreign key, user_id_db foreign key)

Câu 32: 
- grain là purchase
- fact table là purchase, dimension table là product, user, collection
- 4 dimension table là dim_products( PK: product_key, ), dim_users( PK: user_key ), dim_colletion( PK: collection_key ), dim_time( PK: time_key )
- measure là purchase_amount, purchase_quantity, purchase_discount, purchase_total
- paritition là partition theo time_stamp, clustering là clustering theo product_id, user_id_db, collection
Câu 33:

- bottleneck ở đây được xác định như sau : 31/40 * 100 = 77.5% > 70% => bottleneck mà transofrm chỉ có 3 phút : 31 + 2 + 4 = 37 phút, 37/40 * 100 = 92.5% > 70% => bottleneck. Vậy thì bottleneck là mongodb read, vì nó chiếm > 70% thời gian thực hiện.
- Các experiment để cải thiện bottleneck:
    + Tăng số lượng thread trong ThreadPoolExecutor để tăng khả năng xử lý song song
    + Sử dụng batch processing để giảm số lượng truy vấn đến MongoDB
    + Sử dụng caching để lưu trữ kết quả truy vấn phổ biến và giảm tải cho MongoDB
    + Sử dụng indexing trong MongoDB để cải thiện tốc độ truy vấn
- Metrics (chỉ số giám sát) để đo lường hiệu quả của các experiment:
    + Sử dụng broadcast Join cho bảng dimension để giảm số lượng dữ liệu cần truyền qua mạng và cải thiện hiệu suất join.
    + Tăng sức mạnh tính toán (Scale-out cluster) bằng cách thêm nhiều node vào cluster để tăng khả năng xử lý song song và giảm thời gian thực hiện.
    + tối ưu logic code ở tầng Silver (bỏ bớt các hàm biến đổi chuỗi không cần thiết, Regex nặng)
- Threadig có ích khi giảm tải được thời gian chờ đợi I/O, nhưng nếu bottleneck là CPU-bound thì threading sẽ không giúp cải thiện hiệu suất đáng kể. Trong trường hợp này, nếu bottleneck là MongoDB read (I/O-bound), thì multithreading có thể giúp cải thiện hiệu suất bằng cách cho phép nhiều truy vấn được thực hiện song song, giảm thời gian chờ đợi và tăng throughput. Tuy nhiên, nếu bottleneck là CPU-bound (ví dụ: xử lý dữ liệu phức tạp), thì multithreading sẽ không mang lại lợi ích đáng kể và cần xem xét các giải pháp khác như tối ưu hóa thuật toán hoặc sử dụng multiprocessing.

"""

