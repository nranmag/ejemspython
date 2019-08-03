# contenido-juicio.py

import urllib2, obo

url = 'http://maunaloa.rchland.ibm.com/SIIDMQMF/970boxtstdet.htm'

respuesta = urllib2.urlopen(url)
HTML = respuesta.read()

print(obo.quitarEtiquetas(HTML))