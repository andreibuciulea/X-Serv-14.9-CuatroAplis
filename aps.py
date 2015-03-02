#!/usr/bin/python

import webappmulti
import socket
import random
import hola
import suma
import aleat

usuario = socket.gethostname()


if __name__ == "__main__":
    SumaApp = suma.App()
    AleatApp = aleat.App()
    HolaApp = hola.App()
    AdiosApp = hola.App()
    MiApp = webappmulti.webApp(usuario, 1234, {'/suma': SumaApp,
                                               '/aleat': AleatApp,
                                               '/hola': HolaApp,
                                               '/adios': HolaApp})
