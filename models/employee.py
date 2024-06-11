class Employee:
    def __init__(self, id: int, education: str, job: str, profession: str, department: str,
                 enrollment_date: str, salary: float, passport_id: int):
        self.id = id
        self.education = education
        self.job = job
        self.profession = profession
        self.department = department
        self.enrollment_date = enrollment_date
        self.salary = salary
        self.passport_id = passport_id

    def __repr__(self):
        return str({
            'Код': self.id,
            'Образование': self.education,
            'Должность': self.job,
            'Профессия': self.profession,
            'Подразделение': self.department,
            'ДатаПоступленияНаРаботу': self.enrollment_date,
            'Оклад': self.salary,
            'ПаспортныеДанные': self.passport_id
        })
