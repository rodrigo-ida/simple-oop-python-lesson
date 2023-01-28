from food import Food

class Fruit(Food):

    def __init__(self, name, kind='fruit'):
        super().__init__(name,kind='fruit')

    def clean(self):
        print('cleaning up the {}'.format(self.name))

    def __repr__(self):
        return 'the return of the class. this food is called {}, it is a kind of {}'.format(self.name,self.kind)



fruta = Fruit('limao')
fruta.clean()
fruta.describe()
print(fruta)