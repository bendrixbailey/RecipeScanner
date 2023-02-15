import requests
from bs4 import BeautifulSoup as bs
import json
import pandas as ps


site = "SimplyRecipes"


def parseDown(overview, ingredients):
    
    finalOverview = []
    finalIngredients = []
    for line in overview.stripped_strings:
        #if(line[:1].isdigit()):
            finalOverview.append(line)
    
    for line in ingredients.get_text().split("\n"):
        if(len(line)>1 and line[:1].isdigit()):
            finalIngredients.append(line.strip("\n"))

    
    return finalOverview, finalIngredients

def scrapeSimplyRecipes(webdata):
    id = "structured-project-content_1-0"
    soupedData = bs(webdata.content, "html.parser")
    recipeContent = soupedData.find(id)
    recipeOverview = soupedData.find("div", {"id":"project-meta_1-0"})
    recipeIngredients = soupedData.find("div", {"id":"structured-ingredients_1-0"})

    print(parseDown(recipeOverview, recipeIngredients))


def buildJsonRecipe(overview, ingredients):
    finalObject = {}
    

    # print(overviewContent.get_text())
    # print(recipeIngredients.get_text())


def scrapeGeneric(webdata):
    soupedData = bs(webdata.content, "html.parser")
    for line in soupedData.stripped_strings:
        print(line)
    


def main():
    command = ""
    print("\
        Website scraper for recipes. Must be customized per website.\n\
        Enter the url of the webpage to search. If successful, a json object will be\n\
        added to the file specified. If file is not specified/doesnt exist, a new one will\n\
        be created.\n\
        type 'exit' to quit.\n\
        ")
    filename = input("Enter name for file to save data to: ")

    while(command != "exit"):
        command = input("Webpage Url> ")
        if(command != "exit"):
            if(command == "test"):
                webdata = requests.get("https://www.simplyrecipes.com/lemony-baked-cod-with-wild-rice-and-fennel-recipe-5224339")
            else:
                webdata = requests.get(command)

            scrapeSimplyRecipes(webdata)
            #scrapeGeneric(webdata)
            # with open(filename + ".json", "w") as outfile:
            #     json.dump(webdata.json(), outfile, indent=4)
            # print("Data saved to " + filename + ".json")
        

            


main()