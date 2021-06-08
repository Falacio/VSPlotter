import os
import subprocess as sp
import sys


class PlotObject:
    def __init__(self, log_name, config):
        self.args = config['args']['k']
        self.exec = os.path.join(config['chia_path'], config['command'])
        self.log_dir = config['log_directory']
        self.log_name = log_name
        self.process = None
        self.log_lines = 0
        self.phase = 1

    def start_plotter(self):
        """
        comando = f"{self.chia_path}/{self.__command}" 
        for par,val in self.params.items():
            if val:
                if par == 't2': par = '2'
                comando += f" -{par} {val}"
        print(comando)
        """
        comando = f"{self.exec} {self.args} {self.log_dir} {self.log_name}"
        self.process = sp.Popen(comando, stdout=sp.PIPE, stderr=sp.STDOUT, bufsize=1, universal_newlines=True, creationflags=sp.CREATE_NEW_CONSOLE)
        
    def check(self):
        with open(os.path.join(self.log_dir, self.log_name), 'r') as logfile:
            self.log_lines = sum(1 for _ in logfile)
        
        if self.log_lines > 35:
            self.phase = 4
        elif self.log_lines > 19:
            self.phase = 3
        elif self.log_lines > 13:
            self.phase = 2

        return self.process.poll()