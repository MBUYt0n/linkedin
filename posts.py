import random
import time


class Post:
    def __init__(self, user):
        self.user = user
        self.time = time.time()
        self.likes = []
        self.comments = []
        self.views = []
        self.quality = random.random()

    def inc_views(self, user):
        for u in list(set(user)):
            self.views.append(u)

    def inc_likes(self, user):
        for u in list(set(user)):
            self.likes.append(u)

    def inc_comments(self, user):
        for u in list(set(user)):
            self.comments.append(u)

