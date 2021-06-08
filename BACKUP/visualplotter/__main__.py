import sys

from visualplotter.visualplotter.vsplotter import VsPlotter

def main(args=None):
    app = VsPlotter()
    app.run()

if __name__=='__main__':
        sys.exit(main())