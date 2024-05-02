from abc import ABC, abstractmethod
import csv
from pprint import pprint


class Cupcake(ABC):

    size="regular"
    def __init__(self,name,price,flavor,frosting,filling):
        
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting
        self.filling=filling
        self.sprinkles=[]

    def add_sprinkles(self,*args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
        return self.sprinkles
    
    @abstractmethod 
    def calculate_price(self):
        pass

class Mini(Cupcake):
    size="Mini"

    def __init__(self,name,price,flavor,frosting):
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting
        self.sprinkles=[]

    def calculate_price(self,quantity):
        return quantity*self.price

class Regular(Cupcake):
    size="Regular"
    def __init__(self,name, price, flavor,frosting,filling):
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting
        self.filling=filling
        self.sprinkles=[]
    
    def calculate_price(self,quntity):
        return quntity*self.price
    
class Large(Cupcake):
    size="large"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name=name
        self.price=price
        self.flavor=flavor
        self.frosting=frosting
        self.filling=filling
        self.sprinkles=[]

    def calculate_price(self,quantity):
        return quantity*self.price


# my_cupcake=Cupcake('Cookies and Cream',2.99,'Chocolate','Oreo',['White'],'Vanilla')
# my_cupcake.frosting = "Chocolate"
# my_cupcake.filling = "Chocolate"
# my_cupcake.name = "Triple Chocolate"

# my_cupcake.is_miniature = False
# print(my_cupcake.is_miniature)

# print(my_cupcake.add_sprinkles('red','blue','green'))

minicake=Mini('Cookies and Cream',1.99,'Chocolate','Oreo')
minicake.add_sprinkles('red','blue','green')

regularcake=Regular("Triple Chocolate",2.99,"Chocolate","Chocolate","Chocolate")
regularcake.add_sprinkles('white','golden')

largecake=Large("Strawberry",3.99,"Strawberry","Vanilla","Vanilla")
largecake.add_sprinkles('white','pink')

def read_csv(file):
    with open(file) as csvfile:
        reader=csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

# read_csv('starter/sample.csv')

def add_cupcake(file, cupcakes):
    with open(file,'a', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        # writer.writeheader()
        for cupcake in cupcakes:
            if hasattr(cupcake,"filling"):
                writer.writerow({"size":cupcake.size,"name":cupcake.name, "price":cupcake.price, "flavor":cupcake.flavor, "frosting":cupcake.frosting, "sprinkles":cupcake.sprinkles, "filling":cupcake.filling})
            else:
                writer.writerow({"size":cupcake.size,"name":cupcake.name, "price":cupcake.price, "flavor":cupcake.flavor, "frosting":cupcake.frosting, "sprinkles":cupcake.sprinkles})
    print(f"Data has been added to the {file}")

def write_new_file(file):
    with open(file,'w', newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()


write_new_file('new_sample.csv')
add_cupcake('new_sample.csv',[minicake,regularcake,largecake])