import requests
import json

class Version():

    def __init__(self):

        self.currentVersion = 'V1.2.16'
        self.updatedVersion = str(requests.get('https://api.github.com/repos/Xeroxxhah/appsafe/releases/latest').json().get('body'))
    

    def IsUpdated(self):
        if self.currentVersion == self.updatedVersion:
            return True
        return False



