# Code Archive Tools

一个简单而实用的工具集，用于将项目代码打包成单个文本文件，方便与AI大模型进行交互，并能完整还原原始的文件结构。

## 功能特性

- 📦 **代码打包**: 将整个项目目录的代码文件合并到一个文本文件中
- 🔄 **完整还原**: 从打包的文本文件中完整还原原始的目录结构和文件内容
- 🎯 **智能过滤**: 自动过滤常见的代码文件类型（.py, .txt, .json, .sh, .jsonl）
- 🚫 **忽略缓存**: 自动忽略 `__pycache__` 等缓存目录
- 🔒 **编码安全**: 确保所有文件都是UTF-8编码，避免编码问题

## 使用场景

- 🤖 **AI代码审查**: 将项目代码发送给AI大模型进行代码审查、优化建议
- 📚 **代码分享**: 快速分享完整的项目代码结构
- 💾 **代码备份**: 创建项目代码的文本格式备份
- 🔄 **版本传输**: 在不同环境间传输项目代码

## 工具说明

### 1. parse_files_to_one_txt.py - 代码打包工具

将项目目录中的所有代码文件打包成一个文本文件。

**用法:**
```bash
python parse_files_to_one_txt.py <输入文件夹> <输出txt文件>
```

**示例:**
```bash
python parse_files_to_one_txt.py ./my_project ./my_project_archive.txt
```

### 2. decode_one_txt_to_files.py - 代码还原工具

从打包的文本文件中还原出完整的项目目录结构。

**用法:**
```bash
python decode_one_txt_to_files.py <输入txt文件> <输出文件夹>
```

**示例:**
```bash
python decode_one_txt_to_files.py ./my_project_archive.txt ./restored_project
```

## 支持的文件类型

当前版本支持以下文件类型：
- `.py` - Python源代码
- `.txt` - 文本文件
- `.json` - JSON配置文件
- `.sh` - Shell脚本
- `.jsonl` - JSON Lines文件

## 文件格式说明

打包后的文本文件使用特殊的标记格式来分隔不同的文件：

```
DaViD_>>>FILE_START>>>
DaViD_path: relative/path/to/file.py
DaViD_name: file.py
DaViD_<<<CONTENT_START>>>
[文件内容]
DaViD_<<<CONTENT_END>>>
DaViD_>>>FILE_END>>>
```

## 注意事项

- ⚠️ 所有文件必须是UTF-8编码，否则会报错并退出
- 📁 自动忽略 `__pycache__` 目录
- 🔄 还原时会自动创建必要的目录结构
- 📝 相对路径会被保持，确保目录结构完整性

## 快速开始

1. **克隆或下载项目**
2. **打包你的项目代码**:
   ```bash
   python parse_files_to_one_txt.py /path/to/your/project project_code.txt
   ```
3. **将生成的txt文件发送给AI大模型进行分析**
4. **如需还原代码**:
   ```bash
   python decode_one_txt_to_files.py project_code.txt ./restored_project
   ```