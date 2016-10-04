#!/usr/bin/python

import cv2

''' Todo el desarrollo lo haremos con un enfoque Orientado a Objetos
    así que, en adelante todo el codigo sera separado en archivos deiferentes
    esto con la finalidad de facilitar la lectura y comprension de los conceptos
    y métodos que trataremos :)

    Si nunca han programado con este paradigma usando Python, este sera un buen momento
    para que lo vean en funcionamiento.
'''


# Primero importamos del modulo video.py, la clase Video, de esa forma podremos acceder
# a todas sus definiciones o métodos.
from video import Video

# Creamos un "objeto" o "instancia" de la clase Video en app.
app = Video()
# con el objeto "app" usamos la notación punto '.' para llamar a uno de los metodos de
#la clase Video.
app.getVideo()
app.getImage()