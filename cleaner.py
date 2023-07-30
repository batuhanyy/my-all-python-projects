import os
import shutil
import time

def delete_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"{file_path} dosyası silindi.")
            except Exception as e:
                print(f"Hata: {e}")
        elif os.path.isdir(file_path):
            # Recursive call to delete files in subdirectories
            delete_files_in_folder(file_path)
            # Remove empty subdirectories after deleting files
            try:
                os.rmdir(file_path)
                print(f"{file_path} klasörü silindi.")
            except Exception as e:
                print(f"Hata: {e}")


temp = "C:\\Windows\\Temp\\"
tempb = "C:\\Users\\murat\\AppData\\Local\\Temp\\"
prefetch = "C:\\Windows\\Prefetch\\"

# Kontrol edilecek klasörün varlığını doğrulayın
if os.path.exists(prefetch) and os.path.isdir(prefetch) or os.path.exists(temp) and os.path.isdir(temp) or os.path.exists(tempb) and os.path.isdir(tempb):
    # Klasördeki dosyaları ve alt klasörleri silin
    delete_files_in_folder(prefetch)
    delete_files_in_folder(temp)
    delete_files_in_folder(tempb)
else:
    print(f"{prefetch} klasörü bulunamadı veya bir dosya değil.")
    print(f"{tempb} klasörü bulunamadı veya bir dosya değil.")
    print(f"{tempb} klasörü bulunamadı veya bir dosya değil.")
time.sleep(3)