# Hướng dẫn ngắn (tiếng Việt)

Bộ mã nguồn này bao gồm notebook nguyên gốc của các lần chạy và CSV test đã sửa đúng, kèm kiểm tra tự động với Table 3/Table 6. Các file lớn `.npy`, `manifest_split.csv`, metadata tương ứng và CSV candidate gốc từ NB10/NB11 chưa có trong bộ tệp để đóng gói, nên **chưa thể tuyên bố tái lập end-to-end chỉ từ ZIP này**.

**Công việc còn lại trên Kaggle:** tìm và xuất `manifest_split.csv`, các `*_metadata.csv` và các bộ feature cache DINOv2/ResNet50. Xem `MISSING_BEFORE_FULL_REPRODUCTION.md`. Các file trên 100 MB không đưa vào GitHub thường; lưu nguồn tải riêng nếu giấy phép cho phép.

Chạy `python scripts/verify_release.py` sau `pip install numpy pandas` để kiểm tra 480 dòng kết quả test, các bảng kiểm định và các biến thể DC. Notebook 12 v3 đã sửa lỗi validation/test, không sử dụng lại Notebook 12 v2 cho bản thảo sửa. Data Availability cần thêm Oxford Flowers 102 [24], trang gốc https://www.robots.ox.ac.uk/~vgg/data/flowers/102/; Oxford chỉ là thống kê nguồn cho DC-Adapted, không phải dữ liệu đào tạo CA-PFG.
