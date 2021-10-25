import csv

with open('investigados.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file, fieldnames=[
                                        "Partido A", 
                                        "Partido B", 
                                        "Partido C", 
                                        "Partido D", 
                                        "Partido E", 
                                        "Partido F", 
                                        ])
    
    csv_reader.__next__()
    
    list_total = []

    for row in csv_reader:

        if row["Partido A"] == None:
            break

        try: 
            print( row["Partido A"] + ', ' + row["Partido B"] + ', ' + row["Partido C"] + ', ' + row["Partido D"] + ', ' + row["Partido E"] + ', ' + row["Partido F"])

            total = 0

            for part in row:
                if part:
                    
                    str = row[part].split(';')[-1].replace(',', '.').replace(' ', '')
                    
                    if str != '':
                        total += float(str)

            list_total.append(total)
        except:
            pass

    print(list_total)
    """total = 0

    for part in row:
        if part:
            
            str = row[part].split(';')[-1]
            print(part)

            if str != '':
                total += float(str)

    list_total.append(total)"""

    #print(list_total)
        #str = row["Partido A"].split(';')[-1]
        #total = float(str)

        #print(row["Partido A"])
        #print(total)