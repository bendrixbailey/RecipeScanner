# RecipeScanner
Small program to scan a recipe webpage and assemble a json list for import into a document database

As of now, it only works with Simplyrecipes.com and Allrecipes.com. Can easily be configured for more.

# How to use

The program is run via command line, and has options for either a single link, or a file with links on new lines for batch processing. You can specify a filename to write to, whether to overwrite it, or to write it to a default file named recipe.json

### Usage Types

```python app.py -l <link to recipe> -f <name of file> -o <name of output file> -r <if included, will overwrite output file>```

For example, say you want to search one link, and put it in a file named hamburger.txt. Here is how it would work

```python app.py -l www.coolrecipes.com/besthamburger -o hamburger.txt```

# Planned changes/features

- Moved to AWS lambda, triggered by sending an email
- Support for taking a search result in supported website, then gathers links, then extracts the data
- Integration with clearcook recipe website backend database