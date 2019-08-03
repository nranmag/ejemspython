# abre-paginaweb.py

import urllib2

url = 'http://maunaloa.rchland.ibm.com/SIIDMQMF/970boxtstdet.htm'

respuesta = urllib2.urlopen(url)
contenidoWeb = respuesta.read()

print(contenidoWeb[0:300])