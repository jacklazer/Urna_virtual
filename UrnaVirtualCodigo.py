# Proyecto Votaciones
# Juan Sebastian Cifuentes Vallejo - 202179800 - 3743 - Grupo 01
# Wilson Andrés Mosquera Zapata - 202182116 - 3743 - Grupo 02
# Profesora: Diana patricia Lozano



#Librerías
import tkinter
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk


# Lista cedulas
LiC = [] 
# Lista sexos
LiS = []
# Lista votos alcaldia
LiVA = []
# Lista votos gobernacion
LiVG = []


# FRE = Funcion que entrega los resultados finales y algunas estadisticas
def FRE(): #FVCA

    global VREV
    global VA

    # Número de Cédulas inscritas
    NCI = len(LiC)
    NHI = 0
    NMI = 0

    for i in range(0,NCI):
        if LiS[i] == '1':
            # Número de Hombres inscritos
            NHI = NHI+1
        elif LiS[i] == '0':
            # Número de Mujeres inscritas
            NMI = NMI+1
    j=0
    NVCA1 = 0
    NVCA2 = 0
    NVCA3 = 0
    NVBA = 0
    NVNA = 0

    while j<NCI:
        if LiVA[j] == '1':
            # Numero de votos candidato A1
            NVCA1 = NVCA1+1
        if LiVA[j] == '2':
            # Numero de votos candidato A2
            NVCA2 = NVCA2+1
        if LiVA[j] == '3':
            # Numero de votos candidato A3
            NVCA3 = NVCA3+1
        if LiVA[j] == 'B':
            # Numero de votos en blanco alcaldia
            NVBA = NVBA+1
        if LiVA[j] == 'VN':
            # Numero de votos nulos alcaldia
            NVNA = NVNA+1
        j = j+1
    h = 0
    NVCG1 = 0
    NVCG2 = 0
    NVCG3 = 0
    NVBG = 0
    NVNG = 0

    while h<NCI:
        if LiVG[h] == '1':
            # Numero de votos candidato G1
            NVCG1 = NVCG1+1
        if LiVG[h] == '2':
            # Numero de votos candidato G1
            NVCG2 = NVCG2+1
        if LiVG[h] == '3':
            # Numero de votos candidato G1
            NVCG3 = NVCG3+1
        if LiVG[h] == 'B':
            # Numero de votos en blanco gobernacion
            NVBG = NVBG+1
        if LiVG[h] == 'VN':
            # Numero de votos nulos gobernacion
            NVNG = NVNG+1
        h = h+1

    # Numero votantes alcaldía
    NVA = NVCA1+NVCA2+NVCA3+NVBA

    # Número votantes Gobernación
    NVG = NVCG1+NVCG2+NVCG3+NVBG

    # Ganador Alcaldía
    global GA
    if NVCA1>NVCA2 and NVCA1>NVCA3 and NVCA1>NVBA:
        GA = 'Candidato A1'
    elif NVCA2>NVCA1 and NVCA2>NVCA3 and NVCA2>NVBA:
        GA = 'Candidato A2'
    elif NVCA3>NVCA1 and NVCA3>NVCA2 and NVCA3>NVBA:
        GA = 'Candidato A3'
    elif NVBA>NVCA1 and NVBA>NVCA2 and NVBA>NVCA3:
        GA = 'Voto en blanco'
    elif NVA==0:
        GA = 'No se registraron votos'
    else:
        GA = 'Empate en votos'

    # Ganador Gobernación
    global GG
    if NVCG1>NVCG2 and NVCG1>NVCG3 and NVCG1>NVBG:
        GG = 'Candidato G1'
    elif NVCG2>NVCG1 and NVCG2>NVCG3 and NVCG2>NVBG:
        GG = 'Candidato G2'
    elif NVCG3>NVCG1 and NVCG3>NVCG2 and NVCG3>NVBG:
        GG = 'Candidato G3'
    elif NVBG>NVCG1 and NVBG>NVCG2 and NVBG>NVCG3:
        GG = 'Voto en blanco'
    elif NVG==0:
        GG = 'No se registraron votos'
    else:
        GG = 'Empate en votos'

    # Porcentaje Hombres
    PHI = str(round((NHI/NCI)*100))
    
    # Porcentaje Mujeres
    PMI = str(round((NMI/NCI)*100))

    # Ventana
    VA = '10'
    VOV.destroy()
    VREV = Tk()
    VREV.geometry('500x500')
    VREV.resizable(False, False)

    # Encabezado
    ICo = Image.open('Colombia.jpg').resize((100, 100))
    ICo2 = ImageTk.PhotoImage(ICo)
    ICo3 = tk.Label(VREV, image=ICo2)
    ICo3.place(x=0, y=0)

    IRe = Image.open('Registraduria.jpg').resize((100, 100))
    IRe2 = ImageTk.PhotoImage(IRe)
    IRe3 = tk.Label(VREV, image=IRe2)
    IRe3.place(relx = 1.0,
                rely = 0.0,
                anchor ='ne')

    LER = Label(VREV, text='ELECCIONES REGIONALES')
    LER.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold"))
    LER.place(x=100, y=0, width=298, height=100)

    FrST = Frame(VREV)
    FrST.config(bg='black', width=500, height=1)
    FrST.place(x=0, y=101)

    # Título
    LCA = Label(VREV, text='Resultado Elecciones Regionales 2022', justify="center")
    LCA.config(font=('Verdana', 15, "bold"))
    LCA.place(x=0, y=115, width= 500)

    # Ganador Alcaldía
    LAE = Label(VREV, text='Ganador para Alcaldía: ')
    LAE.config(font=('Verdana', 10))
    LAE.place(x=30, y=170)

    EAE = Entry(VREV)
    EAE.config(font=('Verdana', 10))
    EAE.place(x=270, y=170)
    EAE.delete(0, END)
    EAE.insert(0, GA)
    EAE.config(state="readonly")

    # Ganador Gobernación
    LGE = Label(VREV, text='Ganador para Gobernación: ')
    LGE.config(font=('Verdana', 10))
    LGE.place(x=30, y=200)

    EGE = Entry(VREV)
    EGE.config(font=('Verdana', 10))
    EGE.place(x=270, y=200)
    EGE.delete(0, END)
    EGE.insert(0, GG)
    EGE.config(state="readonly")

    # Número Votantes Alcaldía
    LCVA = Label(VREV, text='Cantidad de votantes Alcaldía: ')
    LCVA.config(font=('Verdana', 10))
    LCVA.place(x=30, y=230)

    ECVA = Entry(VREV)
    ECVA.config(font=('Verdana', 10), state=tkinter.DISABLED)
    ECVA.place(x=270, y=230)

    if NVA != 0:
        ECVA.config(state=tkinter.NORMAL)
        ECVA.delete(0, END)
        ECVA.insert(0, NVA)
        ECVA.config(state="readonly")
    else :
        ECVA.config(state=tkinter.NORMAL)
        ECVA.delete(0, END)
        ECVA.insert(0, '0')
        ECVA.config(state="readonly")

    # Número Votantes Gobernación
    LCVG = Label(VREV, text='Cantidad de votantes Gobernación: ')
    LCVG.config(font=('Verdana', 10))
    LCVG.place(x=30, y=260)

    ECVG = Entry(VREV)
    ECVG.config(font=('Verdana', 10), state=tkinter.DISABLED)
    ECVG.place(x=270, y=260)

    if NVG  != 0:
        ECVG.config(state=tkinter.NORMAL)
        ECVG.delete(0, END)
        ECVG.insert(0, NVG)
        ECVG.config(state="readonly")
    else :
        ECVG.config(state=tkinter.NORMAL)
        ECVG.delete(0, END)
        ECVG.insert(0, '0')
        ECVG.config(state="readonly")

    # Total Votantes
    LCTV = Label(VREV, text='Cantidad total de votantes: ')
    LCTV.config(font=('Verdana', 10))
    LCTV.place(x=30, y=290)

    ECTV = Entry(VREV)
    ECTV.config(font=('Verdana', 10), state=tkinter.DISABLED)
    ECTV.place(x=270, y=290)

    if NCI != 0 or NCI != 0:
        ECTV.config(state=tkinter.NORMAL)
        ECTV.delete(0, END)
        ECTV.insert(0, NCI)
        ECTV.config(state="readonly")
    else :
        ECTV.config(state=tkinter.NORMAL)
        ECTV.delete(0, END)
        ECTV.insert(0, '0')
        ECTV.config(state="readonly")

    # Votos Blanco Alcaldía
    LCBA = Label(VREV, text='Votos en Blanco Alcaldía: ')
    LCBA.config(font=('Verdana', 10))
    LCBA.place(x=30, y=320)

    ECBA = Entry(VREV)
    ECBA.config(font=('Verdana', 10), state=tkinter.DISABLED)
    ECBA.place(x=270, y=320)

    if NVBA != 0:
        ECBA.config(state=tkinter.NORMAL)
        ECBA.delete(0, END)
        ECBA.insert(0, NVBA)
        ECBA.config(state="readonly")
    else :
        ECBA.config(state=tkinter.NORMAL)
        ECBA.delete(0, END)
        ECBA.insert(0, '0')
        ECBA.config(state="readonly")

    # Votos Blanco Gobernación
    LCBG = Label(VREV, text='Votos en Blanco Gobernación: ')
    LCBG.config(font=('Verdana', 10))
    LCBG.place(x=30, y=350)

    ECBG = Entry(VREV)
    ECBG.config(font=('Verdana', 10), state=tkinter.DISABLED)
    ECBG.place(x=270, y=350)

    if NVBG != 0:
        ECBG.config(state=tkinter.NORMAL)
        ECBG.delete(0, END)
        ECBG.insert(0, NVBG)
        ECBG.config(state="readonly")
    else :
        ECBG.config(state=tkinter.NORMAL)
        ECBG.delete(0, END)
        ECBG.insert(0, '0')
        ECBG.config(state="readonly")

    # Porcentaje Hombres
    LPH = Label(VREV, text='Porcentaje de Hombres: ')
    LPH.config(font=('Verdana', 10))
    LPH.place(x=30, y=380)

    EPH = Entry(VREV)
    EPH.config(font=('Verdana', 10), state=tkinter.DISABLED)
    EPH.place(x=270, y=380)

    if NHI != 0:
        EPH.config(state=tkinter.NORMAL)
        EPH.delete(0, END)
        EPH.insert(0, PHI+"%")
        EPH.config(state="readonly")
    else :
        EPH.config(state=tkinter.NORMAL)
        EPH.delete(0, END)
        EPH.insert(0, '0%')
        EPH.config(state="readonly")

    # Porcentaje Mujeres
    LPM = Label(VREV, text='Porcentaje de Mujeres: ')
    LPM.config(font=('Verdana', 10))
    LPM.place(x=30, y=410)

    EPM = Entry(VREV)
    EPM.config(font=('Verdana', 10), state=tkinter.DISABLED)
    EPM.place(x=270, y=410)

    if NMI != 0:
        EPM.config(state=tkinter.NORMAL)
        EPM.delete(0, END)
        EPM.insert(0, PMI+"%")
        EPM.config(state="readonly")
    else :
        EPM.config(state=tkinter.NORMAL)
        EPM.delete(0, END)
        EPM.insert(0, '0%')
        EPM.config(state="readonly")

    # Botón Finalizar Proceso
    BRVEC = Button(VREV, text='Finalizar proceso',command=FDR, bg="#FFFFE0")
    BRVEC.place(x=180, y=450)
    BRVEC.config(width=20, height=2, font=('Verdana', 9))

    VREV.mainloop()


# FDR = Funcion destruir ventana final
def FDR():
    VREV.destroy()


# FOVEC = Funcion registrar otro voto ó obtener resultados de votación.
def FOVR():
    if VAE == False:
        LiVA.append('VN')

    elif VGE == False:
        LiVG.append('VN')

    if VAE == True or VGE == True:

        # Ventana
        global VOV
        global VA
        VA = '10'
        VEC.destroy()
        VOV = Tk()
        VOV.geometry('500x500')
        VOV.resizable(False, False)

        # Encabezado
        ICo = Image.open('Colombia.jpg').resize((100, 100))
        ICo2 = ImageTk.PhotoImage(ICo)
        ICo3 = tk.Label(VOV, image=ICo2)
        ICo3.place(x=0, y=0)

        IRe = Image.open('Registraduria.jpg').resize((100, 100))
        IRe2 = ImageTk.PhotoImage(IRe)
        IRe3 = tk.Label(VOV, image=IRe2)
        IRe3.place(relx = 1.0,
                        rely = 0.0,
                        anchor ='ne')

        LER5 = Label(VOV, text='ELECCIONES REGIONALES')
        LER5.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold"))  
        LER5.place(x=100, y=0, width=298, height=100)

        FrST5 = Frame(VOV)
        FrST5.config(bg='black', width=500, height=1)
        FrST5.place(x=0, y=101)

        # Título
        LCA = Label(VOV, text='Votaciones', justify="center")
        LCA.config(font=('Verdana', 15, "bold"))
        LCA.place(x=0, y=125, width= 500)

        # Texto
        Linfo3 = Label(VOV, text='Muchas gracias por  sufragar y hacer valer su   derecho  al  voto.  Si  hace   clíck  en "Terminar proceso electoral" se realizará el proceso  de   Escrutinio   y  obtendrá   los resultados  de  los   ganadores  y  algunas estadisticas  de  esta  votación.  Por  otra  parte si haces  clíck en el botón  "Registrar otro  voto"  te  llevará  a  la  ventana   de registro  donde otra persona podrá realizar su votación.', wraplength=300, anchor="n",justify=LEFT, width= 300, height= 100)
        Linfo3.config(fg=None, bg=None, font=('Verdana', 10))
        Linfo3.place(x=100, y=180, width= 300, height= 200)

        # Botón otro voto
        BRVA = Button(VOV, text='Registrar otro\nvoto', command=FRVRV, bg="#FFFFE0")
        BRVA.place(x=70, y=400)
        BRVA.config(width=20, height=2, font=('Verdana', 9))
        
        # Botón terminar
        BRVEC = Button(VOV, text='Terminar proceso\nelectoral', bg="#FFFFE0", command=FRE)
        BRVEC.place(x=270, y=400)
        BRVEC.config(width=20, height=2, font=('Verdana', 9))

        VOV.mainloop()
    else:
        messagebox.showwarning('Atención', 'Debe registrar por lo menos un voto en alguna de las corporaciones.')


# FRVEC = Funcion regresar a ventana eleccion corporacion
def FRVEC():
    if VA != '11':
        VCA.destroy()
        FVEC()
    elif VG != '11':
        VCG.destroy()
        FVEC()


# FCVBG = Funcion casilla voto en blanco gobernacion
def FCVBG():
    global VG
    ECG2.config(state=tkinter.NORMAL)
    ECG2.delete(0, END)
    ECG2.config(state="readonly")
    ECG3.config(state=tkinter.NORMAL)
    ECG3.delete(0, END)
    ECG3.config(state="readonly")
    ECG1.config(state=tkinter.NORMAL)
    ECG1.delete(0, END)
    ECG1.config(state="readonly")
    EVBG.config(state=tkinter.NORMAL)
    EVBG.delete(0, END)
    EVBG.insert(0, 'X')
    EVBG.config(state="readonly")
    VG = 'B'


# FCCG3 = Funcion casilla candidato gobernacion 3
def FCCG3():
    global VG
    ECG2.config(state=tkinter.NORMAL)
    ECG2.delete(0, END)
    ECG2.config(state="readonly")
    ECG1.config(state=tkinter.NORMAL)
    ECG1.delete(0, END)
    ECG1.config(state="readonly")
    EVBG.config(state=tkinter.NORMAL)
    EVBG.delete(0, END)
    EVBG.config(state="readonly")
    ECG3.config(state=tkinter.NORMAL)
    ECG3.delete(0, END)
    ECG3.insert(0, 'X')
    ECG3.config(state="readonly")
    VG = '3'


# FCCG2 = Funcion casilla candidato gobernacion 2
def FCCG2():
    global VG
    ECG1.config(state=tkinter.NORMAL)
    ECG1.delete(0, END)
    ECG1.config(state="readonly")
    ECG3.config(state=tkinter.NORMAL)
    ECG3.delete(0, END)
    ECG3.config(state="readonly")
    EVBG.config(state=tkinter.NORMAL)
    EVBG.delete(0, END)
    EVBG.config(state="readonly")
    ECG2.config(state=tkinter.NORMAL)
    ECG2.delete(0, END)
    ECG2.insert(0, 'X')
    ECG2.config(state="readonly")
    VG = '2'


# FCCG1 = Funcion casilla candidato gobernacion 1
def FCCG1():
    global VG
    ECG2.config(state=tkinter.NORMAL)
    ECG2.delete(0, END)
    ECG2.config(state="readonly")
    ECG3.config(state=tkinter.NORMAL)
    ECG3.delete(0, END)
    ECG3.config(state="readonly")
    EVBG.config(state=tkinter.NORMAL)
    EVBG.delete(0, END)
    EVBG.config(state="readonly")
    ECG1.config(state=tkinter.NORMAL)
    ECG1.delete(0, END)
    ECG1.insert(0, 'X')
    ECG1.config(state="readonly")
    VG = '1'


# FRVG= Funcion registrar voto gobernacion
def FRVG():
    global VGE
    if VG != '10':
        LiVG.append(VG)
        messagebox.showinfo('Información', 'Voto registrado correctamente')
        VGE = True
        VCG.destroy()
        FVEC()
    else:
        r = messagebox.showwarning('Atención', 'No ha escogido ningun candidato para la Gobernación')


# FVCG = Funcion ventana candidatos a la gobernacion
def FVCG():
    if VGE == False:

        # Ventana
        global VCG
        global VG
        VG = '10'
        VEC.destroy()
        VCG = Tk()
        VCG.geometry('500x500')
        VCG.resizable(False, False)

        # Encabezado
        ICo = Image.open('Colombia.jpg').resize((100, 100))
        ICo2 = ImageTk.PhotoImage(ICo)
        ICo3 = tk.Label(VCG, image=ICo2)
        ICo3.place(x=0, y=0)

        IRe = Image.open('Registraduria.jpg').resize((100, 100))
        IRe2 = ImageTk.PhotoImage(IRe)
        IRe3 = tk.Label(VCG, image=IRe2)
        IRe3.place(relx = 1.0,
                        rely = 0.0,
                        anchor ='ne')

        LER4 = Label(VCG, text='ELECCIONES REGIONALES')
        LER4.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold")) 
        LER4.place(x=100, y=0, width=298, height=100)

        FrST4 = Frame(VCG)
        FrST4.config(bg='black', width=500, height=1)
        FrST4.place(x=0, y=101)

        # Título
        LCG = Label(VCG, text='Candidatos a la Gobernación', justify="center")
        LCG.config(font=('Verdana', 15, "bold"))
        LCG.place(x=0, y=125, width= 500)

        # Candidato 1
        BCG1 = Button(VCG, text='Candidato G1', command=FCCG1, bg= "yellow")
        BCG1.place(x=40, y=220, height= 120, width= 100)
        global ECG1
        ECG1 = Entry(VCG, width=2, justify='center', state='readonly')
        ECG1.place(x=110, y=310)

        # Candidato 2
        BCG2 = Button(VCG, text='Candidato G2', command=FCCG2, bg="blue")
        BCG2.place(x=150, y=220, height= 120, width= 100)
        global ECG2
        ECG2 = Entry(VCG, width=2, justify='center', state='readonly')
        ECG2.place(x=220, y=310)

        # Candidato 3
        BCG3 = Button(VCG, text='Candidato G3', command=FCCG3, bg= "red")
        BCG3.place(x=260, y=220, height= 120, width= 100)
        global ECG3
        ECG3 = Entry(VCG, width=2, justify='center', state='readonly')
        ECG3.place(x=330, y=310)

        # Voto Blanco
        BVBG = Button(VCG, text='Voto en blanco', command=FCVBG, bg= "white")
        BVBG.place(x=370, y=220, height= 120, width= 100)
        global EVBG
        EVBG = Entry(VCG, width=2, justify='center', state='readonly')
        EVBG.place(x=440, y=310)

        # Botón Registrar voto
        BRVG = Button(VCG, text='Registrar voto\na la Gobernación', command=FRVG, bg="#FFFFE0")
        BRVG.place(x=70, y=420)
        BRVG.config(width=20, height=2, font=('Verdana', 9))

        # Botón Regresar
        BRVEC2 = Button(VCG, text='Regresar a la ventana\ncorporaciones', command=FRVEC, bg="#FFFFE0")
        BRVEC2.place(x=270, y=420)
        BRVEC2.config(width=20, height=2, font=('Verdana', 9))

        VCG.mainloop()
    else:
        messagebox.showwarning('Atención', 'El ciudadano ya sufrago en elecciones para Gobernación')


# FCVBA = Funcion casilla voto en blanco alcaldia
def FCVBA():
    global VA
    ECA2.config(state=tkinter.NORMAL)
    ECA2.delete(0, END)
    ECA2.config(state="readonly")
    ECA3.config(state=tkinter.NORMAL)
    ECA3.delete(0, END)
    ECA3.config(state="readonly")
    ECA1.config(state=tkinter.NORMAL)
    ECA1.delete(0, END)
    ECA1.config(state="readonly")
    EVBA.config(state=tkinter.NORMAL)
    EVBA.delete(0, END)
    EVBA.insert(0, 'X')
    EVBA.config(state="readonly")
    VA = 'B'


# FCCA3 = Funcion casilla candidato alcaldia 3
def FCCA3():
    global VA
    ECA2.config(state=tkinter.NORMAL)
    ECA2.delete(0, END)
    ECA2.config(state="readonly")
    ECA1.config(state=tkinter.NORMAL)
    ECA1.delete(0, END)
    ECA1.config(state="readonly")
    EVBA.config(state=tkinter.NORMAL)
    EVBA.delete(0, END)
    EVBA.config(state="readonly")
    ECA3.config(state=tkinter.NORMAL)
    ECA3.delete(0, END)
    ECA3.insert(0, 'X')
    ECA3.config(state="readonly")
    VA = '3'


# FCCA2 = Funcion casilla candidato alcaldia 2
def FCCA2():
    global VA
    ECA1.config(state=tkinter.NORMAL)
    ECA1.delete(0, END)
    ECA1.config(state="readonly")
    ECA3.config(state=tkinter.NORMAL)
    ECA3.delete(0, END)
    ECA3.config(state="readonly")
    EVBA.config(state=tkinter.NORMAL)
    EVBA.delete(0, END)
    EVBA.config(state="readonly")
    ECA2.config(state=tkinter.NORMAL)
    ECA2.delete(0, END)
    ECA2.insert(0, 'X')
    ECA2.config(state="readonly")
    VA = '2'


# FCCA1 = Funcion casilla candidato alcaldia 1
def FCCA1():
    global VA
    ECA2.config(state=tkinter.NORMAL)
    ECA2.delete(0, END)
    ECA2.config(state="readonly")
    ECA3.config(state=tkinter.NORMAL)
    ECA3.delete(0, END)
    ECA3.config(state="readonly")
    EVBA.config(state=tkinter.NORMAL)
    EVBA.delete(0, END)
    EVBA.config(state="readonly")
    ECA1.config(state=tkinter.NORMAL)
    ECA1.delete(0, END)
    ECA1.insert(0, 'X')
    ECA1.config(state="readonly")
    VA = '1'


# FRVA = Funcion registrar voto alcaldia
def FRVA():
    global VAE
    if VA != '10':
        LiVA.append(VA)
        messagebox.showinfo('Información', 'Voto registrado correctamente')
        VAE = True
        VCA.destroy()
        FVEC()
    else:
        r = messagebox.showwarning('Atención', 'No ha escogido ningun candidato para la Alcaldía')


# FVCA = Funcion ventana candidatos a la alcaldia
def FVCA():
    if VAE == False:

        # Ventana
        global VCA
        global VA
        VA = '10'
        VEC.destroy()
        VCA = Tk()
        VCA.geometry('500x500')
        VCA.resizable(False, False)

        # Encabezado
        ICo = Image.open('Colombia.jpg').resize((100, 100))
        ICo2 = ImageTk.PhotoImage(ICo)
        ICo3 = tk.Label(VCA, image=ICo2)
        ICo3.place(x=0, y=0)

        IRe = Image.open('Registraduria.jpg').resize((100, 100))
        IRe2 = ImageTk.PhotoImage(IRe)
        IRe3 = tk.Label(VCA, image=IRe2)
        IRe3.place(relx = 1.0,
                        rely = 0.0,
                        anchor ='ne')

        LER3 = Label(VCA, text='ELECCIONES REGIONALES')
        LER3.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold"))  
        LER3.place(x=100, y=0, width=298, height=100)

        FrST3 = Frame(VCA)
        FrST3.config(bg='black', width=500, height=1)
        FrST3.place(x=0, y=101)


        # Título
        LCA = Label(VCA, text='Candidatos a la Alcaldía', justify="center")
        LCA.config(font=('Verdana', 15, "bold"))
        LCA.place(x=0, y=125, width= 500)

        # Candidato 1
        BCA1 = Button(VCA, text='Candidato A1', command=FCCA1, bg= "yellow")
        BCA1.place(x=40, y=220, height= 120, width= 100)
        global ECA1
        ECA1 = Entry(VCA, width=2, justify='center', state='readonly')
        ECA1.place(x=110, y=310)

        # Candidato 2
        BCA2 = Button(VCA, text='Candidato A2', command=FCCA2, bg="blue")
        BCA2.place(x=150, y=220, height= 120, width= 100)
        global ECA2
        ECA2 = Entry(VCA, state='readonly', width=2, justify='center')
        ECA2.place(x=220, y=310)

        # Candidato 3
        BCA3 = Button(VCA, text='Candidato A3', command=FCCA3, bg= "red")
        BCA3.place(x=260, y=220, height= 120, width= 100)
        global ECA3
        ECA3 = Entry(VCA, state='readonly', width=2, justify='center')
        ECA3.place(x=330, y=310)

        # Voto Blanco
        BVBA = Button(VCA, text='Voto en blanco', command=FCVBA, bg= "white")
        BVBA.place(x=370, y=220, height= 120, width= 100)
        global EVBA
        EVBA = Entry(VCA, state='readonly', justify='center')
        EVBA.config(width=2)
        EVBA.place(x=440, y=310)

        # Botón Voto Alcaldía
        BRVA = Button(VCA, text='Registrar voto\na la Alcaldía', command=FRVA, bg="#FFFFE0")
        BRVA.place(x=70, y=420)
        BRVA.config(width=20, height=2, font=('Verdana', 9))

        # Botón Regresar
        BRVEC = Button(VCA, text='Regresar a la ventana\ncorporaciones', command=FRVEC, bg="#FFFFE0")
        BRVEC.place(x=270, y=420)
        BRVEC.config(width=20, height=2, font=('Verdana', 9))

        VCA.mainloop()
    else:
        messagebox.showwarning('Atención', 'El ciudadano ya sufrago en elecciones para Alcaldía')


# FVEC = Funcion ventana eleccion corporacion
def FVEC():

    # Ventana
    global VEC
    global VA
    global VG
    VA = '11'
    VG = '11'
    VEC = Tk()
    VEC.geometry('500x500')
    VEC.resizable(False, False)

    # Encabezado
    ICo = Image.open('Colombia.jpg').resize((100, 100))
    ICo2 = ImageTk.PhotoImage(ICo)
    ICo3 = tk.Label(VEC, image=ICo2)
    ICo3.place(x=0, y=0)

    IRe = Image.open('Registraduria.jpg').resize((100, 100))
    IRe2 = ImageTk.PhotoImage(IRe)
    IRe3 = tk.Label(VEC, image=IRe2)
    IRe3.place(relx = 1.0,
                 rely = 0.0,
                 anchor ='ne')

    LER2 = Label(VEC, text='ELECCIONES REGIONALES')
    LER2.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold"))
    LER2.place(x=100, y=0, width=298, height=100)

    FrST2 = Frame(VEC)
    FrST2.config(bg='black', width=500, height=1)
    FrST2.place(x=0, y=101)

    # Título
    LCor = Label(VEC, text='Corporaciones', justify ="center")
    LCor.config(font=('Verdana', 14, "bold"))
    LCor.place(x=0, y=125, width= 500)

    # Texto
    Linfo2 = Label(VEC, text='Para realizar la votación haga click en la corporación por la cual  desea  sufragar, puede  votar por  solo una o las  dos. Al terminar  de votar  seleccione  "Finalizar votación" para concluir.', wraplength=300, anchor="n",justify=LEFT, width= 300, height= 100)
    Linfo2.config(font=('Verdana', 10))
    Linfo2.place(x=100, y=185, width= 300, height= 100)

    # Botón Alcaldía
    BA = Button(VEC, text='Alcaldía', command=FVCA)
    BA.place(x=80, y=320, width=100)
    BA.config(font=('Verdana', 10))

    # Botón Gobernación
    BG = Button(VEC, text='Gobernación', command=FVCG)
    BG.place(x=350, y=320)
    BG.config(font=('Verdana', 10))

    # Botón Finalizar Votación
    BFV = Button(VEC, text='Finalizar votación', bg="#FFFFE0", command=FOVR)
    BFV.config(width=15, height=2, font=('Verdana', 9))
    BFV.place(x=200, y=420)

    VEC.mainloop()


# FCM = Funcion casilla masculino
def FCM():
    global S
    ESF.config(state=tkinter.NORMAL)
    ESF.delete(0, END)
    ESF.config(state="readonly")
    ESM.config(state=tkinter.NORMAL)
    ESM.delete(0, END)
    ESM.insert(0, 'X')
    ESM.config(state="readonly")
    S = '1'


# FCF = Funcion casilla femenino
def FCF():
    global S
    ESM.config(state=tkinter.NORMAL)
    ESM.delete(0, END)
    ESM.config(state="readonly")
    ESF.config(state=tkinter.NORMAL)
    ESF.delete(0, END)
    ESF.insert(0, 'X')
    ESF.config(state="readonly")
    S = '0'


# FRC = Funcion registrar cédula
def FRC():
    C = str(EC.get())
    Scs = C.count('0')+C.count('1')+C.count('2')+C.count('3')+C.count('4')+C.count('5')+C.count('6')+C.count('7')+C.count('8')+C.count('9')
    Ccs = C.count('')-1
    if (Ccs == Scs) and (S != '10'):
        if C != '':
            if ((C in LiC) == False):
                LiC.append(C)
                LiS.append(S)
                messagebox.showinfo('Información', 'Cédula registrada correctamente')
                VRV.destroy()
                FVEC()
            else:
                messagebox.showwarning('Información', 'El ciudadano ya sufragó en las presentes elecciones regionales')
        else:
            messagebox.showwarning("Atención", "Debe llenar todos los campos")
    elif (Ccs != Scs) and (S == '10'):
        messagebox.showwarning("Atención", "La cédula solo debe contener números enteros")
        messagebox.showwarning("Atención", "Debe llenar todos los campos")
    elif (Ccs != Scs):
        messagebox.showwarning("Atención", "La cédula solo debe contener números enteros")
    elif S == '10':
        messagebox.showwarning("Atención", "Debe llenar todos los campos")


# FRVRV = Funcion repetir ventana registro de votacion
def FRVRV():
    VOV.destroy()
    FVRV()


# FVRV = Funcion ventana registro de votacion
def FVRV():

    # Ventana
    global VRV
    global S
    global VAE
    global VGE
    S = '10'
    VAE = False
    VGE = False
    VRV = Tk()
    VRV.geometry('500x500')
    VRV.resizable(False, False)

    # Encabezado
    ICo = Image.open('Colombia.jpg').resize((100, 100))
    ICo2 = ImageTk.PhotoImage(ICo)
    ICo3 = tk.Label(VRV, image=ICo2)
    ICo3.place(x=0, y=0)

    IRe = Image.open('Registraduria.jpg').resize((100, 100))
    IRe2 = ImageTk.PhotoImage(IRe)
    IRe3 = tk.Label(VRV, image=IRe2)
    IRe3.place(relx = 1.0,
                 rely = 0.0,
                 anchor ='ne')

    LER = Label(VRV, text='ELECCIONES REGIONALES')
    LER.config(fg='Black', bg='#f7f7f7', font=('Verdana', 15, "bold"))
    LER.place(x=100, y=0, width=298, height=100)

    FrST = Frame(VRV)
    FrST.config(bg='black', width=500, height=1)
    FrST.place(x=0, y=101)

    # Título
    LRV = Label(VRV, text='Registro de votación', justify='center')
    LRV.config(font=('Verdana', 12, "bold"))
    LRV.place(x=0, y=115, width= 500)

    # Texto
    Linfo = Label(VRV, text='Ingrese  el  número  de  su   documento  de  identificación, sin  puntos  ni  comas. Luego seleccione la opción de su sexo y por ultimo  haga  click  en  el  botón  "Registrar Cédula" para continuar con el proceso.', wraplength=300, anchor="n",justify=LEFT, width= 300, height= 100)
    Linfo.config(font=('Verdana', 10))
    Linfo.place(x=100, y=165, width= 300, height= 100)

    # Cédula
    LC = Label(VRV, text='Cédula:')
    LC.config(font=('Verdana', 10))
    LC.place(x=120, y=280)
    global EC
    EC = Entry(VRV)
    EC.place(x=180, y=280)

    # Sexo
    LS = Label(VRV, text='Sexo:')
    LS.config(font=('Verdana', 10))
    LS.place(x=120, y=330)

    # Masculino
    BSM = Button(VRV, text='Masculino', command=FCM)
    BSM.place(x=170, y=329)
    BSM.config(font=('Verdana',9))

    global ESM
    ESM = Entry(VRV, justify='center')
    ESM.config(width=2, state=tkinter.DISABLED)
    ESM.place(x=250, y=332)

    # Femenino
    BSF = Button(VRV, text='Femenino', command=FCF)
    BSF.place(x=170, y=364)
    BSF.config(font=('Verdana',9))

    global ESF
    ESF = Entry(VRV, justify='center')
    ESF.config(width=2, state=tkinter.DISABLED)
    ESF.place(x=250, y=367)

    # Botón registrar cédula
    BRC = Button(VRV, text='Registrar Cédula', command=FRC, bg="#FFFFE0")
    BRC.config(width=15, height=2, font=('Verdana', 9))
    BRC.place(x=200, y=450)

    VRV.mainloop()

FVRV()
