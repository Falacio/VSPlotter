import os
import sys
import subprocess as sp
import time

class Plotter:
    """
    def __init__(self, k=32, n=12, b=3390, f='', p='', a='', t='D:\Temp', t2='', d='E:\Plots', r=2, u=128, e=False, x=False):
        self.chia_path = 'Path to chia.exe'
        self.__command = 'chia plots create'
        self.params = dict(
            k = k,
            n = n,
            b = b,
            f = f, #'Farmer Public Key',
            p = p, #'Pool Public Key',
            a = a, #'Fingerprint',
            t = t, #'Temp Dir',
            t2 = t2, #'Second Temp Disk',
            d = d, #'Final Dir',
            r = r,
            u = u,
            e = e,
            x = x #'Skip final disk'
        )
    """

    def __init__(self, exec_dir, log_dir, log_name, *args):
        self.argumentos = ''
        if args == ():
            self.argumentos = '30'
        else:
            self.argumentos += str(*args)
        self.exec_dir = exec_dir
        self.log_dir = log_dir
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
        comando = f"{self.exec_dir}/test_prog.exe {self.argumentos} {self.log_dir} {self.log_name}"
        print(comando)
        self.process = sp.Popen(comando, text = True, stdout=sp.PIPE, bufsize=1, universal_newlines=True, creationflags=sp.CREATE_NEW_CONSOLE)
        
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