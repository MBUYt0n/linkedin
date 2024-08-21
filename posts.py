import random
import time


class Post:
    def __init__(self):
        self.time = time.time()
        self.likes = random.randint(0, 50)
        self.comments = random.randint(0, 25)
        self.views = random.randint(0, 100)
        self.quality = random.random()

    def inc_views(self):
        self.views += 1

    def inc_likes(self):
        self.likes += 1

    def inc_comments(self):
        self.comments += 1


d = [Post() for i in range(10)]
for i in d:
    i.inc()
    print(i.likes, i.comments, i.views)
    print(i.quality)
