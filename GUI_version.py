import csv
import codecs
from tkinter import *
import tkinter.filedialog as fd
from tkinter import messagebox as mb


def main():
    def fromkinorium2letterboxd():
        kinorium_path = str(txt_in_data.get())
        csvReader = csv.reader(codecs.open(kinorium_path, 'rU', 'utf-16'), delimiter='\t')
        letterboxd_rows = [["Title", "Year", "Rating10"]]
        for row in csvReader:
            if (row[4] == "Фильм" or row[4] == "Мультфильм") and (row[0] != ""):
                if (row[3] != ""):
                    letterboxd_rows.append([row[3], row[5], row[0]])
                else:
                    letterboxd_rows.append([row[2], row[5], row[0]])
        with open("letterboxd.csv", mode="w", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file)
            file_writer.writerows(letterboxd_rows)


    def start():
        fromkinorium2letterboxd()
        mb.showinfo("Готово", "Файл letterboxd.csv сформирован")

    window = Tk()
    window.geometry('500x300')

    lbl_in_data = Label(window, text="CSV-файл из Кинориума:")
    lbl_in_data.place(relx=0.01, rely=0.01)

    txt_in_data = Entry(window, width=50)
    txt_in_data.place(relx=0.01, rely=0.1)
    txt_in_data.config(state=DISABLED)

    def choose_file():
        filetypes = (("CSV-файл", "*.csv"),
                     ("Любой", "*"))
        filename =fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        if filename:
            txt_in_data.config(state=NORMAL)
            txt_in_data.insert(0, filename)
            txt_in_data.config(state=DISABLED)

    btn_in_data = Button(window, text="Выбрать файл", command=choose_file)
    btn_in_data.place(relx=0.65, rely=0.08)

    btn_in_data = Button(window, text="Сформировать CSV-файл для Letterboxd", command=start)
    btn_in_data.place(relx=0.01, rely=0.3)

    window.mainloop()

main()
