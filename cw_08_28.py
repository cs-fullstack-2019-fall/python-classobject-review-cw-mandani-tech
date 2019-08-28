# # Python classes review graded
#
# ### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that will print
# the value of all the properties/attributes of the Movie class
#
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
#
# Remember, this is the basic model of a Python file with a class
# ```
class Movie:
    def __init__(self,movieName,rating,yearReleased):# initialize my template /instances
        self.movieName=movieName
        self.rating=rating
        self.yearReleased=yearReleased # Class constructor code and property handling
    def __str__(self):
        return f'The Movie name :{self.movieName}\n' \
               f'The movie rating : {self.rating}\n' \
               f'The year of release : {self.yearReleased}\n' \


#
#     OTHER PROPERTIES AND METHODS HERE
#
def main():
# # Create class instance(s) and perform other activities in/from this function
    myMovie=Movie("FastNFurious",5,2019)
    print(myMovie)
#
main()
# ```
#


# ### Problem 2:
# Create a class Product that represents a product sold online.
#
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
#
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
#
# #
class Product():
    def __init__(self, price, quantity, name): # initialize my template /instances
        self.price=price
        self.quantity=quantity
        self.name=name

    def __str__(self):
        return  f'The Product Price is : {self.price}\n'\
                f'The Product Quantity is : {self.quantity}\n'\
                f'The Product Name is : {self.name}\n'
def main():
    # # Create class instance(s) and perform other activities in/from this function
    myproduct_1=Product(25,300,"Pens")
    myproduct_2=Product(300,1,"Laptop")
    print(myproduct_1)
    print(myproduct_2)
#
main()
