#4
def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance


def deposit(self, amount):
    self.balance += amount
    return f"Успішно внесено {amount} грн"


def withdraw(self, amount):
    if amount > self.balance:
        return "Недостатньо коштів на рахунку"
    else:
        self.balance -= amount
        return f"Успішно знято {amount} грн"


def get_balance(self):
    return f"Поточний  баланс: {self.balance} грн"