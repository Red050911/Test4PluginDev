# Test4PluginDev
A way for plugin developers to test their plugins without building a server themselves. Name stands for Testing for Plugin Development.
# Description
There has always been a problem with developing Minecraft plugins compared to developing mods. This problem is that you cannot test them without manually building a server!
Test4PluginDev simplifies this process with a single Python script that downloads a server jar, copies your plugin to the directory and starts up the server!
# Install
To install Test4PluginDev, follow the instructions below.
### Windows
First, download Python 3 for Windows at [this link](https://www.python.org/downloads/windows/). Then, install it and go to your project directory.
Now, run the command below in the root directory of your project.
```batch
curl -o testproject.py https://raw.github.com/Red050911/Test4PluginDev/master/testproject.py
```
Now you have it set up! You can run testproject.py to test your project.
### Linux
First, download Python 3 for your distribution. Use your distro's way of getting Python to do it. An example for Debian and derivatives is
```shell
sudo apt install python3
```
Now that you have Python installed, go to your project's root directory and run:
```shell
curl -o testproject.py https://raw.github.com/Red050911/Test4PluginDev/master/testproject.py
```
Now you have it set up! You can run testproject.py to test your project.
# Usage
You can test your project by running
```cmd
python testproject.py YOUR_PLUGIN_FILENAME
```
Or the more unsupported but still works way:
```cmd
python testproject.py
```
in your OS terminal.
# Attention
If you use Git for version control, make sure to include these two lines in your gitignore!
```gitignore
testproject.py
testing/
```

*I am not affiliated with Mojang, Git, Python, PaperMC, or Microsoft*
