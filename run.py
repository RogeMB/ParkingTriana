import sys
from main import main_terminal

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        main_terminal.almacenar()
        main_terminal.iniciar()

    # Contraseña ADMIN: 1234

    # else:
    #    app = ui.MainWindow()
    #    app.mainloop()

    # El else para construir la interfaz gráfica en el pc
