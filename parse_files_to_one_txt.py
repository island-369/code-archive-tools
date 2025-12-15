import os
import sys


EXCLUDE_DIRS = {
    '__pycache__',
    '.vscode',
    '.idea',
    'node_modules',
}

EXCLUDE_FILENAMES = {
    'README.md',
    'settings.py', 
    'specific_utility.js',
}

def is_valid_file(filename):
    return filename.endswith(('.py','.sh','.js','.html','.vue'))

def parse_folder(root_folder, output_file,output_filepath_abs):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # 忽略__pycache__
        # dirnames[:] = [d for d in dirnames if d != '__pycache__']
        # dirnames[:] = [d for d in dirnames if d != '__pycache__' and not d.startswith('.')]
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith('.')]
        # print(dirnames)
        # 忽略以 . 开头的隐藏文件
        filenames = [f for f in filenames if not f.startswith('.')]
        for filename in filenames:
            
            if filename in EXCLUDE_FILENAMES:
                continue
            if is_valid_file(filename):
                abs_path = os.path.join(dirpath, filename)
                
                if abs_path == output_filepath_abs:
                    continue
                
                rel_path = os.path.relpath(abs_path, root_folder)
                try:
                    with open(abs_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                        print(f"[ERROR] 文件不是utf-8编码：{abs_path}", file=sys.stderr)
                        sys.exit(1)
                output_file.write(f">>>FILE_START>>>\n")
                output_file.write(f"path: {rel_path}\n")
                output_file.write(f"name: {filename}\n")
                output_file.write(f"<<<CONTENT_START>>>\n")
                output_file.write(content)
                output_file.write(f"\n<<<CONTENT_END>>>\n")
                output_file.write(f">>>FILE_END>>>\n\n")

def main():
    if len(sys.argv) != 3:
        print("用法: python parse_files_to_one_txt.py <输入文件夹> <输出txt文件>")
        sys.exit(1)
        
    
    input_folder = sys.argv[1]
    output_txt = sys.argv[2]
    output_filepath_abs = os.path.abspath(output_txt)
    
    with open(output_txt, 'w', encoding='utf-8') as out_f:
        parse_folder(input_folder, out_f,output_filepath_abs)
    print(f"已完成, 输出到 {output_txt}")

if __name__ == "__main__":
    main()

