from enum import Enum

#Class to hold data for the simplyrecipes website
class simplyrecipes(Enum):
    TITLE = {
        "class" : "h1",
        "identifier" : "class",
        "value" : "heading__title"
    }
    IMG = {
        "class" : "figure",
        "identifier" : "id",
        "value" : "primary-image_1-0"
    }
    # IMG = {
    #     "class" : "div",
    #     "identifier" : "class",
    #     "value" : "img-placeholder"
    # }
    OVERVIEW = {
        "class" : "div",
        "identifier" : "class",
        "value" : "loc total-time project-meta__total-time"
    }
    INGREDIENTS = {
        "class" : "div",
        "identifier" : "id",
        "value" : "structured-ingredients_1-0"
    }
    STEPS = {
        "class" : "div",
        "identifier" : "id",
        "value" : "structured-project__steps_1-0"
    }


class allrecipes(Enum):
    TITLE = {
        "class" : "h1",
        "identifier" : "id",
        "value" : "article-heading_1-0"
    }
    IMG = {
        "class" : "div",
        "identifier" : "class",
        "value" : "img-placeholder"
    }
    OVERVIEW = {
        "class" : "div",
        "identifier" : "id",
        "value" : "recipe-details_1-0"
    }
    INGREDIENTS = {
        "class" : "ul",
        "identifier" : "class",
        "value" : "mntl-structured-ingredients__list"
    }
    STEPS = {
        "class" : "ol",
        "identifier" : "id",
        "value" : "mntl-sc-block_2-0"
    }