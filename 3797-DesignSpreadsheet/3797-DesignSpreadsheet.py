# Last updated: 02/03/2026, 13:56:08
class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        op1, op2 = formula[1:].split('+')
        if op1.isnumeric():
            op1 = int(op1)
        else:
            op1 = self.cells.get(op1, 0)
        if op2.isnumeric():
            op2 = int(op2)
        else:
            op2 = self.cells.get(op2, 0)
        return op1 + op2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)