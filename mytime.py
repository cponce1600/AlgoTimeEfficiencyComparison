from datetime import datetime, date

def timeNow():
    now = datetime.now()
    #current_time = now.strftime("%H:%M:%S.%f")
    #print(" Time:", current_time)
    return now


def timeDiff(start, end):
    print(end - start)