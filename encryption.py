# Encryption using the periodic table of elements

elements = ["h", "he", "li", "be", "b", "c", "n", "o", "f", "ne", "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca", "sc",
"ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr",
"nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "sb", "te", "i", "xe", "cs", "ba", "la",
"ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb",
"dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi",
"po", "at", "rn", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "md", "no",
"lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "og"]

text = input("Enter text to encrypt:")
text = text.lower()
grouped_text = [text[i:i+2] for i in range(0,len(text),2 )]
encrypted_text_list = []
single_text = []

for i in grouped_text:
    if i in elements:
        encrypted_text_list.append(str(elements.index(i) + 1))
    else:
        single_text = []
        single_text.append(i)
        single_text = [i for i in "".join(single_text)]
        for j in single_text:
            if j in elements:
                encrypted_text_list.append(str(elements.index(j)+1))
            else:
                encrypted_text_list.append(j)

encrypted_text = "".join(encrypted_text_list)
print(encrypted_text)
