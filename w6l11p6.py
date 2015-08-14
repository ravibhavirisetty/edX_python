
class Queue(object):

    def __init__(self):
        self.vals = []

    def insert(self, x):
        self.vals.append(x)

    def remove(self):
        try:
            return self.vals.pop()
        except:
            raise ValueError('ValueError')

