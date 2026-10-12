import os

class DirectoryInspector:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.gif')

    def get_all_files(self):
        file_list = []
        total_size = 0
        
        for item in os.listdir(self.directory_path):
            full_path = os.path.join(self.directory_path, item)
            if os.path.isfile(full_path):
                file_list.append(item)
                total_size += os.path.getsize(full_path)
                
        return file_list, total_size

    def get_image_files(self):
        image_list = []
        total_image_size = 0
        
        for item in os.listdir(self.directory_path):
            full_path = os.path.join(self.directory_path, item)
            if os.path.isfile(full_path) and item.lower().endswith(self.image_extensions):
                image_list.append(item)
                total_image_size += os.path.getsize(full_path)
                
        return image_list, total_image_size

if __name__ == "__main__":
    target_dir = "."  
    inspector = DirectoryInspector(target_dir)

    all_files, total_size = inspector.get_all_files()
    print("=== All Files ===")
    for f in all_files:
        print(f" - {f}")
    print(f"Total size: {total_size:,} bytes\n")

    img_files, total_img_size = inspector.get_image_files()
    print("=== Image Files Only (.jpg, .gif, .png) ===")
    for img in img_files:
        print(f" - {img}")
    print(f"Total image size: {total_img_size:,} bytes")