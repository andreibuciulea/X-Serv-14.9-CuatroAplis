#!/usr/bin/python

import webappmulti
import socket

usuario = socket.gethostname()


class App(webappmulti.app):
    def parse(self, request, rest):
        paquete = request.split()[1][1:]
        (a) = paquete.split('/')[0]
        return a

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>" + parsedRequest +
                "</h1></body></html>")
if __name__ == "__main__":
    HolaApp = App()
    MiApp = webappmulti.webApp(usuario, 1234, {'/Hola': HolaApp,
                                               '/Adios': HolaApp})
