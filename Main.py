##Imports
import requests
from bs4 import BeautifulSoup
import lxml
from datetime import date



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

def save_text(save):
    if save == "Y":
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(get_date())
            for data in soup.find_all("p"): 
                f.write(data.get_text())
                f.write("\n")
            print("Data saved!")
    else:
        pass

def get_date():
    today = str(date.today())
    return today

#Menu Functions

def option_1():
    print(f"Currently choosen site: {site}")
    change = input("Do you wish to change website? Y/N\nNote that your website might not work, only some do.\n >> ").capitalize
    if change == "Y":
        change_site = input("Input link: ")
        print(f""""{change_site}" has been choosen!""")
        return change_site
    else:
        print("Site Saved")

def option_3():
    print("Work in progress.")


def Main(menu):
    print("-=Welcome to Content Aggregator=-\n")
    text_save_enabled = {} #Save placeholder

    while menu:

        print(f"""-=Options=-\n
        [1] Choose website, Currently set to: {site}\n
        [2] Save to data.txt, Currently set to: {text_save_enabled}\n
        [3] Send to mail(WIP)\n
        [4] Launch Program\n
        [0] Exit Program\n""")

        choise = int(input("Choose Option: "))
    
        if choise == 1:
            option_1()
        elif choise == 2:
            text_save_enabled = str(input("Do you want to enable save text to data.txt? Y/N\n >> ")).capitalize
            if text_save_enabled == "N":

                for data in soup.find_all("p"): 
                    print(data.get_text())
            else:

                text_save_enabled = "Y"

            #choise_is_2 = True
        elif choise == 3:
            option_3()
        elif choise == 4:
            menu = False
        elif choise == 0:
            quit()
        else:
            print("Invalid choise!")
        
    check_request() #Checks request
    save_text(str(text_save_enabled)) #Spara text till data.txt om det är påslaget


##Main
if __name__ == "__main__":
    while True:
        soup = BeautifulSoup(requests.get(site).content, "lxml") #Gör en request till site
        Main(menu)

        
    

    
    

    