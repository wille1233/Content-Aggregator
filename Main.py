##Imports
import requests
from bs4 import BeautifulSoup
import lxml



##Variables
site = "https://www.dn.se/"
data = ""
menu = True # Disable/enable menu


##Functions

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
        print("data saved!")
        for data in soup.find_all("p"): 
            f.write(data.get_text())
            f.write("\n")
        print("Data saved!")

#Menu Functions
def options():
    print("""-=Options=-\n
    [1] Choose website\n
    [2] Save to data.txt\n
    [3] Send to mail(WIP)\n
    [4] Launch Program\n
    [0] Exit Program\n""")

def option_1():
    print(f"Currently choosen site: {site}")
    change = input("Do you wish to change website? Y/N\n >> ").capitalize
    if change == "YES" or "Y":
        change_site = input("Input link: ")
        print(f""""{change_site}" has been choosen!""")
    else:
        print("site saved")

def option_2():
    enable_text_save = input("Do you want to save text to data.txt? Y/N\n >> ")
    save_text()

def option_3():
    print("Work in progress.")




def Menu(menu):
    print("-=Welcome to Content Aggregator=-\n")
    while menu:
        options()
        choise = int(input("Choose Option: "))
    
        if choise == 1:
            option_1()
        elif choise == 2:
            option_2()
        elif choise == 3:
            option_3()
        elif choise == 4:
            menu = False
        elif choise == 0:
            quit()
        else:
            print("Invalid choise!")





##Main
if __name__ == "__main__":
    
    soup = BeautifulSoup(requests.get(site).content, "lxml") #Gör en request till site
    Menu(menu)
    check_request() #Checks request
    save_text() #Sparar text till data.txt
    
    

    