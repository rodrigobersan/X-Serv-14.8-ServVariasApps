#!/usr/bin/python
import webappmulti
import random

class holaApp(webappmulti.app):
	def process(self,parsedRequest):
		return ("200 OK","<html><body>Hola Mundo!</html></body>")

class adiosApp(webappmulti.app):
	def process(self,parsedRequest):
		return ("200 OK","<html><body>Adios mundo cruel</body></html>")

class aleatApp(webappmulti.app):
	def process(self,parsedRequest):
		nextExt = str(random.randint(0,100000))
		nextURL = "localhost:1234/aleat/" + nextExt
		msg = "Hola. " + '<a href="' + NextURL + '">' + "Quieres mas?"

		return("200 OK","<html><body>" + msg + "</body></html>")

class sumaApp(webappmulti.app):
	status=0
	sum1=0
	sum2=0

	def parse (self, request, rest):
		print "\n\n" + rest[1:] + "\n\n"
		return rest[1:]

	def process(self, parsedRequest):
		try:
			if self.status==0:
				self.sum1 = int(parsedRequest)
				msg = "Recibido primer operando: " + str(self.sum1)
				self.status=1
			else:
				self.sum2 = int(parsedRequest)
				op = self.sum1 + self.sum2
				msg="Resultado de la suma: " + str(self.sum1) + ' + ' + str(self.sum2) + ' = ' + str(op)
				self.status = 0
		except ValueError:
			msg="La URL debe entregar un numero al final. Ejemplo: localhost:1234/suma/3"

		return ("200 OK", "<html><body><h1>" + msg + "</h1></body></html>")

if __name__ == "__main__":
	hola = holaApp()
	adios = adiosApp()
	suma = sumaApp()
	aleat = aleatApp()
	testWebApp = webappmulti.webApp ("localhost", 1234, {'/hola': hola,
														 '/adios': adios,
														 '/suma': suma,
														 '/aleat': aleat})
