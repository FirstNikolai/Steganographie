from tkinter import *
from tkinter import filedialog
from PIL import Image
import PIL
def cherche():
    windows.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return windows.filename;

#Fonction pour transformer un entier de base 10 en binaire
def binarisation(entier) :
    i = 0;
    result = str();
    while i < 8:
        result = result + str(int(entier % 2));
        entier = (entier - entier%2) /2 ;
        i= i+1;
    return result[::-1]; #Inversion de la chaine de caractère

#Fonction pour transformer un binaire en entier de base 10
def entierisation(binar) :
    i = 0
    result = 0;
    while i < 8:
        result = result + (int(binar[i]) * 2 **(7-i));
        i = i+1;
    return result;
imageDecode = Image.open("stegano.png");
L, H = imageDecode.size;
imageOrigin = Image.new("RGB", (L,H))
imageHide = Image.new("RGB", (L,H))
for y in range(H):
    for x in range(L):
        #enregistrement de la couleur des pixels sous forme d'octet de l'image à décoder
        pixelDecode =  imageDecode.getpixel((x,y));
        rougeBin1 = binarisation(pixelDecode[0]);
        vertBin1 = binarisation(pixelDecode[1]);
        bleuBin1 = binarisation(pixelDecode[2]);
        #Reconstitution des pixels de l'image d'origine avec les bits fort
        rougeOrigin = entierisation(str(rougeBin1[:4] + "0000"));
        vertOrigin = entierisation(str(vertBin1[:4] + "0000"));
        bleuOrigin = entierisation(str(bleuBin1[:4] + "0000"));
        #Reconstitution des pixels de l'image caché avec les bits faibles
        rougeHide = entierisation(str(rougeBin1[4:] + "0000"));
        vertHide = entierisation(str(vertBin1[4:] + "0000"));
        bleuHide = entierisation(str(bleuBin1[4:] + "0000"));
        #Inscription des pixels reconstitué pour la reconstituion des images
        imageOrigin.putpixel((x,y),(rougeOrigin,vertOrigin,bleuOrigin));
        imageHide.putpixel((x,y),(rougeHide,vertHide,bleuHide));
#Sauvegarde et écriture de l'image d'origine
imageOrigin.save("imageOrigin.jpg");
imageOrigin.show()
#Sauvegarde et écriture de l'image caché
imageHide.save("ImageHide.jpg");
imageHide.show()   
