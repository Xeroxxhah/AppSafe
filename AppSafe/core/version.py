import requests
import json

class Version():

    def __init__(self):

        self.currentVersion = 'V1.4.1'
        try:
            self.updatedVersion = str(requests.get('https://api.github.com/repos/Xeroxxhah/appsafe/releases/latest').json().get('body'))
        except:
            self.updatedVersion = None
            print('An Error Ocurred: Could not check latest version.')
    

    def IsUpdated(self):
        if self.currentVersion == self.updatedVersion:
            return True
        return False



