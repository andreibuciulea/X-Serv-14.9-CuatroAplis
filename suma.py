#!/usr/bin/python

import webappmulti
import socket
import random

usuario = socket.gethostname()


class App(webappmulti.app):

    def parse(self, request, rest):
        try:
            paquete = request.split()[1][1:]
            #(operacion, operando1, operando2) = paquete.split('/')
            lista = paquete.split('/')
        except ValueError:
            return None

        if len(lista) != 3:
            return None
        return lista

    def process(self, parsedRequest):
        #if self.guardado is None:
        #	self.guardado = 0
        if not parsedRequest:
            return ("400 Bad Request")
        (operacion, operando1, operando2) = parsedRequest
        if operacion == "suma":
            resultado = int(operando1) + int(operando2)
        elif operacion == "resta":
            resultado = int(operando1) - int(operando2)
        return ("200 OK", "<html><body><h1>" + str(resultado)
                + "</h1></body></html>")

if __name__ == "__main__":
    SumaApp = App()
    MiApp = webappmulti.webApp(usuario, 1234, {'/suma': SumaApp})
