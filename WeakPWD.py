import argparse
import os

def logo():
    print('''
    __       __                      __        _______   __       __  _______  
    /  |  _  /  |                    /  |      /       \ /  |  _  /  |/       \ 
    $$ | / \ $$ |  ______    ______  $$ |   __ $$$$$$$  |$$ | / \ $$ |$$$$$$$  |
    $$ |/$  \$$ | /      \  /      \ $$ |  /  |$$ |__$$ |$$ |/$  \$$ |$$ |  $$ |
    $$ /$$$  $$ |/$$$$$$  | $$$$$$  |$$ |_/$$/ $$    $$/ $$ /$$$  $$ |$$ |  $$ |
    $$ $$/$$ $$ |$$    $$ | /    $$ |$$   $$<  $$$$$$$/  $$ $$/$$ $$ |$$ |  $$ |
    $$$$/  $$$$ |$$$$$$$$/ /$$$$$$$ |$$$$$$  \ $$ |      $$$$/  $$$$ |$$ |__$$ |
    $$$/    $$$ |$$       |$$    $$ |$$ | $$  |$$ |      $$$/    $$$ |$$    $$/ 
    $$/      $$/  $$$$$$$/  $$$$$$$/ $$/   $$/ $$/       $$/      $$/ $$$$$$$/  
                                                                                
                                                                                
                                                                                
''')

def replace_keywords_in_file(keywords, dict_file=None):
    try:
        # 读取rule.txt文件内容
        with open('rule.txt', 'r') as file:
            template_content = file.read()

        # 生成最终内容
        final_content = []

        # 对每个关键字进行替换
        for keyword in keywords:
            replaced_content = template_content.replace('%username%', keyword)
            final_content.append(replaced_content.rstrip())  # 移除每个内容末尾的空白字符

        # 如果提供了字典文件，读取并合并内容
        if dict_file and os.path.exists(dict_file):
            with open(dict_file, 'r') as file:
                dict_content = file.read().rstrip()  # 移除字典内容末尾的空白字符
                final_content.append(dict_content)

        # 将替换后的内容写入password.txt文件
        with open('password.txt', 'w') as file:
            file.write('\n'.join(final_content) + '\n')  # 使用join合并内容，并确保文件以单个换行符结束

        print("Replacement complete. Check password.txt for results.")

    except FileNotFoundError:
        print("Error: 'rule.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    logo()
    # 设置参数解析器
    parser = argparse.ArgumentParser(
        usage='\npython3 %(prog)s -keys keyword [-w dict_file]\npython3 %(prog)s -keys key1,key2 [-w dict_file]\npython3 %(prog)s -kf keys_file [-w dict_file]',
        description='Replace username in rule.txt with single or multiple keywords and optionally merge with a dictionary file.'
    )
    
    # 创建互斥参数组
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-keys', '--keywords', help='Comma-separated keywords or a single keyword to replace username with')
    group.add_argument('-kf', '--keyfile', help='Path to a file containing keywords, one per line')
    
    parser.add_argument('-w', '--dict', help='Path to an existing dictionary file to merge with the final content')

    # 解析命令行参数
    args = parser.parse_args()

    # 处理关键字参数
    if args.keywords:
        keywords = args.keywords.split(',')
    else:
        try:
            with open(args.keyfile, 'r') as f:
                keywords = [line.strip() for line in f if line.strip()]
            if not keywords:
                print("Error: Key file is empty.")
                exit(1)
        except FileNotFoundError:
            print(f"Error: Key file '{args.keyfile}' not found.")
            exit(1)
        except Exception as e:
            print(f"Error reading key file: {e}")
            exit(1)

    # 调用函数并传入关键字列表和字典文件路径
    replace_keywords_in_file(keywords, args.dict)
