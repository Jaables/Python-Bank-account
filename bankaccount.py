class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "%s's account. Balance: £%.2f" % (self.name, self.balance)

  def show_balance(self):
    print "Balance: £%.2f" %(self.balance)

  def deposit(self, amount):
    if self.amount <= 0:
      print "Error"
    else:
      print "You are depositing £%.2f" % (self.amount)
      self.balance += amount
      self.show_balance()

  def withdraw(self, amount):
    if self.amount > balance:
      print "Error"
    else: 
      print "You are withdrawing £%.2f" % (self.amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Jamie")

print my_account





