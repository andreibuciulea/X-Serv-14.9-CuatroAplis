#!/usr/bin/python

import webappmulti
import socket
import random

usuario = socket.gethostname()


class App(webappmulti.app):
    def process(self, parsedRequest):
        aleatorio = str(int(random.random()*1000000))
        return ("200 OK", "<html><body><h1>" + aleatorio +
                "</h1></body></html>")
if __name__ == "__main__":
    AleatApp = App()
    MiApp = webappmulti.webApp(usuario, 1234, {'/aleat': AleatApp})
