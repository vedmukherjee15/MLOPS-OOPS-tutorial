class employee:
    def __init__(self):
        print("Variable initialization started")
        self.id = 123
        self.designation = "AI Engineer/ Data Scientist"
        self.salary = 1000000
        print("Variable initialization finished")

    def travel(self,destination):
        print(f"Employee is travelling to {destination}")


vedaant = employee()


print(vedaant.designation)

vedaant.travel("London")





