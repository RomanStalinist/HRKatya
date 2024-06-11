class Passport:
    def __init__(self, id: int, seria: str, number: str, fullname: str, sex: str, dob, pob: str):
        self.id = id
        self.seria = seria
        self.number = number
        self.fullname = fullname
        self.sex = sex
        self.dob = dob
        self.pob = pob

    def __repr__(self):
        return str({
            'Код': self.id,
            'Серия': self.seria,
            'Номер': self.number,
            'ФИО': self.fullname,
            'Пол': self.sex,
            'ДатаРождения': self.dob,
            'МестоРождения': self.pob
        })
