class User:
    def __init__(self, username: str, password: str):
        self.username = username 
        self.__password_hash = password
        self.balance = 10000 #� ��������, ����� ������ ������ 
        #�� 100, ����� �� �������� �� ��� �������� 
        #��������� �����
        self.transaction_history = [] #todo �������� � ����������� 
        # ��������� ������� ��� ������ � �������� �������������

    def register(self, username, __password_hash):
        #todo ����������� ������ md265 � �������� � ��
        pass

    def login(self, username, __password_hash):
        #todo ����������� ������ md265
        #
        pass

    def recover_password(self, username: str):
        #todo logic sent email service
        pass

    def check_balance(self) -> int:
        return self.balance/100 # ������ ��� � ��� �������

    def top_up_balance(self, amount: int): #������������ ��������� ����� � ������ + �������, �� ��������� ���� � ��������
        # ����������� �� frontend ����� ��������� �� ������ ������
        self.balance += amount
        self.transaction_history.append(f'{amount}') #todo
    
    def balance_consumption(self, amount: int):
        if self.balance > amount and self.balance != 0:
            self.balance -= amount
            self.transaction_history.append(f"{-1*amount}") #todo ��������� ������ 
        else:
            return f"{Some_sorry_text}" #todo
        