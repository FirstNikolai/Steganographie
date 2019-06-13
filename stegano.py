from tkinter import *
from tkinter import filedialog
from PIL import Image
import PIL

#Création de variable global pour communiquer entre les fonctions
imageVrai = str();
imageHide = str();
im1 = str();
im2 = str();

#Fonction pour transformer un entier de base 10 en binaire
def binarisation(entier) :
    i = 0;
    result = str();
    while i < 8:
        result = result + str(int(entier % 2));
        entier = int(entier/2) ;
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

#Fonction pour renseigner le chemin d'accès de la photo à afficher à traver un explorateur de fichier
def cherche1():
    windows.filename =  filedialog.askopenfilename(initialdir = "/",title = "Selectionne tes photos",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")));
    global im1
    im1 = windows.filename
    print(im1);

#Fonction pour renseigner le chemin d'accès de la photo à cacher à traver un explorateur de fichier
def cherche2():
    windows.filename =  filedialog.askopenfilename(title = "Selectionne tes photos",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")));
    global im2
    im2 = windows.filename
    print(im2);

#Fonction qui s'occupe de la partie stegano du programme 
def stegano():
    global imageVrai;
    global imageHide;
    imageVrai = Image.open(im1);
    imageHide = Image.open(im2);
    L, H = imageVrai.size;
    imageNew = Image.new("RGB", (L,H))
    for y in range(H):
        for x in range(L):
            #enregistrement de la couleur des pixels sous forme d'octet de l'image d'origine
            pixelVrai = imageVrai.getpixel((x,y));
            rougeBin1 = binarisation(pixelVrai[0]);
            vertBin1 = binarisation(pixelVrai[1]);
            bleuBin1 = binarisation(pixelVrai[2]);
            #enregistrement de la couleur des pixels sous forme d'octet de l'image à cacher
            pixelHide = imageHide.getpixel((x,y));
            rougeBin2 = binarisation(pixelHide[0]);
            vertBin2 = binarisation(pixelHide[1]);
            bleuBin2 = binarisation(pixelHide[2]);
            #création des nouveau octets des couleurs des pixels de la nouvelle image
            rougeNew = entierisation(str(rougeBin1[:4] + rougeBin2[:4]));
            vertNew = entierisation(str(vertBin1[:4] + vertBin2[:4]));
            bleuNew = entierisation(str(bleuBin1[:4] + bleuBin2[:4]));
            #création des pixels de la nouvelle image
            imageNew.putpixel((x,y),(rougeNew,vertNew,bleuNew));
    #Sauvegarde et écriture de la nouvelle image
    imageNew.save("stegano.png");
    imageNew.show()              

#Ouverture d'une fenêtre tkinter
windows = Tk();

#Création des labels et bouton référant aux fonctions définis precedement
label_description = Label(windows,text="Choisis tes photos !");
button_add_img_1 = Button(windows, text="Photo à afficher", command = cherche1);
button_add_img_2 = Button(windows, text="Photo à cacher", command = cherche2);
button_start = Button(windows, text="C'est partit", command = stegano);

#Affichage des labels et bouton
label_description.pack();
button_add_img_1.pack();
button_add_img_2.pack();
button_start.pack();

#La boucle pour permettre aux boutons de fonctionner
windows.mainloop();


