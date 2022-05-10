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

        self.shadowPath = os.path.join(os.getenv('HOME'),'.appsafe.shadow')
        self.secretPath = os.path.join(os.getenv('HOME'),'.appsafe.secret')
        self.secretQuestion = os.path.join(os.getenv('HOME'),'.appsafe.question')

    
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
    
    def resetPasswords(self, secret):
        if os.path.exists(self.secretPath):
            with open(self.secretPath, 'r') as secretf:
                secrettbm = secretf.read().strip()
                if str(secrettbm) == str(hashlib.sha256(secret.encode()).hexdigest()):
                    newPassword = input('Enter New Password: ')
                    with open(self.shadowPath, 'w') as chngpass:
                        chngpass.write(hashlib.sha256(newPassword.encode()).hexdigest())
                    chngpass.close()
                else:
                    print(f'file: {secrettbm}, given: {hashlib.sha256(secret.encode()).hexdigest()}')
                    print('Wrong Secret...')
        else:
            print('Something went wrong...')

    def createSecret(self, secquestion , secret):
        if os.path.exists(self.secretPath):
            return
        else:
            with open(self.secretQuestion, 'w') as question:
                question.write(secquestion)
            question.close()
            with open(self.secretPath, 'w') as secretf:
                secretf.write(hashlib.sha256(secret.encode()).hexdigest()) 
            secretf.close()
    
    def getSecQuestion(self):
        with open(self.secretQuestion,'r') as question:
            return str(question.read().strip(''))













