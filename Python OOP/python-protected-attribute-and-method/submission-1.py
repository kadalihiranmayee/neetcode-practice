class Account:
    def __init__(self, title: str, balance: float):
        self._title = title    
        self._balance = balance
        
    def get_title(self) -> str: #pub method
        return self._name
    
    def display_balance(self) -> None: #pub method
        print(f'Balance: ${self._balance}')


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
