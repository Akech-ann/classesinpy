class Fruits:
    quantity=0
    def __init__(self,name,taste,color):
        self.name=name
        self.taste=taste
        self.color=color
    def add_fruits(self,quant):
        self.quantity+=quant
        return f"There are now {self.quantity}{self.name}"
    
    def remove_fruits(self,quant):
        self.quantity-=quant
        return f"There are now {self.quantity}{self.name}"
    def eat_fruit(self):
        return f"Eat this {self.name} make sure to enjoy"
       

        
        