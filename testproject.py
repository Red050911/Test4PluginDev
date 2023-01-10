# _________ _______  _______ _________    ___    _______  _                 _______ _________ _        ______   _______
# \__   __/(  ____ \(  ____ \\__   __/   /   )  (  ____ )( \      |\     /|(  ____ \\__   __/( (    /|(  __  \ (  ____ \|\     /|
#    ) (   | (    \/| (    \/   ) (     / /) |  | (    )|| (      | )   ( || (    \/   ) (   |  \  ( || (  \  )| (    \/| )   ( |
#    | |   | (__    | (_____    | |    / (_) (_ | (____)|| |      | |   | || |         | |   |   \ | || |   ) || (__    | |   | |
#    | |   |  __)   (_____  )   | |   (____   _)|  _____)| |      | |   | || | ____    | |   | (\ \) || |   | ||  __)   ( (   ) )
#    | |   | (            ) |   | |        ) (  | (      | |      | |   | || | \_  )   | |   | | \   || |   ) || (       \ \_/ /
#    | |   | (____/\/\____) |   | |        | |  | )      | (____/\| (___) || (___) |___) (___| )  \  || (__/  )| (____/\  \   /
#    )_(   (_______/\_______)   )_(        (_)  |/       (_______/(_______)(_______)\_______/|/    )_)(______/ (_______/   \_/

# Code licensed under the MIT License

# MIT License

# Copyright (c) 2022 Red050911

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import requests
import os
import hashlib
import sys
import os.path

print("Building...")
os.system("mvn clean install")
print("Checking testing directory...")
try:
    os.mkdir("testing")
except OSError as error:
    print("Directory already exists, skipping")
print("Refreshing server.jar...")
r = requests.get(url = "https://api.papermc.io/v2/projects/paper/versions/1.19.3")
data = r.json()
print("Received 1.19.3 build data")
print(data)
latestBuild = data["builds"][len(data["builds"]) - 1]
r = requests.get(url = "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/" + str(latestBuild))
data = r.json()
print("Received latest DL information")
print(data)
print("Downloading from https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/" + str(latestBuild) + "/downloads/" + data["downloads"]["application"]["name"])
dl = requests.get("https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/" + str(latestBuild) + "/downloads/" + data["downloads"]["application"]["name"])
with open("newsrv.jar", "wb") as file:
    file.write(dl.content)
print("Checking file hash...")
hash = hashlib.sha256()
with open("newsrv.jar", "rb") as file:
    for block in iter(lambda: file.read(4096), b""):
        hash.update(block)
readableHash = hash.hexdigest()
print("SHA256 Hash: " + readableHash)
if(not readableHash == data["downloads"]["application"]["sha256"]):
    sys.exit("Hash does not match. Try running the program again!")
else:
    print("Hash check succeeded.")
os.replace("newsrv.jar", "testing/server.jar")
if(not os.path.exists("testing/eula.txt")):
    print("To run a Minecraft server, you must agree to the Minecraft End User License Agreement.")
    print("We will now generate the required files to agree.")
    cwd = os.getcwd()
    os.chdir("testing")
    os.system("java -Xms1024M -Xmx1024M -jar server.jar")
    os.chdir(cwd)
    print("Please go into the testing folder, open eula.txt and change eula=false to eula=true to agree.")
    input("Press ENTER once you have agreed")
print("Creating plugins folder...")
try:
    os.mkdir("testing/plugins")
except OSError as error:
    print("Directory already exists, skipping")
pluginFile = "Plugin-1.0.jar"
if(len(sys.argv) > 1):
    pluginFile = sys.argv[1]
else:
    print("Please enter the name of your plugin file. We will automatically find it in your target folder. Tip: Add your plugin filename to the app arguments to skip this dialog!")
    pluginFile = input("Please enter your plugin filename: ")
try:
    os.replace("target/" + pluginFile, "testing/plugins/tested-plugin.jar")
except OSError as error:
    sys.exit("Plugin file does not exist!")
print("Starting your testing server!")
cwd = os.getcwd()
os.chdir("testing")
os.system("java -Xms1024M -Xmx1024M -jar server.jar")
os.chdir(cwd)
# End Test4PluginDev script
