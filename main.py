class UsernameAlreadyExistsException(BaseException):
    pass

class UserNotFoundException(BaseException):
    pass

class InvalidUserException(BaseException):
    pass

class PaymentProcessor:
    def __init__(self):
        self.balance = 0
        # Конструктор инициализирует баланс платежного процессора

    def add_funds(self, amount):
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной.")
        self.balance += amount
        # Метод добавляет средства на баланс платежного процессора

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств.")
        self.balance -= amount
        # Метод совершает платеж и уменьшает баланс платежного процессора

    def get_balance(self):
        return self.balance
        # Метод возвращает текущий баланс платежного процессора

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        # Конструктор инициализирует имя пользователя и адрес электронной почты

class UserManager:
    def __init__(self):
        self.users = {}
        # Конструктор инициализирует пустой словарь для хранения пользователей

    def add_user(self, user):
        try:
            if not isinstance(user, User):
                raise InvalidUserException("Пользователь должен быть экземпляром класса User.")
            if user.username in self.users:
                raise UsernameAlreadyExistsException("Пользователь с таким именем уже существует.")
            self.users[user.username] = user
            print("Пользователь успешно добавлен.")
        except (InvalidUserException, UsernameAlreadyExistsException) as e:
            print(f"Ошибка при добавлении пользователя: {e}")
        # Метод добавляет нового пользователя в список пользователей

    def get_user(self, username):
        try:
            if username not in self.users:
                raise UserNotFoundException("Пользователь с таким именем не найден.")
            return self.users[username]
        except UserNotFoundException as e:
            print(f"Ошибка при получении пользователя: {e}")
        # Метод возвращает пользователя по заданному имени пользователя

    def remove_user(self, username):
        try:
            if username not in self.users:
                raise UserNotFoundException("Пользователь с таким именем не найден.")
            del self.users[username]
            print("Пользователь успешно удален.")
        except UserNotFoundException as e:
            print(f"Ошибка при удалении пользователя: {e}")
        # Метод удаляет пользователя по заданному имени пользователя

user_manager = UserManager()

# Создание пользователей
user1 = User("john_doe", "john@example.com")
user2 = User("jane_smith", "jane@example.com")
user3 = User("john_doe", "another_email@example.com")  # Пользователь с уже существующим именем

# Добавление пользователей
user_manager.add_user(user1)
user_manager.add_user(user2)
user_manager.add_user(user3)  # Попытка добавить пользователя с недопустимым именем
