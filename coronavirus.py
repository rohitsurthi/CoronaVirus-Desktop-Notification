from plyer import notification
import requests
import time
from bs4 import BeautifulSoup

def Notification(head , data):
    notification.notify(title = head ,
                        message = data ,
                        timeout = 20
                        #also add icon using app_icon = "icon file address"
                        )

def getData(url):
    result = requests.get(url)
    return result.text

if __name__ == "__main__":
    while(True):
        htmlData = getData("https://www.mohfw.gov.in/") #data from this website
        soup = BeautifulSoup(htmlData,"html.parser")
        dataString = ""

        for tr in soup.find_all('tbody')[1].find_all('tr'):
            dataString  += tr.get_text()
        dataString = dataString[1:]
        itemli = dataString.split("\n\n")
        myState = ["Telengana"] #Add your state here

        for item in itemli[0:23]:
            dataList = item.split("\n")
            if(dataList[1] in myState):
                print(dataList)
                heading = "CoronaVirus"
                caseData = f"{dataList[1]}:\n Indian:{dataList[2]} Cases\n Foreign:{dataList[3]} Cases\n Cured:{dataList[4]} & Deaths:{dataList[5]} "
                Notification(heading,caseData)
                time.sleep(7200)
