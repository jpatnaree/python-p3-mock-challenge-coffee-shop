from statistics import mean

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if isinstance(new_name, str) and len(new_name) >= 3:
                self._name = new_name
            else:
                raise Exception('must be a string & at least 3 characters long')
        else:
            raise Exception('cannot be change')
        
    def orders(self):
        return [o for o in Order.all if o.coffee == self]
    
    def customers(self):
        return list(set([o.customer for o in Order.all if o.coffee == self]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        price = [o.price for o in Order.all if o.coffee == self]
        return mean(price)

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception('must be a string & have 1 - 15 characters')
        
    def orders(self):
        return [o for o in Order.all if o.customer == self]
    
    def coffees(self):
        return list(set([o.coffee for o in Order.all if o.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(coffee):
        pass

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not hasattr(self,'_price'):
            if isinstance(new_price, float) and 1.0 <= new_price <= 10.0:
                self._price = new_price
            else:
                raise Exception('Wrong!')
        else:
            raise Exception('cannot be changed')