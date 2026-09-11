"""
1-A
2-A
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
28-A
29-A
30-A
Câu 31:
    - Chúng ta sẽ chuyển nó về 1 dạng thống nhất là array<object>
    def normalize_option(option):
        if option is None:
            return [], None
        if isinstance(option, list):
            return [option], None
        if isinstance(optin, list) and all(isinstance(x,dict) for x in option):
            return option, None
        return None, "INVALID_OPTION_FORMAT"

Câu 32 :
    - Grain ở đây được xác định như sau, mỗi 1 dòng của bảng là 1 sự kiện đại diện do 1 người dùng hoặc là 1 thiết bị tạo ra cho 1 sản phẩm tại 1 thời điểm cụ thể
(vd: 1 người dùng đang đại diện cho 1 lựa chọn cho 1 sản phẩm hoặc là 1 thiết bị đang đại diện cho việc lựa chọn sản phẩm )
    - Chúng ta có thể thiết kể bảng như sau để phù hợp với các event document đã cho : 
    events
    -----------------------------
    even_id          String/ PK
    event_time       Timestamp
    event_date       DATE
    user_id          String
    device_id        String
    product_id       String
    current_url      String
    Referrer_url     String
    Collection       String

    - Chill table option
    event_options 
    --------------------------------
    event_id         String
    option_id        String
    option_label     String
    valua_id         String
    value_label      String

    - Keys :  
        + events.event_id : PK
        + event_options.event_id nó là FK của events.event_id

    - Type : 
    event_id        STRING
    event_time      TIMESTAMP
    event_date      DATE
    user_id         STRING
    device_id       STRING
    product_id      STRING
    current_url     STRING
    referrer_url    STRING

    option_id       STRING
    option_label    STRING
    value_id        STRING
    value_label     STRING

    - Partition By event_date

    - Trade-off nghĩa là: Khi bạn chọn một phương án, bạn nhận được một số lợi ích nhưng đồng thời phải chấp nhận một số bất lợi.
Child table
events
+
event_options

Ưu điểm:

schema rõ
SQL analytics dễ
one-to-many rõ ràng
option filtering/grouping dễ

Nhược điểm:

tăng số rows
cần JOIN
ETL phức tạp hơn

    - Nested array: Nested = dữ liệu con được giữ bên trong record cha. Child table = lấy dữ liệu con đó ra thành bảng riêng rồi liên kết lại bằng key.
gần source BSON
ít JOIN
giữ event + options cùng nhau

Nhược điểm:

phải UNNEST
query option phức tạp hơn
engine phải hỗ trợ nested tốt

Một câu trả lời rất ổn trong bài thi là:

Nếu workload thường xuyên phân tích option độc lập, tôi chọn child table. Nếu warehouse hỗ trợ nested tốt và query thường đọc toàn bộ event cùng options, tôi có thể giữ ARRAY<STRUCT>. Quyết định dựa trên query pattern.

Câu 33:   

    
"""