from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression
watch_cascade=cv2.CascadeClassifier('cascade.xml')

cap=cv2.VideoCapture('automaticas3.mp4')
def visualize():
    global cap
    if cap is not None:
        ret,img=cap.read()
        if ret == True:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            watch = watch_cascade.detectMultiScale(gray, scaleFactor=1.05,minNeighbors=20, minSize=(550, 550),flags=cv2.CASCADE_SCALE_IMAGE)
     
            ancho_min=600
            alto_min=600
            for(x,y,w,h) in watch:
                
                cv2.rectangle(img,(x,y),(x+w-300,y+h-300),(255,0,0),2)
                cv2.putText(img, 'weapon', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

                validar_contorno = (w >= ancho_min) and (h >= alto_min)
                if not validar_contorno:
                  continue
           

            img=imutils.resize(img,width=980)
            im = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualize)


             #    continue
    
        else:
            lblVideo.image = ""
            cap.release()


         

def start():
    global cap
    visualize()


root = Tk()

root.title("DETECCION DE ARMAS")
root.geometry("1500x720")

root.resizable(width=False, height=False)
imagenF = PhotoImage(file="TABLA_ARMAS.png")
background = Label(image = imagenF, text = "Fondo")
background.place(x =0, y = -10, relwidth = 1, relheight = 1)  

imagenBI = PhotoImage(file="ARMAS_BOTON.png")
Start= Button(root,  image=imagenBI, height="80", width="100", command=start)
Start.place(x = 200, y = 350)

imagenBF = PhotoImage(file="STOP_BOTON.png")
end = Button(root, text="Finalizar", image= imagenBF, height="40", width="70", command=root.destroy)
end.place(x = 220, y = 500)
lblVideo = Label(root)
lblVideo.place(x = 314, y = 90)
root.mainloop()            