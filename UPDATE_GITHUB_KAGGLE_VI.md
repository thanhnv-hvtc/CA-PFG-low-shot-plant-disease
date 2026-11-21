# Cập nhật GitHub với Kaggle Feature Caches

Nguồn dữ liệu được người dùng cung cấp: https://www.kaggle.com/datasets/nguynvnthanhhvtc/capfg-feature-caches

## 1. Kiểm tra Kaggle trước khi công bố
1. Vào trang Dataset > Settings/Sharing và kiểm tra chế độ Public nếu điều kiện chia sẻ cho phép.
2. Mở Kaggle Notebook mới, Add Input -> `capfg-feature-caches`.
3. Dùng lệnh `!find /kaggle/input -name "*.npy" | head -30` để xem tên file.
4. Sử dụng script `scripts/verify_kaggle_feature_caches.py` (copy vào notebook) hoặc đoạn code ngắn trong `docs/FEATURE_INPUTS_GUIDE.md` để soát shapes. Với chế độ `--full-hash`, đối chiếu đủ 5 mã SHA-256.
5. Xác nhận không có ảnh nguồn bị chia sẻ trái phép.

## 2. Cập nhật GitHub bằng GitHub Desktop
1. Nhấn **Show in Explorer** trong GitHub Desktop.
2. Giải nén tệp ZIP cập nhật này, **chỉ sao chép README.md, docs/* và scripts/verify_kaggle_feature_caches.py** vào thư mục repo clone, ghi đè theo yêu cầu. Không chép thêm `UPDATE_GITHUB_KAGGLE_VI.md` nếu không muốn.
3. Trong GitHub Desktop: xem tab Changes, điền Summary: `Document external Kaggle feature caches`, chọn Commit to main -> Push origin.
4. Mở README GitHub và bấm thử link Kaggle.

## 3. Phát hành
- Khi kiểm tra quyền chia sẻ và dữ liệu hợp lệ, chuyển Kaggle Dataset và GitHub repository sang Public.
- Giữ mã nguồn và manifest trên GitHub; giữ năm `.npy` tại Kaggle.
- Không đổi sắp xếp hàng của file feature.
- Trong bản thảo, chèn URL **GitHub công khai chính xác** (chưa có URL xác minh ở bước này) và URL Kaggle Dataset nêu trên.
- Dẫn Oxford Flowers 102 bằng tham khảo [24] và trang nguồn Oxford; không viết rằng Oxford được dùng huấn luyện CA-PFG.
