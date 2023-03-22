import requests
from util.scraper import *
from util.webtags import *
import json
import ssl
import time
import certifi
from urllib.request import urlopen


site = "SimplyRecipes"
ssl._create_default_https_context = ssl._create_unverified_context

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
        result = ""
        if(command != "exit" or command != "quit"):
            if(command == "test"):
                #webdata = requests.get("https://www.simplyrecipes.com/lemony-baked-cod-with-wild-rice-and-fennel-recipe-5224339", verify=False)
                webdata = urlopen("https://www.simplyrecipes.com/lemony-baked-cod-with-wild-rice-and-fennel-recipe-5224339").read()
                result = scrapeWebsite(webdata, simplyrecipes)
            elif(".txt" in command):
                #how to open a file and read line by line python?
                result = []
                numlinks = 0
                lineNum = 0
                with open(command) as file:
                    numlinks = len(file.readlines())
                    file.seek(0)
                    printProgressBar(0, numlinks, prefix="Progress", suffix="Converted", length=50)
                    for line in file:
                        webdata = urlopen(line).read()
                        tempLine = ""
                        if("simplyrecipes" in line):
                            tempLine = scrapeWebsite(webdata, simplyrecipes)
                        if("allrecipes" in line):
                            tempLine = scrapeWebsite(webdata, allrecipes) 
                        if(result != ""):
                            result.append(tempLine)
                        printProgressBar(lineNum + 1, numlinks, prefix="Progress", suffix="Converted", length=50)
                        lineNum = lineNum + 1

            else:
                #webdata = requests.get(command)
                start = time.time()
                webdata = urlopen(command).read()
                if("simplyrecipes" in command):
                    result = scrapeWebsite(webdata, simplyrecipes)
                if("allrecipes" in command):
                    result = scrapeWebsite(webdata, allrecipes) 
                end = time.time()
                print(end-start)
        
            with open(filename + ".json", "w") as outfile:
                json.dump(result, outfile, indent=4)
            print("Data saved to " + filename + ".json")
            
        

main()