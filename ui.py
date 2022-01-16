from number_gen import fill_txt  
from csvToArr import csvToArray, printArray
from mytime import timeNow, timeDiff
from sort import bubbleSort, selectionSort, insertionSort, mergeSort, quickSort

def ui():
    while(True):
        print("Would you like to generate new files or use existing")
        files = input("1 = new files 2 = existing files. Type quit to quit\n")
        if(files == 'quit'):
            break
        elif(files == 1):
            size = int(input("select amount of numbers to be generated\n"))
            fill_txt('userGen.csv', size)
            files = 'userGen.csv'
        #if 1 is not inpiuted then the user will be directed to select a pregenerated file 
        else:
            print("Please input a pregenrated file: 5k.csv, 25k.csv, 80k.csv, 150k,csv, 300k.csv")
            files = input("(input should be name of files)\n")
        filearr = csvToArray(files)
        getSorter(filearr)

def getSorter(filearr):
    while(0==0):
        print("Which algorithm would you like to use: bubble, selection, insertion, merg, quick")
        sorter = input("(input should be name of algorithm) type quit to end\n")
        if(sorter == "bubble"):
            x = timeNow()
            bubbleSort(filearr)
            y = timeNow()
            timeDiff(x, y)
        elif(sorter == "selection"):
            x = timeNow()
            selectionSort(filearr)
            y = timeNow()
            timeDiff(x, y)
        elif(sorter == "insertion"):
            x = timeNow()
            insertionSort(filearr)
            y = timeNow()
            timeDiff(x, y)
        elif(sorter == "merg"):
            x = timeNow()
            mergeSort(filearr)
            y = timeNow()
            timeDiff(x, y)
        elif(sorter == "quick"):
            x = timeNow()
            quickSort(filearr, 0, len(filearr)-1)
            y = timeNow()
            timeDiff(x, y)
        elif(sorter == 'quit'):
            break
        else:
            print('invalid sorter please try again')