# BẮT ĐẦU TẠI ĐÂY — Đăng bộ CA-PFG lên GitHub

## Cần tải và đẩy file nào?

**GitHub:** file tải về `CA-PFG_GitHub_PUBLISH_v3.zip` là gói nguồn đã kiểm tra. **Hãy giải nén** và tải các tệp/thư mục bên trong lên repository GitHub. GitHub không tự giải nén một ZIP được upload như một file.

**Kaggle hoặc Google Drive (tùy chọn, sau khi kiểm tra giấy phép):** năm feature cache `.npy` lớn **không nằm trong ZIP GitHub**. Bạn đã cung cấp đủ các nguồn: `features_DINOv2.rar`, `features_ResNet50.zip`, `oxford102_resnet50_features.npy` và `oxford102_metadata.csv`. Để gộp thành một ZIP dữ liệu riêng, sử dụng `scripts/build_external_bundle_from_sources.py` sau khi giải nén RAR bằng WinRAR/7-Zip (lệnh mẫu bên dưới).

## Đẩy GitHub bằng GitHub Desktop (Windows)

1. Đăng nhập GitHub → New repository → `CA-PFG-low-shot-plant-disease` → Public. **Không** chọn tạo README/license mới.
2. Giải nén `CA-PFG_GitHub_PUBLISH_v3.zip` trên máy.
3. Mở GitHub Desktop → File → Clone repository; chọn repository vừa tạo.
4. Sao chép **toàn bộ nội dung** của thư mục `CA-PFG_GitHub_PUBLISH_v3` (chứ không phải file ZIP) vào thư mục clone.
5. GitHub Desktop → Commit to main → Push origin. Kiểm tra README và CSV mở công khai được.
6. Xem `docs/PUBLISH_GITHUB.md` để có lệnh Git nếu thích.

## Kiểm tra bộ mã nguồn

Từ thư mục đã giải nén, cài `numpy`, `pandas`; chạy lần lượt:

```bash
python scripts/verify_release.py
python scripts/verify_candidates.py
python scripts/verify_input_metadata.py
```

Các kiểm tra trên chỉ xác minh CSV kết quả/metadata; **không** tuyên bố đã huấn luyện lại đầy đủ từ ảnh gốc.

## Gộp feature caches thành một ZIP bên ngoài GitHub

1. Giải nén `features_DINOv2.rar` bằng WinRAR/7-Zip, ví dụ vào `D:\CA-PFG\DINO_unpacked`.
2. Giữ `features_ResNet50.zip` và `oxford102_resnet50_features.npy` nguyên trạng.
3. Từ thư mục repository đã giải nén, chạy:

```bash
python scripts/build_external_bundle_from_sources.py --dino-dir "D:/CA-PFG/DINO_unpacked" --resnet-zip "D:/CA-PFG/features_ResNet50.zip" --oxford-npy "D:/CA-PFG/oxford102_resnet50_features.npy" --output "D:/CA-PFG/CA-PFG_Frozen_Features_Kaggle_External.zip"
```

Script so sánh SHA-256 của **5** file feature với checksum từ thực nghiệm gốc. Sau khi được phép chia sẻ, upload ZIP kết quả lên Kaggle Dataset hoặc Google Drive, rồi điền URL thật vào `docs/EXTERNAL_DOWNLOAD_LINKS.md`.

Để dùng ZIP trên Kaggle, gắn ZIP làm Input và giải nén vào `/kaggle/working/capfg_input` trước khi chạy notebook. Có script `scripts/extract_feature_bundle.py` hỗ trợ xác minh SHA-256. Nên thử **một task** trong phiên Kaggle mới trước khi tuyên bố khả năng tái lập đầy đủ.

## Còn cần người dùng xác nhận gì?

- Chọn giấy phép cho **mã nguồn** với đồng tác giả.
- Xác minh quyền chia sẻ **derived feature caches** từ các bộ dữ liệu, đặc biệt nếu muốn đặt Kaggle Dataset công khai.
- Sau khi upload: xác minh URL truy cập công khai và kiểm tra tải xuống không yêu cầu đăng nhập đặc biệt.
- Điền URL repository **thật** vào bản thảo và Revision Response; không điền trước khi upload.

**Không cần bổ sung file thực nghiệm mới** để tạo bộ GitHub này; các bảng kết quả, manifest, metadata, candidate-level results và năm feature caches đều đã có. Không có dữ liệu ảnh gốc trong gói.
