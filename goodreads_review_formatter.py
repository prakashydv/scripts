import csv_to_json

# usage: python goodreads_review_formatter.py <csv_filepath>
# e.g. python goodreads_review_formatter.py "/Users/sigma_male/Downloads/2025-05-11_goodreads_library_export.csv"

# Headers: 
    # Book Id :  769658
    # Title : Battlefield Earth: A Saga of the Year 3000
    # Author : L. Ron Hubbard
    # Author l-f : Hubbard, L. Ron
    # Additional Authors :
    # ISBN :
    # ISBN13 :
    # My Rating :
    # Average Rating : 3.55
    # Publisher : Galaxy Press
    # Binding: Paperback
    # Number of Pages: 1050
    # Year Published: 2001
    # Original Publication Year: 1982
    # Date Read: 
    # Date Added: 2025/02/16
    # Bookshelves: currently-reading, fiction
    # Bookshelves with positions: currently-reading (#4), fiction (#7)
    # Exclusive Shelf: currently-reading
    # My Review: 
    # Spoiler: 
    # Private Notes: 
    # Read Count: 1
    # Owned Copies: 0

def getMarkdownReview(jsonReview):
    # print(jsonReview)
    return f"""
## {jsonReview["Title"]} - {jsonReview["Author"]}
#### read on {jsonReview["Date Read"]} | rating {jsonReview["My Rating"]} (avg. {jsonReview["Average Rating"]})
""" + ("\n" + jsonReview["My Review"] + "\n") if jsonReview["My Review"] != "" else ""

def format_review(csv_filepath):
    out_str = ""
    jsonReviews = csv_to_json.csvToJson(csv_filepath)
    for jsonReview in jsonReviews:
        if jsonReview["Date Read"] != "":
            out_str += getMarkdownReview(jsonReview)
    return out_str

import sys
str = format_review(sys.argv[1])
f = open(f"{sys.argv[1]}.md", "w")
f.write(str)
f.close()
