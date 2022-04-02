from core.applock import AppLock
from core.auth import Auth
import getpass
import sys

DEFALUT_PASS = 'Appsafe123'

dummy = Auth(DEFALUT_PASS)
if dummy.IsFirst():
    dummy.createAuth()
    print(f'Authentication Created:\nYour Default Password is: {DEFALUT_PASS}')


VERSION='0.1.0'
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
            print(f'{app.appname} has been locked.')
        else:
            print('Authentication Failiure')
            quit()


def unlock(path_to_binary):
    app = AppLock(path_to_binary)
    if not app.IsLocked():
        print(f'{app.appname} is not locked successfully.')
        quit()
    else:
        password = getpass.getpass(prompt='Passworcd: ', stream=None)
        auth = Auth(password)
        auth.validate()
        if auth.IsAuthenticated:
            app.unlock(app.appname)
            print(f'{app.appname} has been unlocked sucessfully.')
        else:
            print('Authentication Failiure')
            quit()

menu = """
1: Lock
2: Unlock
3: Version
4: Change Password
5: Exit
"""
print(menu)
option = input('Choose Option: ')
if option == '1':
    path = input('Enter path: ')
    lock(path)
elif option == '2':
    path = input('Enter path: ')
    unlock(path)
elif option == '3':
    print(f'Version: v{VERSION}')
elif option == '4':
    old_passwd = getpass.getpass(prompt='Old Password:', stream=None)
    new_passwd = input('New Password: ')
    chpass = Auth(old_passwd)
    chpass.validate()
    chpass.ChangePasswd(new_passwd)
elif option == '5':
    print('Bye...')
    quit()
else:
    print('Wrong Option')


