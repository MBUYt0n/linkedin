import random
import time


class Post:
    def __init__(self, user):
        self.user = user
        self.time = time.time()
        self.likes = set()
        self.comments = set()
        self.views = set()
        self.quality = random.random()
        self.id = random.randint(0, 1000000)

    def inc_views(self, user):
        for u in user:
            self.views.add(u)

    def inc_likes(self, user):
        for u in user:
            self.likes.add(u)

    def inc_comments(self, user):
        for u in user:
            self.comments.add(u)
