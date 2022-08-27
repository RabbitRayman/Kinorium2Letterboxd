import csv
import codecs

with open("votes_for_letterboxed.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\n")
    file_writer.writerow(["Title", "Year", "Rating10"])
    csvReader = csv.reader(codecs.open('votes.csv', 'rU', 'utf-16'), delimiter='\t')
    for row in csvReader:
        if (row[4] == "Фильм" or row[4] == "Мультфильм") and (row[0] != ""):
            if (row[3] != ""):
                file_writer.writerow([row[3], row[5], row[0]])
            else:
                file_writer.writerow([row[2], row[5], row[0]])
