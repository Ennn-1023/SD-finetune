import os
import glob

# 定義目錄
raw_dir = "./dataset_2025_03/val_data/origin/"
fixed_dir = "./dataset_2025_03/val_data/fixed/"
mask_dir = "./dataset_2025_03/val_data/masks/"
out_dir = "./dataset_2025_03/val_data/"
'''
# 批量處理 raw
for file_path in glob.glob(os.path.join(raw_dir, "*.jpg")):
    base_name = os.path.basename(file_path)  # 取得原始檔名
    new_name = os.path.join(raw_dir, base_name.replace(".jpg", "_raw.jpg"))
    os.rename(file_path, new_name)

# 批量處理 fixed
for file_path in glob.glob(os.path.join(fixed_dir, "*.jpg")):
    base_name = os.path.basename(file_path)
    new_name = os.path.join(raw_dir, base_name.replace(".jpg", "_fixed.jpg"))
    os.rename(file_path, new_name)

# 批量處理 mask
for file_path in glob.glob(os.path.join(mask_dir, "*.jpg")):
    base_name = os.path.basename(file_path)
    new_name = os.path.join(raw_dir, base_name.replace(".jpg", "_mask.jpg"))
    os.rename(file_path, new_name)
'''
raw_dir = "./dataset_2025_03/val_data/reshaped/"
for file_path in glob.glob(os.path.join(raw_dir, "*.jpg")):
    base_name = os.path.basename(file_path)  # 取得原始檔名
    new_name = os.path.join(out_dir, base_name)
    os.rename(file_path, new_name)
for file_path in glob.glob(os.path.join(mask_dir, "*.jpg")):
    base_name = os.path.basename(file_path)
    new_name = os.path.join(out_dir, base_name.replace(".jpg", "_mask.jpg"))
    os.rename(file_path, new_name)
print("檔案重新命名完成！")
