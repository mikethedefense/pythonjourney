# PageRank algorithm

# Variables
links = [('a','b'), ('a','c'), ('b','c'), ('c','b')]
d= {}
results = {}
score = 1
damping_factor = 0.85

# Main Code

# Iterate through the list of tuples and add them to a dict
for link, outgoing in links:
    d.setdefault(link, []).append(outgoing) 

# Iterate through the dict containing the links and outgoing links and add them to a result dict 
for link in d: 
    score = 1
    for j in range(10):
        score = (score/len(d[link])) * damping_factor # Equation is: score / number of outgoing links * damping factor typically set to 0.85
        results[link] = score
   
# Print the results 
print(results)
