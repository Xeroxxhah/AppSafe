import os
import stat

class Agent():

    def __init__(self,agentPath):
        self.agentPath = agentPath
        self.symlinkName = os.path.basename(self.agentPath)
        self.agent_content = """#!/usr/bin/python3

from easygui import msgbox

msg = msgbox('This App is Locked by Appsafe.', 'AppSafe')
"""

    def CreateAgent(self):
        with open(self.agentPath, 'w') as appAgent:
            appAgent.write(self.agent_content)
        appAgent.close()
        os.chmod(self.agentPath, 0o755)

