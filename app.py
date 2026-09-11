from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__, template_folder='templates')
#for rank update 

# BankAccount class
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"Deposit: ₹{amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"Withdraw: ₹{amount}")
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.transactions

# Dummy Account (No login system)
account = BankAccount("123456", "Ankit Singh", 100000)

# Home  Page
@app.route('/')
def index():
    return render_template("index.html", balance=account.get_balance(), name=account.account_holder)

# Deposit Page
@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amt = float(request.form['amount'])
        account.deposit(amt)
        return redirect(url_for('index'))
    return render_template("deposit.html")

# Withdraw Page
@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amt = float(request.form['amount'])
        account.withdraw(amt)
        return redirect(url_for('index'))
    return render_template("withdraw.html")

# Transaction History
@app.route('/transactions')
def transactions():
    return render_template("transactions.html", transactions=account.get_transactions())

# Run  the Flask app
if __name__ == '__main__':
    app.run(debug=True)
