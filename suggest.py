import utils

g = utils.read_graph("data1.json")

def suggest(user_id, qual):
    neighbors = g[user_id].neighbours
    collaborative = [set(g[user_id].posts[i]["likes"]) for i in g[user_id].posts]
    collaborative = set.union(*collaborative)
    content = set([i for i in collaborative if abs(g[i].avg - qual) <= 0.05])
    return content.union(neighbors)

f = suggest(1, 0.3)
d = [97, 2, 67, 68, 70, 18, 54, 86, 27, 60]
print(sorted([i for i in d if i in f]))
print(sorted(f))

