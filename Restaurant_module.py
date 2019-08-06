class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=0
    def describe_restaurant(self):
        print("Restaurant "+self.restaurant_name.title()+' with '+self.cuisine_type.lower())
    def open_restaurant(self):
        print("The restaurant "+self.restaurant_name.title()+" is open")
    def clients_served(self):
        print('Served '+str(self.number_served)+ " so far")
    def update_clients_served(self, newNumServed):
        self.number_served=newNumServed
    def increment_clients_served(self, addServed):
        self.number_served+=addServed
