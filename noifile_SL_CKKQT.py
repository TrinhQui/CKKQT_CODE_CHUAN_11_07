import os
import pandas as pd

# Thư mục chứa các file Excel cần nối
folder_path = r"D:\BVHNVD_2022"

# Danh sách các file Excel trong thư mục
excel_files = [file for file in os.listdir(folder_path) if file.endswith(".xlsx")]

# Đối tượng DataFrame để lưu dữ liệu từ các file Excel
merged_data = pd.DataFrame()

# Đọc dữ liệu từ các file Excel và nối chúng vào merged_data
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Lưu merged_data vào file Excel mới
output_file_path = os.path.join(folder_path, "CKKQT_BVHNVD_SL_NOI_FILE.xlsx")
merged_data.to_excel(output_file_path, index=False)

print("Đã nối các file Excel thành công và lưu vào file CKKQT_SL_NOI_FILE.xlsx!")
