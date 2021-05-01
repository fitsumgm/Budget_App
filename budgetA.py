#*******OOP programming, budget App*****

class Category:

    def __init__(self, category, amount): 

        self.category = category
        self.amount = amount

    def deposit(self, amount):

        amount = int(input("How much would you like like to deposit in to your {} category: \n".format(self.category)) )
        print("you've successfully deposited {} to your {} category \n".format(amount, self.category))

        self.amount += amount;
        return ("YOur balance is {}".format(self.amount))


    def withdraw(self, amount):

        amount = int(input("How much would you like to withdraw from your {} category: \n".format(self.category)))
        print("You've successfully withdrawn {} from your {} category".format(amount, self.category))

        self.amount -= amount;
        return self.amount


    def check_balance(self, amount):

        if self.amount > amount:
            return True
        else:
            return False
            

    def transfer(self, amount):
        self.withdraw(amount) 
        return Car_category.deposit(amount)


Vacation_category = Category('Vacation', 1000)
Clothing_category = Category('Clothing', 1000)
Food_category = Category('Food', 1000)
Car_category = Category('Car Expenses', 1000)

print(Vacation_category.deposit(250))
print(Vacation_category.withdraw(200))
print(Vacation_category.check_balance(100))
print(Food_category.transfer(200))
