"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
 pictures or other items. We want to create the text that should be displayed next to such an item.

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return ", ".join(names[:2]) + f" and {names[2]} like this"
    elif len(names) > 3:
        return ", ".join(names[:2]) + f" and {len(names)-2} others like this"