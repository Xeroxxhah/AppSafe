import hashlib
import os
import string

class Auth():

    def __init__(self,paswd):
        self.password = paswd
        if not self.password:
            print('Provide Passowrd')
            quit()
        self.IsAuthenticated = False
        self.shadowPath = os.getenv('HOME')+'/.appsafe.shadow'
    
    def createAuth(self):
        if os.path.exists(self.shadowPath):
            return
        """if len(self.password) < 8 or string.ascii_uppercase not in self.password:
            print('Password Must be at least 8 chars and must contain 1 uppercase char')
            quit()"""
        with open(self.shadowPath, 'w') as shadow:
            shadow.write(hashlib.sha256(self.password.encode()).hexdigest())
        shadow.close()
    
    def validate(self):
        with open(self.shadowPath, 'r') as readShadow:
            content = readShadow.read().strip('')
            if str(content) == str(hashlib.sha256(self.password.encode()).hexdigest()):
                self.IsAuthenticated = True
        readShadow.close()
    
    def ChangePasswd(self,new_passwd):
        if self.IsAuthenticated:
            with open(self.shadowPath, 'w') as chngpass:
                chngpass.write(hashlib.sha256(str(new_passwd).encode()).hexdigest())
            chngpass.close()
        else:
            print('Authentication Failiure')
            quit()
    
    def IsFirst(self):
        if os.path.exists(self.shadowPath) and os.path.getsize(self.shadowPath) > 0:
            return False
        else:
            return True







