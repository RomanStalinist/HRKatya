import os
import pathlib
import sqlite3

from db.ForeignKey import ForeignKey


class SQLiteDatabase:
    def __init__(self, dataSource: str):
        self.dataSource = dataSource
        self.connection = sqlite3.connect(dataSource)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create(self, instanceType: str, instanceName: str, columns: dict = None,
               foreignKeys: list[ForeignKey] = None) -> None:
        if columns is None:
            columns = {}
        if foreignKeys is None:
            foreignKeys = []

        columns_str = ',\n'.join([f'\t{col_name} {col_type}' for col_name, col_type in columns.items()])
        foreign_keys_str = ',\n'.join([fk.buildQuery() for fk in foreignKeys])
        query = f'''
CREATE {instanceType} IF NOT EXISTS {instanceName} (
{columns_str}{(",\n" + foreign_keys_str[:-5]) if foreign_keys_str else ''}
);
'''
        self.execSQL(query)

    def beginTransaction(self) -> None:
        self.execSQL("BEGIN TRANSACTION")

    def beginTransactionNonExclusive(self) -> None:
        self.execSQL("BEGIN IMMEDIATE")

    def delete(self, table: str, whereClause: str, whereArgs: list) -> int:
        return self.execSQL(f"DELETE FROM {table} WHERE {whereClause if whereArgs else "1"};", whereArgs)

    def deleteDatabase(self) -> None:
        os.remove(self.dataSource)

    def drop(self, instanceType: str, instanceName: str) -> None:
        self.execSQL(f"DROP {instanceType} IF EXISTS {instanceName}")

    def commit(self) -> None:
        self.connection.commit()

    def execSQL(self, sql: str, bindArgs: tuple = ()) -> int:
        result = self.cursor.execute(sql, bindArgs)
        return result.rowcount

    def getPageSize(self) -> int:
        result = self.cursor.execute("SELECT page_count * page_size FROM pragma_page_count(), pragma_page_size()")
        return result.fetchone()[0]

    def getPath(self) -> str | None:
        return fr"{pathlib.Path(__file__).parent.resolve()}\{self.dataSource}"

    def insert(self, table: str, values: dict):
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?' for _ in values])
        values_list = list(values.values())

        self.execSQL(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", values_list)
        self.commit()

    def isOpen(self) -> bool:
        return self.connection is not None

    def isReadOnly(self):
        return self.connection.isolation_level is None

    def query(self, table: str, columns: list[str] | str = "*", selection: str = None, selectionArgs: tuple[str] = (),
              groupBy: str = None, having: str = None, orderBy: str = None, limit: str = None):
        query = f"SELECT {(', '.join(columns)) if columns != '*' else columns} FROM {table}"
        if selection:
            query += f" WHERE {selection}"
        if groupBy:
            query += f" GROUP BY {groupBy}"
        if having:
            query += f" HAVING {having}"
        if orderBy:
            query += f" ORDER BY {orderBy}"
        if limit:
            query += f" LIMIT {limit}"

        result = self.cursor.execute(query, selectionArgs)
        return result.fetchall()

    def rawQuery(self, query: str, selectionArgs: list[str] = None):
        result = self.cursor.execute(query, selectionArgs) if selectionArgs else self.cursor.execute(query)
        return result.fetchall()

    def replace(self, table: str, initialValues: dict):
        columns = ', '.join(initialValues.keys())
        placeholders = ', '.join(['?' for _ in initialValues])
        sql = f"REPLACE INTO {table} ({columns}) VALUES ({placeholders})"
        values_list = list(initialValues.values())

        self.execSQL(sql, values_list)
        self.commit()

    def rollback(self):
        self.connection.rollback()
