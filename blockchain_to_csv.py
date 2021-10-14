import csv
from os import listdir, getcwd, system
from os.path import isfile, join, splitext
import xlsxwriter


replaceValues = {"received": "Received",
                     "sent": "Sent",
                     "note": "Note",
                     "tx": "Origin address",
                     "exchange_rate_then": "Exchange rate then",
                     "value_now": "Value now",
                     "value_then": "Value then",
                     "amount": "Amount",
                     "type": "Type",
                     "token": "Token",
                     "time": "Time",
                     "ï»¿\"date\"": "Date"
                    }

def main():
    print("\n\n")

    for fileName in listdir():

        if not fileName.endswith(".csv"):
            #print("Invalid format " + fileName)
            continue

        splitExt = splitext(fileName)[0]
        outFileName = splitExt + "_results.xlsx"

        workbook = xlsxwriter.Workbook(outFileName)
        worksheet = workbook.add_worksheet("Bitcoin history")


        with open(fileName, 'r') as file:

            reader = csv.reader(file)
            rowCount = 2

            for row in reader:

                columnCount = 2

                for value in row:

                    if value in replaceValues:
                        value = replaceValues[value]

                    worksheet.write(rowCount, columnCount, value)
                    columnCount += 1

                rowCount += 1


        workbook.close()

        print("File processed successfully " + fileName + " -> " + outFileName)


main()
