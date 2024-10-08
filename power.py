import subprocess


class Powershell:
    def __init__(self) -> None:
        self.output = None
        self.error_output = None
    
    def _execute(self, cmd: str):
        res = subprocess.run(['Powershell', '-Command', cmd],
                              capture_output=True, text=True)
        
        if res.stderr:
            self.error_output = res.stderr
        else:
            self.output = res.stdout
            return res.stdout

    def create_user(self):
        pass

    def add_user(self):
        pass

    def rmv_user(self):
        pass

    def greet_user(self):
        return self._execute(cmd='Write-Output "Hi :)"')
    

pwsh = Powershell()
pwsh.greet_user()
