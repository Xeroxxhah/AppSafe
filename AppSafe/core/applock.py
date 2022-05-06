from .agent import Agent
import pyAesCrypt
import os
import stat



class AppLock():
    

    def __init__(self, apppath):
        if os.path.exists(apppath):
            self.apppath = apppath
        else:
            print('File Does not Exist...')
            quit()
        self.appname = os.path.basename(self.apppath)
        self.APP = os.getenv('HOME')+'/.appsafe.apps'
        
    def IsLocked(self):
        with open(self.APP, 'r') as app:
            data = app.readlines()
            for x in data:
                if self.appname == x.split(':')[0]:
                    return True
            return False

    def lock(self, password):
        try:
            destpath = self.appname+'.applock'
            pyAesCrypt.encryptFile(self.apppath, f'{self.apppath.replace(self.appname, destpath)}', password)
            with open(self.APP, 'a') as app:
                app.write(f'{self.appname}:{self.apppath}\n')
            os.unlink(self.apppath)
            agent = Agent(self.apppath)
            agent.CreateAgent()
        except Exception as e:
            print(f'Following error ocurred: {e}')


    def unlock(self, password):
        try:
            os.unlink(self.apppath)
            orgpath = self.appname+'.applock'
            pyAesCrypt.decryptFile(f'{self.apppath.replace(self.appname, orgpath)}', self.apppath, password)
            with open(self.APP, 'r') as log:
                content_log = log.read()
            log.close()
            content_log = content_log.replace(f'{self.appname}:{self.apppath}\n', '')
            with open(self.APP, 'w') as applog:
                applog.write(content_log)
            applog.close()
            os.chmod(self.apppath, 0o755)
            os.remove(self.apppath+'.applock')
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f'Following error ocurred: {e}')


    def showLockedApps(self):
        with open(self.APP, 'r') as apps:
            data = apps.readlines()
            for app in data:
                print(app.split(':')[0])
    
    def createConf(self):
        if os.path.exists(self.APP):
            return
        else:
            with open(self.APP,'w') as app:
                pass

