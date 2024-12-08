import requests
print("Welcome to UpE, our new updater.")
print("The update command in LigmaBalls will still work.")
print("What would you like to update?")
print("MurderBob")
print("MurderBob Advanced")
print("LigmaBalls")
print("UpE")
print("Banana Simulator")
program = input("Please select the program you would like to update (CASE-SENSITIVE): ")
if (program == "MurderBob Advanced"):
    print("Alright! Downloading...")
    url = 'https://github.com/Freakybob-Team-Games/murderbobadvanced/blob/main/Code/java/Game.java?raw=true'
    response = requests.get(url)
    file_Path = 'MurderBobAdvanced.java'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            file.close()
    else:
        print('Failed to download file')
if (program == "MurderBob"):
    print("Alright! This will download to the directory this program is in.")
    print("Options:")
    print("1")
    print("2")
    print("2.1")
    print("3")
    print("3.1")
    version = input("What version would you like to download? ")
    if (version == "1"):
        input("WARNING! THIS IS 85.9 MB (shrank in later releases)")
        url = 'https://github.com/Freakybob-Team-Games/MurderBob/blob/main/Releases/1/MurderBob.jar?raw=true'
        response = requests.get(url)
        file_Path = 'MurderBob.jar'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
        else:
            print('Failed to download file')
    if (version == "2"):
        url = 'https://github.com/Freakybob-Team-Games/MurderBob/blob/main/Releases/2/MurderBob.jar?raw=true'
        response = requests.get(url)
        file_Path = 'MurderBob.jar'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
        else:
            print('Failed to download file')
    if (version == "2.1"):
        url = 'https://github.com/Freakybob-Team-Games/MurderBob/blob/main/Releases/2.1/MurderBob.zip?raw=true'
        response = requests.get(url)
        file_Path = 'MurderBob.zip'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
        else:
            print('Failed to download file')
    if (version == "3"):
        url = 'https://github.com/Freakybob-Team-Games/MurderBob/blob/main/Releases/3/MurderBob3.zip?raw=true'
        response = requests.get(url)
        file_Path = 'MurderBob3.zip'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
        else:
            print('Failed to download file')
    if (version == "3.1"):
        url = 'https://github.com/Freakybob-Team-Games/MurderBob/blob/main/Releases/3.1/MurderBob.zip?raw=true'
        response = requests.get(url)
        file_Path = 'MurderBob.zip'
        if response.status_code == 200:
            with open(file_Path, 'wb') as file:
                file.write(response.content)
                print('File downloaded successfully')
                file.close()
        else:
            print('Failed to download file')
if (program == "LigmaBalls"):
    print("Installing to current directory...")
    url = 'https://github.com/Freakybob-Team/lb/blob/main/lb.py?raw=true'
    response = requests.get(url)
    file_Path = 'lb.py'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            file.close()
    else:
        print('Failed to download file')
if (program == "UpE"):
    print("We're downloading the update wizard...")
    url = 'https://github.com/Freakybob-Team-Games/UpE/blob/main/UpDate.py?raw=true'
    response = requests.get(url)
    file_Path = 'UpDate.py'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            file.close()
            exec(open('UpDate.py').read())
    else:
        print('Failed to download file')
if (program == "LigmaBalls"):
    print("Installing to current directory...")
    url = 'https://github.com/Freakybob-Team-Games/lb/blob/main/lb.py?raw=true'
    response = requests.get(url)
    file_Path = 'lb.py'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            file.close()
    else:
        print('Failed to download file')
if (program == "Banana Simulator"):
    print("Installing to current directory...")
    url = 'https://github.com/Freakybob-Team-Games/Banana-Simulator/blob/main/Banana%20Simulator.py?raw=true'
    response = requests.get(url)
    file_Path = 'Banana Simulator.py'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('File downloaded successfully')
            file.close()
    else:
        print('Failed to download file')
    url = 'https://github.com/Freakybob-Team-Games/Banana-Simulator/blob/main/F.json?raw=true'
    response = requests.get(url)
    file_Path = 'F.json'
    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
            print('FreakiFest file downloaded')
            file.close()
    else:
        print('Failed to download FreakiFest (Note: Banana Simulator requires this!)')
