import csv
import codecs
import argparse

parser = argparse.ArgumentParser(description="Конвертировать экспорт Кинориума в CSV для Letterboxd")
parser.add_argument("csv_file", help="путь к CSV-файлу Кинориума")
args = parser.parse_args()

with open("votes_for_letterboxed.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\n")
    file_writer.writerow(["Title", "Year", "Rating10"])
    csvReader = csv.DictReader(codecs.open(args.csv_file, 'r', 'utf-16'), delimiter='\t')
    for row in csvReader:
        if row['Type'] in ("Фильм", "Мультфильм"):
            file_writer.writerow([row['Original Title'] or row['Title'], row['Year'], row['My rating']])
