# Define a class
class employee():
    def __init__(self, name, basesalary, bonushrs, sales):
        self.name = name
        self.basesalary = basesalary
        self.bonushrs = bonushrs
        self.sales = sales
        

# Function that avoid repetition of the sentence
    def employees(self):
        print("name {} ,base salary {} ,bonushrs {}, sales {}".format(self.name ,self.basesalary, self.bonushrs, self.sales))

# Nominate the information of the employee
employee1 = employee("Ahmed mountasir", 20000, 20, 15)
employee2 =employee("Rachid Benghouzil", 16000, 10, 20)
employee1.employees()
employee2.employees()
