import sys
from visualplotter.plotter import queue

def main(args=None):
    print(sys.argv)
    args = sys.argv[1]
    q = queue.QueueObject(args)
    q.start()

if __name__=='__main__':
        sys.exit(main())