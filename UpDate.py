import requests
print("Hello! This is the updater for UpD.")
url = 'https://github.com/Freakybob-Team/UpD/blob/main/UpD.py?raw=true'
response = requests.get(url)
file_Path = 'UpD.py'
if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
        file.close()
        exec(open('UpD.py').read())
else:
    print('Failed to download file')