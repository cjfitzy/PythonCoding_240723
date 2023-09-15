class Budget:
    def __init__(self,item,balance):
        self.item = item
        self.balance = balance


    def depost(self,amount):
        self.balance += amount
        return"Deposited amount"

    def withdraw(self, amount):
        self.balance -= amount
        return"withdrew amount"

    def transfer(self,amount,targetitem):
        self.balance -= amount
        targetitem.balance += amount
        return"transfered amount"
        



food = Budget("Food",300)
clothing = Budget("Clothing",300)

print(food.balance)
print(clothing.balance)

food.transfer(100,clothing)
print(food.balance)
print(clothing.balance)
food.depost(1000)
print(food.balance)
food.withdraw(100)
print(food.balance)

print(food.item,food.balance)
print(clothing.item,clothing.balance)