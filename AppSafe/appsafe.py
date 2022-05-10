from .core.applock import AppLock
from .core.auth import Auth
from .core.version import Version
import getpass
import sys
import os

DEFALUT_PASS = 'Appsafe123'

dummy_auth = Auth(DEFALUT_PASS)
dummy_app = AppLock('/usr/bin/ls')
version = Version()

if dummy_auth.IsFirst():
    dummy_auth.createAuth()
    dummy_app.createConf()
    print('Create your secrect in case you forgot your password')
    question = input('Enter your security question: ')
    secret = input('Enter your security secret: ')
    dummy_auth.createSecret(question, secret)
    print(f'Authentication Created:\nYour Default Password is: {DEFALUT_PASS}')


option = ''

def lock(path_to_binary):
    app = AppLock(path_to_binary)
    if app.IsLocked():
        print(f'{app.appname} is already locked.')
        quit()
    else:
        password = getpass.getpass(prompt='Password: ', stream=None)
        auth = Auth(password)
        auth.validate()
        if auth.IsAuthenticated:
            app.lock(app.appname)
            print(f'{app.appname} has been locked successfully.')
        else:
            print('Authentication Failiure')
            quit()


def unlock(path_to_binary):
    app = AppLock(path_to_binary)
    if not app.IsLocked():
        print(f'{app.appname} is not locked.')
        quit()
    else:
        password = getpass.getpass(prompt='Password: ', stream=None)
        auth = Auth(password)
        auth.validate()
        if auth.IsAuthenticated:
            app.unlock(app.appname)
            print(f'{app.appname} has been unlocked sucessfully.')
        else:
            print('Authentication Failiure')
            quit()

def ShowApps():
    show = AppLock('/usr/bin/ls')
    show.showLockedApps()

if not version.IsUpdated():
    print(f'New version available {version.updatedVersion}')

menu = """
1: Lock
2: Unlock
3: Version
4: Change Password
5: Show Locked Apps
6: Reset Password
7: Exit
"""

def main():
    if os.geteuid() != 0:
        print('Run as root...')
        quit()
    print(menu)
    option = input('Choose Option: ')
    if option == '1':
        path = input('Enter path: ')
        lock(path)
    elif option == '2':
        path = input('Enter path: ')
        unlock(path)
    elif option == '3':
        print(f'Version: {version.currentVersion}')
    elif option == '4':
        old_passwd = getpass.getpass(prompt='Old Password:', stream=None)
        new_passwd = input('New Password: ')
        chpass = Auth(old_passwd)
        chpass.validate()
        chpass.ChangePasswd(new_passwd)
    elif option == '5':
        ShowApps()
    elif option == '6':
        print('Reset Password')
        reset = Auth(DEFALUT_PASS)
        print('Security Question:')
        print(reset.getSecQuestion())
        secret = input('Enter Secret: ')
        reset.resetPasswords(secret)
    elif option == '7':
        print('Bye...')
        quit()
    else:
        print('Wrong Option')

if __name__ == "__main__":
    main()

