#Imports
import requests
from bs4 import BeautifulSoup
import lxml



#Variables
site = "https://omni.se/senaste"

#data= {"title": Title}

#Functions
def check_request(r):
    if r.status_codes == 200:
        print(f"The status code is, {requests.status_codes}")
    else:
        print(f"Request success, status code is {requests.status_codes}")



#Main
if __name__ == "__main__":
    soup = BeautifulSoup(requests.get(site).content, "lxml") #Gör en request till site

    print(soup.prettify())
    #c = soup.select("main")
    #print(c)
    c = soup.find_all('a', class_="article-link")[1]

    

    print(c)
