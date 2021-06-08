import json
import subprocess as sp
import os
import sys
import time

from visualplotter.plotter.queue import QueueObject
from visualplotter.profiles import config_rw as js

class VsPlotter:
    def __init__(self):
        self.log_name = 'STDlog.log'
        self.queues = []
        self.pool = []
        self.stagger_queues_time = 1

    def create_queue(self, plot_profile, temp, final, plots, phase1, max, name):
        config = {
            "profile": plot_profile,
            "temp_dir": temp,
            "final_dir": final,
            "queue_plots": plots,
            "phase1_max": phase1,
            "queue_max": max
        }
        js.write_config(name, config)

    def run(self):
        print('Aquí está')
        for i in range (1,3):
            queue_name = f'Queue-{i}.json'
            self.create_queue('Default_profile.json', 'D:\Temp', 'E:\Plots', 4, 1, 3, queue_name)
            process = sp.Popen(f'python ./visualplotter/visualplotter/start_queue.py {queue_name}')
            self.queues.append(process)
            time.sleep(self.stagger_queues_time)
        while len(self.queues) > 0:
            for process in self.queues:
                if process.poll() != None:
                    if process.returncode != 0:
                        print('ERROR DE COLA')
                    else:
                        print('COLA OK')
                    self.queues.remove(process)
                time.sleep(2)


    
    def create_profile(self, dir='C:\\Users\\Usuario\\Documents\\GitHub\\Falacio\\VSPlotter\\visualplotter\\profiles', name='STDProfile.json'):
        info_profile = dict(
            chia_path = 'C:\\Users\\Usuario\\Documents\\GitHub\\Falacio\\VSPlotter\\test_program',
            log_directory = 'C:\\Users\\Usuario\\Documents\\GitHub\\Falacio\\VSPlotter\\test_program\\Logs',
            command = 'chia plots create',
            args = dict(
                k = 32,             #k size
                n = 1,              #Number of plots
                b = 3390,           #Buffer
                f = '',             #Farmer Public Key
                p = '',             #Pool Public Key
                a = '',             #Fingerprint
                t = 'D:\Temp',      #Temp Dir
                t2 = '',            #Second Temp Disk
                d = 'E:\Plots',     #Final Dir
                r = 2,              #Threads
                u = 128,            #Buckets
                e = False,          #Deactivate bitfield
                x = False           #Skip final disk
            )
        )
        with open(os.path.join(dir,name), 'w') as mi_profl:
            json.dump(info_profile,mi_profl, indent=4)

#test = VsPlotter()
#test.run()