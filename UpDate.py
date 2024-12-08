import requests
import os
print("Hello! This is the updater for UpE.")
islegacy = input("Are you updating from UpD? Y/N ")
url = 'https://github.com/Freakybob-Team-Games/UpE/blob/main/UpE.py?raw=true'
response = requests.get(url)
if (islegacy == "Y"):
    os.remove("UpD.py")
    print("Successfully removed UpD Legacy!")
file_Path = 'UpE.py'
if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
        print('File downloaded successfully')
        file.close()
        exec(open('UpE.py').read())
else:
    print('Failed to download file')
