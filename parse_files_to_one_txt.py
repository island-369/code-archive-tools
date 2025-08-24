import os
import sys

def is_valid_file(filename):
    return filename.endswith(('.py','.txt','.json','.sh','jsonl'))

def parse_folder(root_folder, output_file):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # 忽略__pycache__
        dirnames[:] = [d for d in dirnames if d != '__pycache__']
        for filename in filenames:
            if is_valid_file(filename):
                abs_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(abs_path, root_folder)
                try:
                    with open(abs_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                        print(f"[ERROR] 文件不是utf-8编码：{abs_path}", file=sys.stderr)
                        sys.exit(1)
                output_file.write(f"DaViD_>>>FILE_START>>>\n")
                output_file.write(f"DaViD_path: {rel_path}\n")
                output_file.write(f"DaViD_name: {filename}\n")
                output_file.write(f"DaViD_<<<CONTENT_START>>>\n")
                output_file.write(content)
                output_file.write(f"\nDaViD_<<<CONTENT_END>>>\n")
                output_file.write(f"DaViD_>>>FILE_END>>>\n\n")

def main():
    if len(sys.argv) != 3:
        print("用法: python parse_files_to_one_txt.py <输入文件夹> <输出txt文件>")
        sys.exit(1)
    input_folder = sys.argv[1]
    output_txt = sys.argv[2]
    with open(output_txt, 'w', encoding='utf-8') as out_f:
        parse_folder(input_folder, out_f)
    print(f"已完成, 输出到 {output_txt}")

if __name__ == "__main__":
    main()

