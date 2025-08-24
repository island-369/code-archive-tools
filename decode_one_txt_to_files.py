import os
import sys

def decode_txt_to_files(input_txt, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(input_txt, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.startswith('DaViD_>>>FILE_START>>>'):
            # 读取文件信息
            path = None
            name = None
            idx += 1
            while idx < len(lines):
                if lines[idx].startswith('DaViD_path: '):
                    path = lines[idx][12:].strip()
                elif lines[idx].startswith('DaViD_name: '):
                    name = lines[idx][12:].strip()
                elif lines[idx].startswith('DaViD_<<<CONTENT_START>>>'):
                    idx += 1
                    content_lines = []
                    while idx < len(lines) and not lines[idx].startswith('DaViD_<<<CONTENT_END>>>'):
                        content_lines.append(lines[idx])
                        idx += 1
                    content = ''.join(content_lines)
                    # 写入文件
                    abs_path = os.path.join(output_folder, path)
                    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                    with open(abs_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(content)
                    break
                idx += 1
        idx += 1
    print(f"还原完成,输出到{output_folder}")

def main():
    if len(sys.argv) != 3:
        print("用法: python decode_one_txt_to_files.py <输入txt文件> <输出文件夹>")
    input_txt = sys.argv[1]
    output_folder = sys.argv[2]
    decode_txt_to_files(input_txt, output_folder)

if __name__ == "__main__":
    main()

                    
