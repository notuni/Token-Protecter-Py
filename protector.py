import subprocess
TOKEN_FILE = "token.txt" # Create a file storing your token for the protector to understand and protect
def get_token():
    with open(TOKEN_FILE, "r") as f:
        return f.read().strip()
def main():
    # Retrieve the token
    token = get_token() # Retreiving your token you created
    subprocess.Popen(["/path/to/discord/application", "--token", token]) # Launching discord using this token with subprocess
if __name__ == "__main__":
    main()
