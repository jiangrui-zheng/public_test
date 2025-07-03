import json
import os

def backup_github_token():
    """
    Reads a GitHub token from ../security.json and saves it to token_backup.txt.
    """
    try:
        # Path to security.json in the parent directory
        security_json_path = "../security.json"

        # Read the token from security.json
        with open(security_json_path, 'r') as f:
            data = json.load(f)

        # Save the content to token_backup.txt
        with open("token_backup.txt", 'w') as f:
            json.dump(data, f, indent=4)

        print("Token backup successful!")

    except FileNotFoundError:
        print(f"Error: {security_json_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {security_json_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    backup_github_token()
