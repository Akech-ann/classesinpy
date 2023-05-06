class Car:
 speed=0
 def __init__(self,make,model,carnumber):
     self.self=self
     self.make=make
     self.carnumber=carnumber
     

 def car_start(self):
        return "Starting the engine"
 def car_accelerate(self, kmh):
        self.speed += kmh
        return f"Accelerating to {self.speed} kmh"
 def car_stop(self):
        self.speed = 0
        return f"The car is stopping {self.speed}"





























    