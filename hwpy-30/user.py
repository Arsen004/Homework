class User:
    def __init__(self, name: str):
        self.__name = name

    @property
    def user(self):
        return {"name": self.__name}

    @user.setter
    def user(self, name: str):
        self.__name = name

    def __str__(self):
        return f"Имя пользователя: {self.__name}"
