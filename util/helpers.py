def removeUnicodeCharacters(line):
    """Removes all unicode characters for stuff like degrees etc. from steps/ingredients

    Args:
        line (String): [line to be edited]

    Returns:
        [String]: [Cleaned line with no extra unicode characters]
    """
    fixedline = line
    fixedline = fixedline.replace("\n", "")
    fixedline = fixedline.replace("\u00a0", " ")
    fixedline = fixedline.replace("\u00b0", " degrees ")
    fixedline = fixedline.replace("\u02da", " degrees ")
    fixedline = fixedline.replace("\u00bc", "1/4")
    fixedline = fixedline.replace("\u00bd", "1/2")
    fixedline = fixedline.replace("\u00be", "3/4")
    fixedline = fixedline.replace("\u2153", "1/3")
    fixedline = fixedline.replace("\u2154", "2/3")
    fixedline = fixedline.replace("\u00bc", "1/4")
    fixedline = fixedline.replace("\u2019", "'")
    fixedline = fixedline.replace("\u00f1", "n")
    return fixedline


def buildJsonRecipe(title, img, overview, ingredients, steps):
    """Given valid inputs, will create a json object representing the recipe

    Args:
        title (String): Title of recipe
        img (String): image link 
        overview (String): overview paragraph
        ingredients (Array[String]): list of ingredients
        steps (Array[String]): list of steps

    Returns:
        Dict: json  object for recipe
    """
    recipe = {
        "id" : "",
        "name" : "",
        "prepTime": 0,
        "imageLink": "",
        "categories" : [],
        "ingredients" : [],
        "steps": [],
        "rating" : {
            "stars" : 0,
            "ratings" : 0
        }
    }
    recipe["name"] = title
    recipe["imageLink"] = img
    if(len(overview) > 0):
        recipe["prepTime"] = overview[-2:][0]
    else:
        recipe["prepTime"] = "0"
    recipe["ingredients"] = ingredients
    recipe["steps"] = steps

    return recipe


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def summarizeDataPrintMissingInfo(filename):
    linecounter = 0
    errorReport = []
    with open(filename) as file:
        for line in file:
            if "Missing Title" in line:
                errorReport.append("ERROR: Missing title on line " + str(linecounter))
            if "Missing Image" in line:
                errorReport.append("ERROR: Missing image link on line " + str(linecounter))
            if "prepTime" in line and "0" in line:
                errorReport.append("WARNING: No preptime found for recipe on line " + str(linecounter))
            if "ingredients" in line and "[]" in line:
                errorReport.append("ERROR: No ingredients found for recipe on line " + str(linecounter))
            if "steps" in line and "[]" in line:
                errorReport.append("ERROR: No steps found for recipe on line " + str(linecounter))
            linecounter = linecounter + 1

    for item in errorReport:
        print(item)
