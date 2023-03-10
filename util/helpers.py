def removeUnicodeCharacters(line):
    """Removes all unicode characters for stuff like degrees etc. from steps/ingredients

    Args:
        line (String): [line to be edited]

    Returns:
        [String]: [Cleaned line with no extra unicode characters]
    """
    fixedline = line
    fixedline = fixedline.replace("\u00a0", " ")
    fixedline = fixedline.replace("\u00b0", " degrees ")
    fixedline = fixedline.replace("\u02da", " degrees ")
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
    recipe["prepTime"] = overview[-2:][0]
    recipe["ingredients"] = ingredients
    recipe["steps"] = steps

    return recipe