# Đăng feature caches lên Kaggle / Google Drive

Bộ mã nguồn GitHub không bao gồm mảng `.npy` dung lượng lớn.

## Bộ nén dữ liệu ngoài dự kiến

`CA-PFG_Frozen_Features_Kaggle_External.zip` được tạo từ năm cache đã gửi,
manifest và metadata chuẩn hóa. Cấu trúc trong ZIP:

```
features/dinov2_small/plantdoc_features.npy
features/dinov2_small/plantvillage_features.npy
features/resnet50/plantdoc_resnet50_features.npy
features/resnet50/plantvillage_resnet50_features.npy
features/oxford102/oxford102_resnet50_features.npy
metadata/dinov2_small/*.csv
metadata/resnet50/*.csv
metadata/oxford102/oxford102_metadata.csv
splits/manifest_split.csv
```

**Không công bố URL file lớn trong README/manuscript trước khi upload và thử tải công khai.**

## Phương án 1: Kaggle Dataset
1. Trên Kaggle, chọn **Datasets → New Dataset → Upload** và chọn file ZIP dữ liệu.
2. Kiểm tra nhãn giấy phép (license) phù hợp với điều khoản của PlantDoc/PlantVillage/Oxford và chính sách về các đặc trưng phát sinh; nếu chưa được phép chia sẻ, giữ Dataset ở trạng thái **Private**.
3. Nếu được phép công bố, đặt Public và ghi lại URL chính thức, phiên bản. Không khẳng định đã công khai nếu còn Private.
4. Khi chạy notebook, attach Kaggle Dataset và dùng `scripts/extract_feature_bundle.py`
   để bung ZIP ra `/kaggle/working/capfg_input` (giữ nguyên tên file). Các notebook có bước auto-discovery vẫn cần được chạy thử trong một session mới.
5. Ghi lại chính xác slug dataset và version vào `docs/EXTERNAL_DOWNLOAD_LINKS.md`.

## Phương án 2: Google Drive
1. Upload ZIP dữ liệu vào một thư mục lưu trữ riêng.
2. Chọn quyền **Anyone with the link → Viewer** chỉ khi chắc chắn được phép công bố tệp.
3. Mở link ở cửa sổ ẩn danh để kiểm tra download và lưu URL, kích thước, SHA-256.
4. Người dùng tải ZIP về máy hoặc kết nối file vào Kaggle qua phương thức họ được phép sử dụng.

## Kiểm tra SHA-256
Dùng `docs/FEATURE_CACHE_INDEX.json` và công cụ `scripts/extract_feature_bundle.py --verify-only`
để kiểm tra `.npy` sau khi giải nén. Nếu file khác hash, **không tự đổi thứ tự hàng**.

Nguồn dữ liệu gốc được dẫn tại `docs/DATA_SOURCES_AND_RIGHTS.md`.
