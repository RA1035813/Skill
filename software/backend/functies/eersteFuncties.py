from datetime import datetime

def getDate():
    return datetime.now().strftime('%Y-%m')


# print(getDate())