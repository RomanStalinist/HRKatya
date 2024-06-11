class ForeignKey:
    def __init__(self, column: str, referenceTable: str, referenceColumn: str, onUpdate='CASCADE', onDelete='RESTRICT'):
        self.column = column
        self.referenceTable = referenceTable
        self.referenceColumn = referenceColumn
        self.onUpdate = onUpdate
        self.onDelete = onDelete

    def buildQuery(self):
        return f'''
    FOREIGN KEY ({self.column})
    REFERENCES {self.referenceTable} ({self.referenceColumn})
    ON UPDATE {self.onUpdate}
    ON DELETE {self.onDelete}
    '''
