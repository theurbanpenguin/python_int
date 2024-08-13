# Path to the hosts file on a Windows system
hosts_file = r"C:\Windows\System32\drivers\etc\hosts"

# Open the file in read mode and print its content
try:
    with open(hosts_file, 'r') as file:
        hosts_content = file.read()
        print(hosts_content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
