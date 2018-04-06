from bs4 import BeautifulSoup
from urllib.request import urlopen

csv_file = open("contact_list.csv", "w")

url = "https://scrapebook22.appspot.com/"

response = urlopen(url).read()

soup = BeautifulSoup(response, "lxml")



for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com/" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html, "lxml")
        email = person_soup.find("span", attrs={"class": "email"}).string
        ime_priimek = person_soup.find("div", attrs={"class": "col-md-8"}).find("h1").string

        li_span_list = person_soup.findAll("li")
        kraj_bivanja_link = li_span_list[2]
        kraj_bivanja = kraj_bivanja_link.find("span").string

        csv_file.write(ime_priimek + ", " + email + ", " + kraj_bivanja + "\n")

csv_file.close()
