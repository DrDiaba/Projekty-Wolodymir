import tkinter as tk
from pydoc import text
from tkinter import messagebox

root = tk.Tk()
root.title("My first GUI")
root.geometry("500x500")


tk.Label(root, text="Inwestor:").grid(row=0, column=0, padx=5, pady=5)
Kto = tk.Entry(root)
Kto.grid(row=0, column=1, padx=5, pady=5)

metry = tk.DoubleVar()

tk.Label(root, text="Ilość (m²/szt):").grid(row=1, column=0, padx=5, pady=5)
entry_ilosc = tk.Entry(root, textvariable=metry)
entry_ilosc.grid(row=1, column=1)


tk.Label(root, text="Kod Rabatowy").grid(row=2, column=0, padx=5, pady=5)
Rabat = tk.Entry(root)
Rabat.grid(row=2, column=1)


wybor = tk.IntVar()
wybor.set(1) # Domyślnie zaznaczona pierwsza opcja

tk.Radiobutton(root, text="Farba (20 zł)", variable=wybor, value=1).grid(row=3, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="Tynk (40 zł)", variable=wybor, value=2).grid(row=4, column=0, padx=5, pady=5)
tk.Radiobutton(root, text="Płytki (100 zł)", variable=wybor, value=3).grid(row=5, column=0, padx=5, pady=5)

Logic = tk.IntVar()
Logic.set(1) # Domyślnie zaznaczona pierwsza opcja

transport_var = tk.BooleanVar()
transport_var.set(True)
wniesienie_var = tk.BooleanVar()

cb1 = tk.Checkbutton(root, text="Transport (+50 zł)", variable=transport_var)
cb1.grid(row=6, column=0, padx=5, pady=5)

cb2 = tk.Checkbutton(root, text="Wniesienie (+100 zł)", variable=wniesienie_var)
cb2.grid(row=7, column=0, padx=5, pady=5)


Raport = tk.Text(root, width=40, height=12, wrap="word")
Raport.grid(row=9, column=0, columnspan=2)

def oblicz():
    try:

        ilosc = float(metry.get())

        imie = Kto.get()

        if imie == "":
            messagebox.showerror("error", "Wpisz imie inwestora")
            return



        if ilosc > 0:

            material = 0
            kodik = "Nie Uzywany"
            transport = "Darmowy"
            imie = Kto.get()


            if wybor.get() == 1:
                material = 20
            elif wybor.get() == 2:
                material = 40
            elif wybor.get() == 3:
                material = 100


            discount = Rabat.get().upper()
            if discount == "RABAT10":
             material = material * 0.9
             kodik = "Uzywany"

            elif discount == "":
             kodik = "Nie używany"

            else:
                Raport.delete("1.0", tk.END)
                Raport.insert(tk.END, "BŁĄD: Niepoprawny kod")
                return

            koszt = material * ilosc



            if transport_var.get():

                if koszt >= 1000 or ilosc > 50 :
                    transport = "Darmowy"
                else:
                    koszt += 50
                    transport = "Platny (50zl)"




            Raport.delete("1.0", tk.END)
            Raport.insert(tk.END,
                          f"Thanks for purchase! Mr.{imie} Kod rabatowy jest {kodik} | Trasport jest {transport} | Summa jest {koszt}  ")



        else:
            messagebox.showerror("error", "Wiencej niz 0")





    except ValueError:
        Raport.delete("1.0", tk.END)
        Raport.insert(tk.END, "Błąd! Wpisz poprawną liczbę.")

przycisk = tk.Button(root, text="Uruchom", command=oblicz)
przycisk.grid(row=8, column=0, columnspan=2, sticky="we")



root.mainloop()