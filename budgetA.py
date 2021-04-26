#*******OOP programming, budget App*****

class Category:


    def __init__(self, category, amount): 

        self.category = category
        self.amount = amount

   
    def deposit(self, amount):

        amount = input("How much would you like like to deposit in to your {} category: \n".format(self.category)) 
        return"you've successfully deposited {} to your {} category \n".format(amount, self.category)

    def withdraw(self, amount):

        amount = input("How much would you like to deposit to your {} category: \n".format(self.category))
        return "You've successfully withdrawn {} from your {} category".format(amount, self.category)

    def check_balance(self, amount):
        if self.amount > amount:
            return True
        else:
            return False

    def transfer(self, amount, category):
        amount= input("How much would you like to transfer?")

        #take amount from user
        #use withdraw funtion to deduct the amount from source category
        #use deposit function to add amount to desitnation category
        
        #self.amount += amount

        #self.amount -= amount
        #print("You have successfully transfered {} to your {} category").format(amount, self.category)

        pass


Vacation_category = Category('Vacation', 1000)
Clothing_category = Category('Clothing', 1000)
Food_category = Category('Food', 1000)
Car_category = Category('Car Expenses', 1000)


print(Vacation_category.deposit(250))
print(Vacation_category.withdraw(200))
