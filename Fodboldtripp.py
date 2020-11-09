import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import pickle

filename = "betalinger.pk"
total = 36000
#  Import og difinitioner


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.main()
#  Klassen

    def main(self):
        self.totalPay = float(sum(fodboldtur.values()))
        if self.totalPay == 0:
            self.payPercent = 0
        else:
            self.payPercent = self.totalPay / total * 100
        #  Udregning af mængden af 36000 kr, der er betalt i %

        self.progress = ttk.Progressbar(self, orient="horizontal", length=250, mode="determinate")
        self.progress["value"] = self.payPercent
        self.progress.pack(side="top")
        #  Progressbar

        self.listKnap = tk.Button(self, text="Vis liste", command=self.makeList)
        self.listKnap.pack(side="left")
        #   Knap til at åbne en liste

        self.betalKnap = tk.Button(self, text="Tilføj betaling", command=self.makeBetal)
        self.betalKnap.pack(side="left")
        #   Knap til at åbne betalingsvinduet

        self.quit = tk.Button(self, text="Luk", fg="red", command=self.master.destroy)
        self.quit.pack(side="right")
        #   Knap til at lukke programmet

    def makeList(self):
        self.listWindow = tk.Toplevel(root)
        self.listWindow.title("Liste")
        self.listWindow.geometry("300x200")
        #  Listevinduet

        self.listBox = tk.Listbox(self.listWindow)
        self.listBox.pack(fill="both")
        for item in fodboldtur.items():
            self.listBox.insert(tk.END, item)
        #  Listen

        self.quitList = tk.Button(self.listWindow, text="Luk liste", fg="red", command=self.listWindow.destroy)
        self.quitList.pack(side="bottom")
        #  Knap til at lukke listevinduet

    def makeBetal(self):
        self.betalWindow = tk.Toplevel(root)
        self.betalWindow.title("Betaling")
        self.betalWindow.geometry("300x200")
        #  Betalingsvinduet

        self.personLabel = Label(self.betalWindow, text="Vælg person:")
        self.personLabel.pack(side="top")
        self.personInput = ttk.Combobox(self.betalWindow, values=list(fodboldtur.keys()))
        self.personInput.pack(side="top")
        #  Label og input af hvem der betaler

        self.betalLabel = Label(self.betalWindow, text="Vælg værdi:")
        self.betalLabel.pack(side="top")
        self.betalInput = tk.Entry(self.betalWindow)
        self.betalInput.pack(side="top")
        #  Label og input af hvad der bliver betalt

        self.betalKnap = tk.Button(self.betalWindow, text="Betal", command=self.betaling)
        self.betalKnap.pack(side="top")
        #  Knap til at betale

        self.quitBetal = tk.Button(self.betalWindow, text="Luk betaling", fg="red",
                                   command=self.betalWindow.destroy)
        self.quitBetal.pack(side="bottom")
        #  Knap til at lukke betalingsvinduet

    def betaling(self):
        try:
            self.personValue = self.personInput.get()
            self.betalValue = int(self.betalInput.get())

            fodboldtur[self.personValue] += self.betalValue

            print(self.betalValue, "kroner tilføjet til", self.betalInput)

            self.totalPay = float(sum(fodboldtur.values()))
            self.payPercent = self.totalPay / total * 100
            print(self.payPercent)

            self.progress["value"] = self.payPercent

            outfile = open(filename, 'wb')
            pickle.dump(fodboldtur, outfile)
            outfile.close()

        except:
            print("err")
        #  Opdatering af alt efter en betaling har fundet sted

infile = open(filename, "rb")
fodboldtur = pickle.load(infile)
infile.close()
root = tk.Tk()
root.title("Fodboldtur")
app = Application(master=root)
app.mainloop()
#  Kør de forskellige funktioner.
