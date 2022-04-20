#Imports
import requests
from bs4 import BeautifulSoup
import lxml



#Variables
site = "https://www.dn.se/"
data = ""


#Functions

def get_text():
    for data in soup.find_all("p"): 
        print(data.get_text())

def check_request():
    try:
        r = requests.get(site)
        print(f"Request success, status code is {r.status_code}")
    except:
        print(f"Request was unsuccessful, status code is {r.status_code}")

def save_text():
    with open("data.txt", "w") as f:
        for data in soup.find_all("p"): 
            f.write(data.get_text())
            f.write("\n")
        print("Data saved!")






#Main
if __name__ == "__main__":

    soup = BeautifulSoup(requests.get(site).content, "lxml") #Gör en request till site

    check_request() #Checks request
    #get_text()
    save_text()
    
    

    