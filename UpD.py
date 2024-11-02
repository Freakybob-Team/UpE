import requests
print("Welcome to UpD, our new updater.")
print("The update command in LigmaBalls will still work.")
print("What would you like to update?")
print("MurderBob")
print("Project M")
print("LigmaBalls")
print("UpD")
program = input("Please select the program you would like to update (CASE-SENSITIVE): ")
if (program == "Project M"):
    print("I'm pretty sure this is a teaser. Or not. I don't know.")
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
        url = 'https://github.com/Freakybob-Team/MurderBob/blob/main/Releases/1/MurderBob.jar?raw=true'
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
        url = 'https://github.com/Freakybob-Team/MurderBob/blob/main/Releases/2/MurderBob.jar?raw=true'
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
        url = 'https://github.com/Freakybob-Team/MurderBob/blob/main/Releases/2.1/MurderBob.zip?raw=true'
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
        url = 'https://github.com/Freakybob-Team/MurderBob/blob/main/Releases/3/MurderBob3.zip?raw=true'
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
        url = 'https://github.com/Freakybob-Team/MurderBob/blob/main/Releases/3.1/MurderBob.zip?raw=true'
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
if (program == "UpD"):
    print("We're downloading the update wizard...")
    url = 'https://github.com/Freakybob-Team/UpD/blob/main/UpDate.py?raw=true'
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