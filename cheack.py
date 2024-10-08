import os

def find_non_utf8_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    f.read()
            except UnicodeDecodeError:
                print(f"File with encoding issue: {file_path}")

# 替换为你的项目路径
find_non_utf8_files('.')
