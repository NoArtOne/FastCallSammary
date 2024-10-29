class User:
    def __init__(self, username: str, password: str):
        self.username = username 
        self.__password_hash = password
        self.balance = 10000 #в копейках, будем просто делить 
        #на 100, чтобы не потерять их при подсчете 
        #плавающих точек
        self.transaction_history = [] #todo улучшить и реализовать 
        # отдельным классом для работы с историей пользователей

    def register(self, username, __password_hash):
        #todo хеширование пароля md265 и записать в бд
        pass

    def login(self, username, __password_hash):
        #todo хеширование пароля md265
        #
        pass

    def recover_password(self, username: str):
        #todo logic sent email service
        pass

    def check_balance(self) -> int:
        return self.balance/100 # потому что у нас копейки

    def top_up_balance(self, amount: int): #пользователь указывает сумму в рублях + копейки, мы сохраняем онли в копейках
        # реализовать на frontend метод получения из рублей копеек
        self.balance += amount
        self.transaction_history.append(f'{amount}') #todo
    
    def balance_consumption(self, amount: int):
        if self.balance > amount and self.balance != 0:
            self.balance -= amount
            self.transaction_history.append(f"{-1*amount}") #todo получение номера 
        else:
            return f"{Some_sorry_text}" #todo
        