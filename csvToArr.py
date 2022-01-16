import csv

def csvToArray(csvFile):
    csvArr = []
    f = open(csvFile, 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            for e in row:
                csvArr.append(int(e))
    return csvArr

def printArray(arr):
    for i in arr: 
        print(i)


  
