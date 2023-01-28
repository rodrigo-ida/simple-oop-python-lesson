class Food():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


    def describe(self):
        print('this food is called {} and it is a kind of {}'.format(self.name, self.kind))


food1 = Food('banana', 'fruit')
food1.describe()


