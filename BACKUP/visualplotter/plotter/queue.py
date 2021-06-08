
import time
from visualplotter.plotter.plot import PlotObject
from visualplotter.profiles import config_rw as js

class QueueObject:

    def __init__(self, name):
        self.name = name.replace('.json', '')
        self.config = js.read_config(name)
        self.plot_config = js.read_config(self.config["profile"])
        self.queue = []

    def start(self):
        for i in range(1, self.config["queue_plots"]+1):
            log_name = f"{self.get_time()}-{self.name}-Plot-{i}.log"
            plot = PlotObject(log_name, self.plot_config)
            plot.start_plotter()
            self.queue.append(plot)
            time.sleep(1)
            while plot.check() == None and plot.phase == 1:
                    print(f"proceso ID: {plot.process.pid}")
                    print('esperando')
                    time.sleep(2)
            while len(self.queue) >= self.config["queue_max"]:
                for plot in self.queue:
                    if plot.check() != None:
                        print(plot.process.pid)
                        if plot.process.returncode != 0:
                            print('ERROR DE PLOTEO')
                        else:
                            print('PLOT OK')
                        self.queue.remove(plot)
                    else:
                        print(f"ID: {plot.process.pid} phase: {plot.phase}")
                time.sleep(2)

    def get_time(self):
        _time = time.localtime()
        return f"{_time[0]:02d}-{_time[1]:02d}-{_time[2]:02d}--{_time[3]:02d}_{_time[4]:02d}_{_time[5]:02d}"
