class employee:
    # Dunder method -> Constructor 
    # Example use of Constructor : so whenver we use Facebook, the database conection is defined inside the constructor so whenver the app is started the backend gets automatically connected
    def __init__(self):
        print("Variable initialization started")
        print(id(self))
        self.id = 123
        self.designation = "AI Engineer/ Data Scientist"
        self.salary = 1000000
        print("Variable initialization finished")

    def travel(self,destination):
        print(f"Employee is travelling to {destination}")


vedaant = employee()

# An attribute can always be defined outside the class
vedaant.name = "Vedaant Mukherjee"

print(vedaant.name)

#print(id(vedaant))

print(vedaant.designation)

vedaant.travel("London")





