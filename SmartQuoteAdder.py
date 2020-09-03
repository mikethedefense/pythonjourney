# Write a function that takes an ASCII string and returns a string with double quotes which are replaced with smart quotes.

def quote_converter(quote):
    smart_quote_open = "\u201C"
    smart_quote_close = "\u201D"
    final = ''
    opening = True
    for character in quote:
        if character == "'":
            if opening == True:
                final += smart_quote_open
                opening = False
            else:
                final += smart_quote_close
                opening = True
        else:
            final += character
    return final

print(quote_converter("'Hello my friend', he said. 'What a nice day', he said again."))
