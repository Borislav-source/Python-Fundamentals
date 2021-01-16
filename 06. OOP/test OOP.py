class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        result = [product for product in self.products if product[0] == first_letter]
        return result

    def __repr__(self):
        self.products = list(sorted(self.products))
        return f'''Items in the {self.name} Catalogue:
{self.products[0]}
{self.products[1]}
{self.products[2]}
{self.products[3]}
{self.products[4]}'''


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


