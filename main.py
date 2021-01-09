import tkinter as tk
from pathlib import Path
import os
import datetime
from tkinter.font import Font
from webbrowser import open_new_tab

#Semplice recorder di attività che mantiene un diario di tutte le attività eseguite e inviate al file
#Il file viene in salvato in /home/user/SimpleActivityDiary/

class HistoryView ():
    def __init__(self,upperLevel):
        self.upperLevel = upperLevel
        self.upperLevel.resizable(False,False)
        self.upperLevel.title("Simple Activity Diary - Storico")

        try:
            with open(str(Path.home())+"\\SimpleActivityDiary\\activitiesLog.txt","r") as file:
                reader = file.readlines()
                shower = tk.Text(upperLevel)
                for line in reader:
                    shower.insert(tk.INSERT,str(line))
                    stringa = "-"*144 + "\n"
                    shower.insert(tk.END,stringa)
                shower.pack(pady=15,padx=15)
                shower.configure(state=tk.DISABLED,font=Font(family="Helvetica",size=12))
        except FileNotFoundError:
            tk.Label(upperLevel,text="Non esiste nessuna cronologia...\nScrivi prima qualcosa!",font=Font(family="Helvetica",size=12)).pack()

        
            
        def deleteSafety():

            def cleaner():
                shower.delete(0,tk.END)
                clearance = open(str(Path.home())+"\\SimpleActivityDiary\\activitiesLog.txt","w")
                clearance.close()
                upperLevel.destroy()
                popup.destroy()

            popup = tk.Tk()
            popup.resizable(False,False)
            popup.title("WARNING")
            tk.Label(popup,text="Stai per eliminare la cronologia, continuare?",font=Font(family="Helvetica",size=14),bg="red").pack(pady=10)
            tk.Button(popup, text="Si",width=15,font=Font(family="Helvetica",size=14),bg="red",command=cleaner).pack()
            tk.Button(popup, text="No",width=15,font=Font(family="Helvetica",size=14),command=popup.destroy).pack(pady=10)
            popup.mainloop()

        tk.Button(upperLevel,text="Pulisci",command=deleteSafety).pack(pady=15)
    
           

class MainView ():
    
    def __init__(self,master):
        self.master = master
        self.master.title("Simple Activity Diary")
        self.master.geometry("500x175")
        self.master.resizable(False,False)

        if os.path.exists(str(Path.home())+"\\SimpleActivityDiary") == False:
            os.mkdir(str(Path.home())+"\\SimpleActivityDiary")    
        
        def saver ():
            now = datetime.datetime.now()
            toAppend = f'{now.strftime("%m/%d/%Y, %H:%M:%S")} : {grepper.get()}\n'
            fileToOpen = str(Path.home()) + "\\SimpleActivityDiary\\activitiesLog.txt"
            if os.path.exists(fileToOpen):
                with open(fileToOpen,"a") as file:
                    file.write(toAppend)
            elif os.path.exists(fileToOpen) == False:
                with open(fileToOpen,"w") as file:
                    file.write(toAppend)
            grepper.delete(0, tk.END)
        
        def history ():
            engineTwo = tk.Toplevel()
            upperLevel = HistoryView(engineTwo)
            engineTwo.mainloop()
        
        def creditsOpener():
            open_new_tab("https://github.com/NicolaM94/Simple-Activity-Diary")


        tk.Label(text="Inserisci la tua attività qui sotto: ").pack()
        grepper = tk.Entry(width=400)
        grepper.pack(pady=10,padx=10)

        tk.Button(text="Salva",command=saver).pack(pady=10)
        tk.Button(text="Storico",command=history).pack(pady=5)
        tk.Button(text="GitHub Project",command=creditsOpener).pack(pady=5)

if __name__ == "__main__" :
    engine = tk.Tk()
    master = MainView(engine)
    engine.mainloop()