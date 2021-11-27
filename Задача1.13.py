#13.Напишите функцию Python, которая печатает первые n строк треугольника Паскаля.  
a = int(input())

def PrintPasTriangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0]+row, row+[0])]
        
PrintPasTriangle(a)