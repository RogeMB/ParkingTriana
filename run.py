import sys
from main import main_terminal

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        main_terminal.iniciar()
    # else:
    #    app = ui.MainWindow()
    #    app.mainloop()
