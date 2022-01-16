import random

import csv

def fill_txt(textfile, totalNumbers):
    #the code below clears the file just to make sure it generates the correct amount of numbers 
    clear = open(textfile, "w")
    clear.truncate()
    clear.close()
    #this code writes the numbers 
    with open(textfile, 'w') as file:
        writer = csv.writer(file)
        for i in range(totalNumbers):
            b= [random.randint(1, 5000000)]
            writer.writerow(b)

def genSetData():
    fill_txt('5k.csv', 5000)
    fill_txt('25k.csv', 25000)
    fill_txt('80k.csv', 80000)
    fill_txt('150k.csv', 150000)
    fill_txt('300k.csv', 300000)

                

    





        

    

    