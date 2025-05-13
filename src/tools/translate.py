#!/usr/bin/env python
import os

# 定义tools文件夹路径
tools_folder = os.path.join(os.getcwd(), 'src', 'tools')

# 直接遍历tools文件夹下的子文件夹
for sub_dir in os.listdir(tools_folder):
    sub_dir_path = os.path.join(tools_folder, sub_dir)
    if os.path.isdir(sub_dir_path):
        language_dir_path = os.path.join(sub_dir_path, 'language')
        
        # 检查language文件夹是否存在，不存在则创建
        if not os.path.exists(language_dir_path):
            os.makedirs(language_dir_path)
            print(f"已在 {sub_dir_path} 中创建 language 文件夹")
        else:
            print(f"{sub_dir_path} 中已存在 language 文件夹，跳过创建")

        lang = ['zh', 'en', 'de', 'es', 'fr', 'no', 'pt', 'uk', 'vi', 'jp']
        for i in lang:
            # 在language文件夹内创建.md文件
            md_file_path = os.path.join(language_dir_path, f'{sub_dir}.{i}.md')
            
            # 检查文件是否存在，不存在则创建
            if not os.path.exists(md_file_path):
                with open(md_file_path, 'w', encoding='utf-8') as f:
                    f.write("")
                print(f"已在 {language_dir_path} 中创建 {sub_dir}{i}.md 文件")
            else:
                print(f"{md_file_path} 文件已存在，跳过创建")