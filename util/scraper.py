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

    soupedData = bs(webdata.content, "html.parser")

    # print(websiteType.TITLE.value)
    # print(websiteType.IMG.value)
    # print(websiteType.OVERVIEW.value)
    # print(websiteType.INGREDIENTS.value)
    # print(websiteType.STEPS.value)

    # recipeTitle = soupedData.find(websiteType.TITLE.value)
    # recipeImg = soupedData.find(websiteType.IMG.value)
    # recipeOverview = soupedData.find(websiteType.OVERVIEW.value)
    # recipeIngredients = soupedData.find(websiteType.INGREDIENTS.value)
    # recipeSteps = soupedData.find(websiteType.STEPS.value)

    recipeTitle = soupedData.find(websiteType.TITLE.value["class"], {websiteType.TITLE.value["identifier"] : websiteType.TITLE.value["value"]})
    recipeImg = soupedData.find(websiteType.IMG.value["class"], {websiteType.IMG.value["identifier"] : websiteType.IMG.value["value"]})
    recipeOverview = soupedData.find(websiteType.OVERVIEW.value["class"], {websiteType.OVERVIEW.value["identifier"] : websiteType.OVERVIEW.value["value"]})
    recipeIngredients = soupedData.find(websiteType.INGREDIENTS.value["class"], {websiteType.INGREDIENTS.value["identifier"] : websiteType.INGREDIENTS.value["value"]})
    recipeSteps = soupedData.find(websiteType.STEPS.value["class"], {websiteType.STEPS.value["identifier"] : websiteType.STEPS.value["value"]})

    #print(recipeOverview)

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