import requests
from util.scraper import *
from util.webtags import *
import json
import ssl
import time
import certifi
from urllib.request import urlopen
import argparse

argparser = argparse.ArgumentParser()
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    link = ""
    infile = ""
    outfile = ""
    replaceOutput = False

    ingroup = argparser.add_mutually_exclusive_group()
    ingroup.add_argument("-l", "--link", help="link to recipe webpage")
    ingroup.add_argument("-f", "--file", help="Name of file with links to process")
    argparser.add_argument("-o", "--out", "-output", help="name of file to output to")
    argparser.add_argument("-r", "--replace", help="If included, will overwrite output file", action="store_true")
    arguments = argparser.parse_args()

    link = arguments.link
    infile = arguments.file
    outfile = arguments.out
    replaceOutput = arguments.replace

    #print(link + "-" + infile + "-" + outfile + "-" + replaceOutput)
    #print(replaceOutput)

    if(outfile == None):
        outfile = "recipe"

    result = ""
    if(link != None):
        #if theres a link, check if its a test run or not
        if(link == "test"):
            webdata = urlopen("https://www.simplyrecipes.com/lemony-baked-cod-with-wild-rice-and-fennel-recipe-5224339").read()
            result = scrapeWebsite(webdata, simplyrecipes)
        else:
            webdata = urlopen(link).read()
            if("simplyrecipes" in link):
                result = scrapeWebsite(webdata, simplyrecipes)
            if("allrecipes" in link):
                result = scrapeWebsite(webdata, allrecipes) 

    if(infile != None):
        #if theres a file, process it
        result = []
        numlinks = 0
        lineNum = 0
        with open(infile) as file:
            numlinks = len(file.readlines())
            file.seek(0)
            #call to external progress bar function to visually display, as theres lots of delay to this
            printProgressBar(0, numlinks, prefix="Progress", suffix="Converted", length=50)
            for line in file:
                webdata = urlopen(line).read()
                tempLine = ""
                #new recipe website checks will be added here
                if("simplyrecipes" in line):
                    tempLine = scrapeWebsite(webdata, simplyrecipes)
                if("allrecipes" in line):
                    tempLine = scrapeWebsite(webdata, allrecipes) 
                if(result != ""):
                    result.append(tempLine)
                printProgressBar(lineNum + 1, numlinks, prefix="Progress", suffix="Converted", length=50)
                lineNum = lineNum + 1

    if(replaceOutput):
        with open(outfile + ".json", "w") as outputfile:
            json.dump(result, outputfile, indent=4)
    else:
        # if append is selected, need to do funky json loading so it stays valid
        with open(outfile + ".json") as inputfile:
            try:
                data = json.load(inputfile)
                #print(data)
                for item in result:
                    #print(item)
                    data.append(item)
                result = data
            except json.decoder.JSONDecodeError:
                pass

        with open(outfile + ".json", "w") as outputfile:
            json.dump(result, outputfile, indent=4)
    
    print("Data saved to " + outfile + ".json")
    #show helpful summary just to warn of some missing data program couldnt find
    summarizeDataPrintMissingInfo(outfile + ".json")
            
        

main()