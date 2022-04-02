import os
import stat

class Agent():

    def __init__(self,agentPath):
        self.agentPath = agentPath
        self.symlinkName = os.path.basename(self.agentPath)

    def CreateAgent(self):
        agent_content = ''
        with open('core/agent', 'r') as agent:
            agent_content = agent.read()
        agent.close()
        agent_content = agent_content.replace('APP-PATH-HERE', self.agentPath+'.applock')
        with open(self.agentPath, 'w') as appAgent:
            appAgent.write(agent_content)
        appAgent.close()
        os.chmod(self.agentPath, 0o755)

