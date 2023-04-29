# Создание пользовательских исключений
class MyCustomException(BaseException):
    pass

class MyOtherException(BaseException):
    pass

class MyThirdException(BaseException):
    pass

# Класс, который хранит баланс и обрабатывает платежи
class PaymentProcessor:
    def __init__(self):
        self.balance = 0

    def add_funds(self, amount):
        # Проверка на отрицательный баланс и выброс исключения, если значение отрицательное
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.balance += amount

    def make_payment(self, amount):
        # Проверка на положительное значение платежа и выброс исключения, если значение меньше или равно 0
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        # Проверка наличия достаточных средств и выброс исключения, если средств недостаточно
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Класс, который представляет пользователя и его свойства
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Класс, который управляет пользователями
class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        try:
            # Проверка, что добавляемый пользователь является экземпляром класса User и выброс исключения, если это не так
            if not isinstance(user, User):
                raise TypeError("user should be an instance of User class")
            # Проверка наличия пользователя с таким же именем и выброс исключения, если пользователь существует
            if user.username in self.users:
                raise ValueError("User with this username already exists")
            self.users[user.username] = user
        except (TypeError, ValueError) as e:
            # Вывод ошибки в консоль, если она произошла при добавлении пользователя
            print(f"Error adding user: {e}")

    def get_user(self, username):
        try:
            # Проверка наличия пользователя с заданным именем и выброс исключения, если пользователь не существует
            if username not in self.users:
                raise ValueError("User with this username does not exist")
            return self.users[username]
        except ValueError as e:
            # Вывод ошибки в консоль, если она произошла при получении пользователя
            print(f"Error getting user: {e}")

    def remove_user(self, username):
        try:
            # Проверка наличия пользователя с заданным именем и выброс исключения, если пользователь не существует
            if username not in self.users:
                raise ValueError("User with this username does not exist")
            # Удаление пользователя из списка пользователей
            del self.users[username]
            # Если есть `ValueError`, вывести сообщение об ошибке с конкретным исключением
        except ValueError as e:
            print(f"Error removing user: {e}")
