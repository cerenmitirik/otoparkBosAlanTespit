import cv2
import pickle #daha once secilen dikdörtgen bolgeleri noktalar dosyasından okumak icin
import numpy as np 

cap=cv2.VideoCapture("video.mp4")

def check(frame1): #binary hale getirilmis işlenmis threshold goruntusu üzerinden alanların dolu bos kontrolu icin tanımladık
    #frame1 dilate edilmis siyah beyaz bir görüntüdür
    spacecounter=0 #bos alan sayaci
    for pos in liste: #pickle ile kayıtlı olan liste icerisindeki koordinatlara gider ve her dikdörtgeni dolasir
        x,y=pos

        crop=frame1[y:y+15,x:x+26]
        #frame1 islenis threshold.
        #crop y yuksekliginde 15 px x genisliginde 26 px yani bo bölgedeki dikdörtgeni keser
        count=cv2.countNonZero(crop)#beyaz piksel sayisi verir 
    
        #print("count",count)

        if count<150: #EGER pikseller azsa ALAN BOSTUR coksa ALAN DOLUDUR 
       
            color=(0,255,0)
            spacecounter+=1
        else:
            color=[0,0,255]
        cv2.rectangle(frame,pos,(pos[0]+26,pos[1]+15),color,2)
    cv2.putText(frame,f"bos: {spacecounter}/{len(liste)}",(15,24),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),4)
with open("noktalar","rb") as f:
    liste=pickle.load(f)
while True:
    _,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gri,(3,3),1)
    thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    median=cv2.medianBlur(thresh,5)
    dilates=cv2.dilate(median,np.ones((3,3)),iterations=1)

    check(dilates)

    cv2.imshow("video",frame)
    #cv2.imshow("gri",gri)
    #cv2.imshow("blur ",blur)
    #cv2.imshow("thresh",thresh)
    #cv2.imshow("median ", median)
    #cv2.imshow("dilate ",dilates)

    if cv2.waitKey(200) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()