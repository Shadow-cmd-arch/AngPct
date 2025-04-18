# # # # # # # # # # # # # # # # # # # #
#                                     #
#          AngPct vers 1.2            #
#                                     #
# # # # # # # # # # # # # # # # # # # #


# Importation de 'Tkinter'.
from tkinter import*
from math import*
from PIL import ImageTk,Image
#import os
import base64
from io import BytesIO

# Variables globales
float_value_p = 0.0
float_value_d = 0.0
nmb_car_1 = 0
nmb_car_2 = 0
result_d = 0.0
result_p = 0.0

translations = {
    "fr": {
        "welcome": "Bienvenue sur le convertisseur de pourcentages en degrés!",
        "percentages": "Pourcentages:",
        "degrees": "Degrés:",
        "convert": "Convertir",
        "reset": "Réinitialiser",
        "quit": "Quitter",
        "language": "Langue",
        "tools": "Outils",
        "confirm_quit": "Voulez-vous vraiment quitter?",
        "yes": "Oui",
        "no": "Non",
        "quit_menu": "Quitter",
        "version": "Version : 1.2",
    },
    "en": {
        "welcome": "Welcome to the percentage-to-degree converter!",
        "percentages": "Percentages:",
        "degrees": "Degrees:",
        "convert": "Convert",
        "reset": "Reset",
        "quit": "Quit",
        "language": "Language",
        "tools": "Tools",
        "confirm_quit": "Do you really want to quit?",
        "yes": "Yes",
        "no": "No",
        "quit_menu": "Quit",
        "version": "Version: 1.2",
    },
    "de": {
        "welcome": "Willkommen beim Prozent-zu-Grad-Umrechner!",
        "percentages": "Prozentsätze:",
        "degrees": "Grad:",
        "convert": "Umrechnen",
        "reset": "Zurücksetzen",
        "quit": "Beenden",
        "language": "Sprache",
        "tools": "Werkzeuge",
        "confirm_quit": "Möchten Sie wirklich beenden?",
        "yes": "Ja",
        "no": "Nein",
        "quit_menu": "Beenden",
        "version": "Version: 1.2",
    },
    "ar": {
        "welcome": "مرحبًا بك في محول النسب المئوية إلى درجات!",
        "percentages": "النسبة المئوية:",
        "degrees": "الدرجات:",
        "convert": "تحويل",
        "reset": "إعادة تعيين",
        "quit": "إنهاء",
        "language": "اللغة",
        "tools": "أدوات",
        "confirm_quit": "هل تريد حقًا إنهاء البرنامج؟",
        "yes": "نعم",
        "no": "لا",
        "quit_menu": "إنهاء",
        "version": "الإصدار: 1.2",
    },
    "zh": {
        "welcome": "欢迎使用百分比到角度转换器！",
        "percentages": "百分比:",
        "degrees": "度数:",
        "convert": "转换",
        "reset": "重置",
        "quit": "退出",
        "language": "语言",
        "tools": "工具",
        "confirm_quit": "您确定要退出吗？",
        "yes": "是",
        "no": "否",
        "quit_menu": "退出",
        "version": "版本: 1.2",
    },
    "it": {
        "welcome": "Benvenuto nel convertitore di percentuali in gradi!",
        "percentages": "Percentuali:",
        "degrees": "Gradi:",
        "convert": "Convertire",
        "reset": "Reset",
        "quit": "Esci",
        "language": "Lingua",
        "tools": "Strumenti",
        "confirm_quit": "Vuoi davvero uscire?",
        "yes": "Sì",
        "no": "No",
        "quit_menu": "Esci",
        "version": "Versione: 1.2",
    },
    "pt": {
        "welcome": "Bem-vindo ao conversor de porcentagem para graus!",
        "percentages": "Porcentagens:",
        "degrees": "Graus:",
        "convert": "Converter",
        "reset": "Redefinir",
        "quit": "Sair",
        "language": "Idioma",
        "tools": "Ferramentas",
        "confirm_quit": "Deseja realmente sair?",
        "yes": "Sim",
        "no": "Não",
        "quit_menu": "Sair",
        "version": "Versão: 1.2",
    },
    "es": {
        "welcome": "¡Bienvenido al convertidor de porcentajes a grados!",
        "percentages": "Porcentajes:",
        "degrees": "Grados:",
        "convert": "Convertir",
        "reset": "Reiniciar",
        "quit": "Salir",
        "language": "Idioma",
        "tools": "Herramientas",
        "confirm_quit": "¿Realmente quieres salir?",
        "yes": "Sí",
        "no": "No",
        "quit_menu": "Salir",
        "version": "Versión: 1.2",
    },
}


# couleur:
#1=("#ffffff")
#2=("#65796e")
#3=("#010101")
#4=("#c67242")
#5=("#a8b2a9")
#6=("#1c4750")

#couleur 2:
##A82F31
##168F8E
##F4973A
##F8FAF9
##E66430
##9F2C35

encoded_icon = ("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")

def decode_and_save_icon(encoded_str, file_name):
    decoded_image = base64.b64decode(encoded_str)
    with open(file_name, "wb") as icon_file:
        icon_file.write(decoded_image)



def chance2():
    quitter=Tk()
    quitter.iconbitmap(temp_icon_path)

    def oui():
        quitter.destroy()
        fenetre.destroy()

    def non():
        quitter.destroy()
    
    current_translations = translations[selected_language]

    quitter.title(" ")
    quitter.config(bg="#ffffff")
    quitter.geometry("430x150")
    titre=Label(quitter,text="Voulez-vous vraiment quitter ?",font=("Arial",20,"bold"),bg="#ffffff",fg="#1c4750")
    B1=Button(quitter,text="OUI",font=("Arial",15),bg="#c67242",fg="black",command=oui)
    B2=Button(quitter,text="NON",font=("Arial",15),bg="#c67242",fg="black",command=non)

    titre.grid(row=0,column=0,columnspan=2)
    B1.grid(row=1,column=0)
    B2.grid(row=1,column=1)
    B1.config(text=current_translations["yes"])
    B2.config(text=current_translations["no"])
    titre.config(text=current_translations["confirm_quit"])

    quitter.mainloop()

temp_icon_path = "temp_icon.ico"
decode_and_save_icon(encoded_icon, temp_icon_path)



# Parametres de la fenêtre.
#icon_path = os.path.join(os.path.dirname(__file__), "logo\AngPtc_3.ico")
fenetre=Tk()#_____________________________________________________________________________________________________________Création de la fenêtre
fenetre.title("AngPct   vers: 1.2")#________________________________________________________________________________________Titre de la fenêtre
fenetre.config(background="#F8FAF9")#_____________________________________________________________________________________Couleur BG
fenetre.minsize(1100,400)#________________________________________________________________________________________________Dimention fenêtre
titre=Label(text="Bienvenue sur le convertisseur de pourcentages en degrés!",font=("Arial",25,"bold","underline"),fg="#1c4750",bg="#F8FAF9")#Titre du logitiel
fenetre.iconbitmap(temp_icon_path)

def set_language(langue):
    global selected_language
    selected_language = langue
    current_translations = translations[langue]

    titre.config(text=current_translations["welcome"])
    pourcentages.config(text=current_translations["percentages"])
    Degré.config(text=current_translations["degrees"])
    convertir_bouton.config(text=current_translations["convert"])
    convertir_bouton_2.config(text=current_translations["convert"])
    bouton_effacer.config(text=current_translations["reset"])
    Bouton_quitter.config(text=current_translations["quit"])
    vers.config(text=current_translations["version"])

    menu_bar.entryconfig(menu_language_index, label=current_translations["language"])
    menu_bar.entryconfig(menu_Quitter_index, label=current_translations["quit_menu"])    

menu_bar=Menu(fenetre,background="#F8FAF9")

menu_quitter=Menu(menu_bar, tearoff=0)
menu_bar.add_command(label="Quitter",command=chance2)
menu_Quitter_index = menu_bar.index("Quitter")

menu_language=Menu(menu_bar, tearoff=0)
menu_language.add_command(label="English", command=lambda: set_language("en"))
menu_language.add_command(label="Français", command=lambda: set_language("fr"))
menu_language.add_command(label="Deutsch", command=lambda: set_language("de"))
menu_language.add_command(label="Español", command=lambda: set_language("es"))
menu_language.add_command(label="Arabe", command=lambda: set_language("ar"))
menu_language.add_command(label="Italien", command=lambda: set_language("it"))
menu_language.add_command(label="Chinois", command=lambda: set_language("zh"))
menu_language.add_command(label="Portugais", command=lambda: set_language("pt"))
#menu_language.add_separator()
#menu_language.add_command(label="Quitter", command=fenetre.destroy)
menu_bar.add_cascade(label="Language",background="#F8FAF9",menu=menu_language)
menu_language_index = menu_bar.index("Language")

fenetre.config(menu=menu_bar,background="#F8FAF9")


entry_var_d=DoubleVar()
entry_var_p=DoubleVar()

#création des widgets.
pourcentages=Label(text="Pourcentages:",font=("Arial",23),bg="#F8FAF9",fg="#1c4750")#________________________ Text 'Pourcentages'.
pourcent=Entry(fenetre,textvariable=entry_var_p,font=("Arial",15),bg="#65796e",fg="black",width=7)#________ Champ d'entré des pourcentages.
degré=Entry(fenetre,textvariable=entry_var_d,font=("Arial",15),bg="#65796e",fg="black",width=7)#___________ Champ d'entré des degrés.
Degré=Label(text="Degrés:",font=("Arial",23),bg="#F8FAF9",fg="#1c4750")#_____________________________________ Text 'Degrés'.
#.config(text=100*tan(pourcent.get()),bg="#000216",fg="green")
#.config(text=100*tan(degré.get()),bg="#000216",fg="green")



#def convertir():
#    entry_value = degré.get().strip() # Récupère et nettoie la valeur de l'Entry
#    entry_value_2 = pourcent.get().strip() # Récupère et nettoie la valeur de l'Entry
#    print(f"Valeur récupérée de l'Entry : '{entry_value}'")
#    print(f"Valeur récupérée de l'Entry : '{entry_value_2}'")
#    if entry_value and entry_value_2:
#        try:
#            value = float(entry_value)
#            value_2 = float(entry_value_2)
#            print(f"Valeur convertie : {value}")
#            print(f"Valeur convertie : {value_2}")
#        except ValueError as e:
#            print(f"Erreur de conversion : {e}")
#
#    else:
#        print("Erreur : L'entrée est vide.")

def pourcentage_en_degre(pourcentage):
    angle_radians = atan(pourcentage / 100)
    angle_degré = degrees(angle_radians)
    return angle_degré

def degre_en_pourcentage(degre):
    pente_radians = tan(radians(degre))
    pente_pourcentage = pente_radians * 100
    return pente_pourcentage

def convertir():
    global float_value_p, nmb_car_2, result_p
    float_value_p = entry_var_p.get()
    result_p  = round(pourcentage_en_degre(float_value_p),3)
    degré.delete(0,END)
    degré.insert(0,result_p)
    nmb_car_2 = len(str(float_value_p))
    bouton_effacer.config(state="normal")
        
def convertir_2():
    global float_value_d, nmb_car_1, result_d
    float_value_d = entry_var_d.get()
    result_d = round(degre_en_pourcentage(float_value_d),3)
    pourcent.delete(0,END)
    pourcent.insert(0,result_d)
    nmb_car_1 = len(str(float_value_d))
    bouton_effacer.config(state="normal")

#def arrondir():
#    global result_d, result_p
#    if result_p is not None:
#        arrondi_p = round(result_p)
#        pourcent.insert(0, arrondi_p)
#    if result_d is not None:
#         arrondi_d = round(result_d)
#         degré.insert(0, arrondi_d)
    
def supr():
    global nmb_car_1, nmb_car_2
    
    degré.delete(0,END)
    pourcent.delete(0,END)

    nmb_car_1 = 0
    nmb_car_2 = 0
    result_d = 0
    result_p = 0
    print(result_p)
    print(result_d)

    bouton_effacer.config(state="disabled")


convertir_bouton=Button(text="Convertir",font=("Cylburn",15),bg="#c67242",fg="#000000",command=convertir)#_____ Bouton 'Convertir'.
convertir_bouton_2=Button(text="Convertir",font=("Cylburn",15),bg="#c67242",fg="#000000",command=convertir_2)#_ Bouton 'Convertir' n°2.
Bouton_quitter=Button(text="Quitter",font=("Arial",15),bg="#c67242",fg="black",command=chance2)#_______________ Bouton Quitter.
#img=ImageTk.PhotoImage(Image.open("C:/Users/chouk/Downloads/Python/Acomas strucure logo.jpg"))#_______________ Importation de l'image.
#IMAGE=Label(fenetre,image=img)#_______________________________________________________________________________ Création de la variable"IMAGE".
bouton_effacer=Button(fenetre,text="Réinitialiser",font=("Cylburn",15),bg="#c67242",fg="#000000",command=supr)
#bouton_arrondir=Button(fenetre,text="Arrondir",font=("Cylburn",15),bg="#c67242",fg="#000000",command=arrondir,state="disabled")
#cadre = LabelFrame(fenetre,text="Vers: 1.0",font=("Arial",15),fg="black",bg="blue")
vers = Label(fenetre,text="Vers: 1.2",font=("Arial",15),fg="black",bg="#ffffff")





# Parametres du placement de la fenêtre.
titre.place(relx=0.1,y=5)#___________________Titre du logitiel.
pourcentages.place(x=40,y=80)#_______________Texte "Pourcentages".
convertir_bouton.place(x=360,y=85)#__________Bouton "Convertir".
pourcent.place(x=240,y=90)#__________________Champ d'entré des pourcentages.
degré.place(x=160,y=230)#____________________Champ d'entré des degrés.
Degré.place(x=40,y=220)#_____________________Texte "Degrés".
convertir_bouton_2.place(x=300,y=220)#_______Bouton "Convertir" n°2.
#z.place(x=480,y=95)#________________________Resultat pourcentage.
#n.place(x=420,y=230)#_______________________Resultat degrés.
Bouton_quitter.place(x=40,y=300)#____________Bouton Quitter.
#IMAGE.place(x=10,y=5)
bouton_effacer.place(x=140,y=300)
#bouton_arrondir.place(x=340,y=300)
vers.place(relx=0.9,rely=0.9)
#cadre.place(relx=0.9,rely=0.9)


fenetre.mainloop()