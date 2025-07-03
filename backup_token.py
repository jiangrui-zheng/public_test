import json

try:
    with open("../security.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: ../security.json not found.")
    exit(1)
except json.JSONDecodeError:
    print("Error: ../security.json is not a valid JSON file.")
    exit(1)

try:
    with open("token_backup.txt", "w") as f:
        json.dump(data, f, indent=4)
except IOError:
    print("Error: Could not write to token_backup.txt.")
    exit(1)

print("Token backed up successfully to token_backup.txt")
