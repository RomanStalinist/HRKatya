class User:
    def __init__(self, id: int, login: str, password: str):
        self.id = id
        self.login = login
        self.password = password

    def __repr__(self):
        return str({
            'Код': self.id,
            'Логин': self.login,
            'Пароль': self.password
        })
