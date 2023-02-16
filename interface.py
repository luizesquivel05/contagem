import tkinter as tk
  
def lerCONTEUDO():
    dados = conteudo.get()
    
    if str(dados)[0] == "C" or str(dados)[0] == "c":
        tk.Label(font=('Montserrat', 12), text=f"VAMOS FAZER UMA CONTAGEM CRESCENTE!\t\t\t\t\t\t").place(x=5, y=160)
        tk.Label(font=('Montserrat', 12), text=f"    VALOR INICIAL\t\tVALOR FINAL").place(x=5, y=180)
        valorINICIAL = tk.Entry(home, font=('Montserrat', 14),); valorINICIAL.place(x=25, y=200)
        valorFINAL = tk.Entry(home, font=('Montserrat', 14)); valorFINAL.place(x=250, y=200)
        valores = tk.Button(home, font=('Montserrat', 14), text="ENVIAR VALORES", fg='white', background='red', command=irCONTAGEM); valores.place(x=400, y=200)
    else: 
        tk.Label(font=('Montserrat', 12), text=f"VAMOS FAZER UMA CONTAGEM DECRESCENTE!").place(x=5, y=160)
        tk.Label(font=('Montserrat', 12), text=f"    VALOR INICIAL\t\tVALOR FINAL").place(x=5, y=180)
        valorINICIAL = tk.Entry(home, font=('Montserrat', 14),); valorINICIAL.place(x=25, y=200)
        valorFINAL = tk.Entry(home, font=('Montserrat', 14)); valorFINAL.place(x=250, y=200)
        valores = tk.Button(home, font=('Montserrat', 14), text="ENVIAR VALORES", fg='white', background='red', command=irCONTAGEM); valores.place(x=400, y=200)

    def irCONTAGEM():
        ini = valorINICIAL.get()
        fim = valorFINAL.get()
        contagem(ini, fim)

def contagem(ini, fim):
    isx = 10
    isy = 500
    for i in range(ini, fim):
        tk.Label(master=home, font=('Montserrat', 12), text=f"{i}").place(x=isx, y=isy)
        isx += 50
home = tk.Tk()
home.geometry('600x300')
home.wm_iconbitmap('count.ico')
home.resizable(False, False)
home.title("Contador | HOME")
tk.Label(font=('Montserrat', 20), text="CONTADOR").place(x=150, y=10)
tk.Label(font=('Montserrat', 18), text="Nos diga se deseja crescente ou decrescente").place(x=50, y=60)
conteudo = tk.Entry(home, font=('Montserrat', 14)); conteudo.place(x=30, y=120)
enviarCONTEUDO = tk.Button(master=home, font=('Montserrat', 14), text="ENVIAR ORDEM", fg='white', background='red', command=lerCONTEUDO); enviarCONTEUDO.place(x=300, y=120)
home.mainloop()