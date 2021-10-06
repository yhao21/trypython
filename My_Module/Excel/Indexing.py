import re

"""
Instruction:

    1. select cells: A1:F5
        cells = CellRange('A1:F5')
    
    2. trans capital letter into numbers:
        number = LetterToNum('B')
        print(number) ------> 2
    
    3. trans number to capital letter:
        letter = NumToLetter('2')
        print(letter) ------> B
    
    4. trans number to lower letter:
        letter = ToLowerLetter('2')
        print(letter) -------> b

"""


def LowerCaseLetter():

    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    lower_case = [i for i in lower_letter]
    return lower_case


def ToLowerLetter(number):
    #trans number to lower case number
    lower_letter = LowerCaseLetter()[number - 1]
    return lower_letter


def Columns():
    #excel row indexing, from A to ZZ
    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper_case = [i for i in upper_letter]
    Columns = []

    for i in range(1,703):
        if i < 27:
            row_index = upper_case[i-1]
            Columns.append(row_index)
        elif i > 26 and i < 703:
            #除法后的整数
            quotient_ = i // 26
            #除法后的余数
            remainder_ = i % 26
            if remainder_ == 0:
                first_letter = upper_case[quotient_ - 2]
                second_letter = upper_case[remainder_ - 1]
                row_index = first_letter + second_letter
                Columns.append(row_index)
            else:
                first_letter = upper_case[quotient_ - 1]
                second_letter = upper_case[remainder_ -  1]
                row_index = first_letter + second_letter
                Columns.append(row_index)
    return Columns


def NumToLetter(number):
    #trans number into letter, from A to ZZ
    Col = Columns()
    letter = Col[number - 1]
    return letter


def LetterToNum(letter):
    #trans letter into number
    #input should be a string
    Col = Columns()
    position = Col.index(letter) + 1
    return position


def CellRange(cell_range):
    #auto trans cells range used in excel

    def output(start_position, end_position, start_row, end_row):

        col_index = Columns()
        cells = []
        for row in range(int(start_row), int(end_row) + 1):
            for col in range(start_position - 1, end_position):
                cell = col_index[col] + str(row)
                cells.append(cell)
        return cells

    start_col = re.compile(r'([A-Z]+)\d+').findall(cell_range)[0]
    start_row = re.compile(r'[A-Z]+(\d+)').findall(cell_range)[0]
    end_col = re.compile(r'([A-Z]+)\d+').findall(cell_range)[1]
    end_row = re.compile(r'[A-Z]+(\d+)').findall(cell_range)[1]
    start_position = LetterToNum(start_col)
    end_position = LetterToNum(end_col)
    rows = [start_row,end_row]
    col_trans = 0

    if start_position > end_position:
        col_trans = start_position
        start_position = end_position
        end_position = col_trans
        start_row = min(rows)
        end_row = max(rows)
        result = output(start_position, end_position, start_row, end_row)

    elif start_position < end_position and start_row > end_row:
        start_row = min(rows)
        end_row = max(rows)
        result = output(start_position, end_position, start_row, end_row)

    elif start_position == end_position and start_row > end_row:
        start_row = min(rows)
        end_row = max(rows)
        result = output(start_position, end_position, start_row, end_row)

    else:
        result = output(start_position, end_position, start_row, end_row)

    return result


if __name__ == '__main__':

    cell = CellRange('C3:A1')
    print(cell)





