from db.ForeignKey import ForeignKey
from db.SQLiteDatabase import SQLiteDatabase


def prepare() -> SQLiteDatabase:
    sqlite = SQLiteDatabase(dataSource='./db/db.sqlite')

    """
    sqlite.drop(instanceType='TABLE', instanceName='Пользователи')
    sqlite.drop(instanceType='TABLE', instanceName='Паспорта')
    sqlite.drop(instanceType='TABLE', instanceName='Работники')
    """

    sqlite.create(
        instanceType='table',
        instanceName='Пользователи',
        columns={
            'Код': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'Логин': 'VARCHAR(20)',
            'Пароль': 'VARCHAR(60)'
        }
    )

    sqlite.execSQL('CREATE UNIQUE INDEX IF NOT EXISTS УникальныеДанныеПользователя ON Пользователи(Логин, Пароль)')

    sqlite.create(
        instanceType='table',
        instanceName='Паспорта',
        columns={
            'Код': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'Серия': 'TEXT',
            'Номер': 'TEXT',
            'ФИО': 'TEXT',
            'Пол': 'TEXT CHECK (Пол IN (\'Мужской\', \'Женский\'))',
            'ДатаРождения': 'DATETIME',
            'МестоРождения': 'TEXT',
        }
    )

    sqlite.execSQL('CREATE UNIQUE INDEX IF NOT EXISTS УникальныеДанныеПаспорта ON Паспорта(Серия, Номер)')

    sqlite.create(
        instanceType='table',
        instanceName='Работники',
        columns={
            'Код': 'INTEGER PRIMARY KEY AUTOINCREMENT',
            'Образование':
                '''
    TEXT CHECK (Образование IN (
       \'Дошкольное\',
       \'Начальное\',
       \'Основное\',
       \'Среднее общее\',
       \'Среднее профессиональное\',
       \'Высшее\'
    ))''',
            'Должность': 'TEXT NOT NULL',
            'Профессия': 'TEXT NOT NULL',
            'Подразделение': 'INTEGER NOT NULL',
            'ДатаПоступленияНаРаботу': 'DATETIME',
            'Оклад': 'DECIMAL(10,2)',
            'ПаспортныеДанные': 'INTEGER NOT NULL'
        },
        foreignKeys=[
            ForeignKey(column='ПаспортныеДанные', referenceTable='Паспорта', referenceColumn='Код')
        ]
    )

    sqlite.commit()
    return sqlite
