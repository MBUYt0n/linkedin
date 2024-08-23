import utils
from posts import Post
import random

g = utils.read_graph()
p = Post(random.choice([i.user for i in g]))
g[p.user].add_post(p)
print("Post added to user", p.user)