from bs4 import BeautifulSoup as bs
import configparser
from util.helpers import *


config = configparser.ConfigParser()
config.read('util/websites.ini')

def scrapeWebsite(webdata, websiteType):
    """Logic for scraping the SimplyRecipes website. Method will only work, as it needs tags for specific information sections

    Args:
        webdata (webdata from requests get method): [description]

    Returns:
        [type]: [description]
    """
    finalOverview = []
    finalIngredients = []
    finalSteps = []
    id = "structured-project-content_1-0"

    soupedData = bs(webdata.content, "html.parser")

    recipeTitle = soupedData.find("h1", {"class":"heading__title"})
    recipeImg = soupedData.find("img", {"id":"mntl-sc-block-image_1-0-2"})
    recipeOverview = soupedData.find("div", {"id":"project-meta_1-0"})
    recipeIngredients = soupedData.find("div", {"id":"structured-ingredients_1-0"})
    recipeSteps = soupedData.find("div", {"id" : "structured-project__steps_1-0"})

    #None check each item and only proceed if the item is found. If not, log it.
    if(recipeTitle == None):
        title = "Missing Title"
    else:
        title = recipeTitle.get_text()
    
    if(recipeImg == None):
        img = "Missing Image"
    else:
        img = recipeImg.get("data-src")

    if(recipeOverview != None):
        for line in recipeOverview.stripped_strings:
            if(line[:1].isdigit()):
                finalOverview.append(line)
    if(recipeIngredients != None):
        for line in recipeIngredients.get_text().split("\n"):
        #if(len(line)>1 and line[:1].isdigit()):
            if(len(line)>1):
                finalIngredients.append(removeUnicodeCharacters(line.strip("\n")))
    if(recipeSteps != None):
        recipeSteps.find("figure").decompose()
        stepcounter = 1

        for line in recipeSteps.stripped_strings:
            if(line.split(' ')[0] != "Simply"):
                if(":" not in line):
                    line = str(stepcounter) + ". " + line
                    stepcounter += 1
                finalSteps.append(removeUnicodeCharacters(line)) 
                #print(line)

    



    return buildJsonRecipe(title, img, finalOverview, finalIngredients, finalSteps)