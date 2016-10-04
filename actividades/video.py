
import  numpy as np
import  cv2

''' La clase Video sera la encargada de obtener el flujo de datos de la camara web o fuente de video
'''

class Video():

    def __init__(self):
        pass

    # Esta funcion cargara el dispositivo
    def getVideo(self):

        print("Cargando dispositivos.\nespere...")



        pass

    def getImage(self):
        img = cv2.imread("./imagenes/Kharl.jpg", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        pass
    pass


