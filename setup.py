

import pip
import os

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def addToPath():
    from os.path import expanduser
    home = expanduser("~")
    pasta = os.getcwd()
    os.chdir(home)
    path = ''
    with open('.bashrc', 'a') as file:
        file.write('\nexport PATH="$PATH:' + pasta + '/"')
# Example

def createExecutable():
	os.system('chmod +x autologin.py')

if __name__ == '__main__':
    # install('beautifulsoup4')
		createExecutable()
		addToPath()
