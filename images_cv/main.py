
#Importamos el modulo cv2
import cv2
import numpy as np
import  matplotlib as plt

class Imagenes():
    "Constructor de la clase Imagenes"
    def __init__(self):

        pass
    def imagen(self):
        imagen = cv2.imread("./imagenes/lena.jpg", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("Lena", cv2.WINDOW_NORMAL)

        cv2.imshow("Lena", imagen)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass
    pass

# Instanciar la clase
App = Imagenes()
App.imagen()