'''Suppose we want to model a bank account with support for deposit and withdraw operations. One way to
do that is by using global state as shown in the following example.'''
balance = 0
def deposit(amount):
    global balance
    balance += amount
    return balance
def withdraw(amount):
    global balance
    balance -= amount
    return balance
'''The above example is good enough only if we want to have just a single account.
Things start getting complicated
if want to model multiple accounts.
We can solve the problem by making the state local,
probably by using a dictionary to store the state.'''
def make_account():
    return {'balance': 0}
def deposit(account, amount):
    account['balance'] += amount
    return account['balance']
def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']
'''With this it is possible to work with multiple accounts at the same time.'''

a = make_account()
print(a)
b = make_account()
print(b)
print(deposit(a, 100))
print(deposit(b, 50))
print(withdraw(b, 10))
print(withdraw(a, 10))

