import subprocess

urls_file = 'ftps.txt'

download_directory = 'xyz'

def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

ftp_urls = read_urls(urls_file)

for url in ftp_urls:
    print(url)
    command = 'rsync '+'-avz ' +url +' '+ str(download_directory)
    print(command)
    break
    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded: {url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {url}: {e}")

print("All downloads completed.")
