from abc import ABC, abstractmethod

class Cupcake(ABC):

    size="regular"
    def __init__(self,name,price,flavor,frosting,filling):
        
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting
        self.sprinkles=[]
        self.filling=filling

    def add_sprinkles(self,*args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
        return self.sprinkles
    
    @abstractmethod 
    def calculate_price(self,quantity):
        return quantity*self.price

class Mini(Cupcake):
    size="Mini"

    def __init__(self,name,price,flavor,frosting):
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting

my_cupcake=Cupcake('Cookies and Cream',2.99,'Chocolate','Oreo',['White'],'Vanilla')

# my_cupcake.frosting = "Chocolate"
# my_cupcake.filling = "Chocolate"
# my_cupcake.name = "Triple Chocolate"

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)

# print(my_cupcake.add_sprinkles('red','blue','green'))

my_minicake=Mini('Cookies and Cream',2.99,'Chocolate','Oreo')
print(my_minicake.name)
print(my_minicake.price)
