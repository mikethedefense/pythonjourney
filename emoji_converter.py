# Convert Old School Emojis to Modern ones.
# Simple example of commonly used emojis.

def emoji_converter(emoji):
    emojis = {":)": '🙂', ":]": "😊",":>":"😀", ":D":"😃", "XD":"😆", ":'(":"😥", ":|": "😐", "-_-": "😑", ":')": "😂",":‑,": "😘",":(":"🙁", ":[": "😡"}
    try:
        return emojis[emoji] 
    except KeyError:
        return "This emoji does not exist in our list."

print(emoji_converter(":)"))
