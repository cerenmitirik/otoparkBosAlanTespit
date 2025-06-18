import cv2
import pickle #verileri dosyaya yazma ve geri alma icin kullanilir 
#mousla dikdötgen çizebilen sağ tıkla silen ve konumları dosyaya kaydeden uygulama

try: 
    with open("noktalar","rb") as f:
        liste=pickle.load(f)
        #kullanıcının girdiği noktaları saklar 
        #rb: pickle verisi binary oldugu icin kullanılır
except:
    liste=[]

def mouse(events,x,y,flags,params):#mouseu islemek icin kullan. setmousecallack ile çalısır 
    #event sağ tık mı sol tık mı
    #x,y mouseun koordinatları 
    
    if events==cv2.EVENT_LBUTTONDOWN:
        liste.append((x,y))#sol tıkla listeye ekle 
    #

    if events==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(liste):
            x1,y1=pos
            if x1<x<x1+26 and y1<y<y1+15:
                liste.pop(i)
    #sağ tık yaparsan tıklanan konum daha önce listeye eklenenlerden biri mi ? kontrol et
    #tıklanan nokta 26x15 boyutlarındaki dikdörtgenin içinde mi?
    #eger tıklanan yer dikdörtgenin icindeyse o dikdotgeni listeden pop ile sil

    with open("noktalar","wb") as f:
            pickle.dump(liste,f)
    #tık yapıldıgında liste icerigi noktlar dosyasına binary olarak yaz
    #wb : dosyaya ikili formatta yazmak icin kullanılır 
    #pickle.dump():python listesini dosyaya yazar

while True:
    img=cv2.imread("img1.png")
    #print(liste)
    for l in liste:
        cv2.rectangle(img,l,(l[0]+26,l[1]+15),(255,0,0),2)
# l : sol üst diğerleri sağ alt
    cv2.imshow("oto",img)
    cv2.setMouseCallback("oto",mouse)
    #acılan resimdeki tıklamalar mouse fonksiyonuna yonlendirilir

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()