# AltSpellings
This Python script takes a list of alternate spellings for nouns and ensures that each noun is associated with all of its alternate spellings. It processes the list of words, adds a common description, adds any alternate spellings for each, with an output that adheres to the standard formatting conventions of CSW24.

## Creating the List of Words
<p>The easiest way to do this is to search by Definition in Zyzzyva. For example, if you want all the alternate spellings of JELAB, you can choose the Definition parameter and put JELAB in the search bar. You'll (hopefully) find all the alternate spellings of the word. Right-click on the list, choose Save List, and save <i>just the word</i> as a text file. Each alternate spelling will be on its own line.</p>
<p><h4>Important note:</h4> Alternate spellings appended to a definition <b>do not</b> contain the word that is being defined. <b><i>Don't forget to add the word that you searched for</i> (in this example, JELAB) <i>to the text file or it won't be updated!</i></b></p>

## Using the Script
Download the repo and make sure to edit the alt_spellings.py file to enter the file paths for that list you just saved and your output file. If you're not sure how path files work, <a href="https://github.com/ithaka/constellate-notebooks/blob/master/Python-intermediate/python-intermediate-3.ipynb">this</a> may help!

The file will save as a CSV, largely because this project was the result of a frustrated attempt at solving the GALABEYA problem---i.e. updating every godforsaken alternate spelling with the new CSW24 addition in the Crowdsourced Definitions project.

This script currently only works on nouns that are pluralized with an S. If the root word ends in a Y, you may have to manually check the definition of its plural form to correct the root word in the csv file.
