import os
import sys
import time

class MyProgram:
    def __init__(self, number=35, log_dir='.\Logs', log_name='test.log'):
        self.full_path = os.path.join(log_dir, log_name)
        self.number = int(number)
    
    def run(self):
        with open (self.full_path, 'w') as log_file:
            log_file.write('Cabecera, bla, bla, bla. \n')
            log_file.write('Otra Cabecera, bla, bla, bla. \n\n')
            
        for i in range(0,9):
            target = self.fibonacci(self.number)
            print(target)
            with open (self.full_path, 'a') as log_file:
                log_file.write(str(target)+'\n')
            time.sleep(2)
        with open (self.full_path, 'a') as log_file:
                log_file.write('End of phase 1\n\n')
        
        for i in range(0,4):
            print(target)
            target = self.fibonacci(self.number//4)
            with open (self.full_path, 'a') as log_file:
                log_file.write(str(target)+'\n')
            time.sleep(2)
        with open (self.full_path, 'a') as log_file:
                log_file.write('End of phase 2\n\n')
        
        for i in range(0,14):
            target = self.fibonacci(self.number-3)
            print(target)
            with open (self.full_path, 'a') as log_file:
                log_file.write(str(target)+'\n')
            time.sleep(2)
        with open (self.full_path, 'a') as log_file:
                log_file.write('End of phase 3\n\n')
        
        for i in range(0,4):
            target = self.fibonacci(self.number//4)
            print(target)
            with open (self.full_path, 'a') as log_file:
                log_file.write(str(target)+'\n')
            time.sleep(2)
        with open (self.full_path, 'a') as log_file:
                log_file.write('End of phase 4\n\n')

    
    def fibonacci(self,n):
        if n == 0 or n == 1:
            return n
        else: return (self.fibonacci(n-1) + self.fibonacci(n-2))


def main(args=None):
    args = sys.argv
    arguments = []
    print(args)
    if len(args) > 1:
        for i in range(1,len(args)):
            print(args[i])
            arguments.append(args[i])
            app = MyProgram(*arguments)
    else:
        app = MyProgram()
    app.run()
    
if __name__=='__main__':
    sys.exit(main())