from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json
import pandas as ps


def main():
    print("\
        Website scraper for recipes. Must be customized per website.\n\
        Enter the url of the webpage to search. If successful, a json object will be\n\
        added to the file specified. If file is not specified/doesnt exist, a new one will\n\
        be created.\n\
        ")
    filename = input("Enter the name of the file to put the json object into: ")

    driver = webdriver.Chrome()


main()