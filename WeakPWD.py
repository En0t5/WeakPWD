import argparse

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

def replace_keywords_in_file(keywords):

    # 读取rule.txt文件内容
    with open('rule.txt', 'r') as file:
        template_content = file.read()

    # 生成最终内容
    final_content = ""

    # 对每个关键字进行替换
    for keyword in keywords:
        replaced_content = template_content.replace('%username%', keyword)
        final_content += replaced_content + "\n"  # 每个替换后的内容之间加入一个换行

    # 将替换后的内容写入password.txt文件
    with open('password.txt', 'w') as file:
        file.write(final_content)

    print("Replacement complete. Check password.txt for results.")

if __name__ == '__main__':
    logo()
    # 设置参数解析器
    parser = argparse.ArgumentParser(usage='\npython3 %(prog)s -keys keyword\npython3 %(prog)s -keys key1,key2',description='Replace username in rule.txt with single or multiple keywords.')
    parser.add_argument('-keys', '--keywords', required=True, help='Comma-separated keywords or a single keyword to replace username with')

    # 解析命令行参数
    args = parser.parse_args()

    # 处理传入的关键字参数
    keywords = args.keywords.split(',')

    # 调用函数并传入关键字列表
    replace_keywords_in_file(keywords)
