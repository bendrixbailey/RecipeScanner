import requests
from util.scraper import *
import configparser
import json


site = "SimplyRecipes"


def main():
    command = ""
    print("\
        Website scraper for recipes. Must be customized per website.\n\
        Enter the url of the webpage to search. If successful, a json object will be\n\
        added to the file specified. If file is not specified/doesnt exist, a new one will\n\
        be created.\n\
          \n\
        You can also supply a text file, and the program will create a recipe for every link in the text. Will skip errors.\
        type 'exit' to quit.\n\
        ")
    filename = input("Enter name for file to save data to. Will default to recipe.json if no name is provided: ")
    if(filename == ""):
        filename = "recipe"

    while(command != "exit"):
        command = input("Webpage Url> ")
        if(command != "exit" or command != "quit"):
            if(command == "test"):
                webdata = requests.get("https://www.simplyrecipes.com/lemony-baked-cod-with-wild-rice-and-fennel-recipe-5224339")
            else:
                webdata = requests.get(command)

            if("simplyrecipes" in command):
                result = scrapeSimplyRecipes(webdata, "simplyrecipes")
            if("test" in command):
                break
            
            
            with open(filename + ".json", "w") as outfile:
                json.dump(result, outfile, indent=4)
            print("Data saved to " + filename + ".json")
        

main()