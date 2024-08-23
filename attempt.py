import utils
from posts import Post
import random

g = utils.read_graph()
p = Post(random.choice([i.user for i in g]))
g[p.user].add_post(p)
op = p.user


def feedback():
    pass


def propagate(centre, level):
    pass


def choose(centre):
    neighbours = sorted(g[centre].edges, key=lambda x: x[1], reverse=True)
    k = random.randint(0, (len(neighbours) - 1) // 2)
    likes = neighbours[:k]
    k = random.randint(0, (len(neighbours) - 1) // 3)
    commenter = neighbours[:k]


def changes():
    pass
