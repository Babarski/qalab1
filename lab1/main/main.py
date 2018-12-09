from . import MySorter

if __name__ == "__main__":
    sorter = MySorter()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    res = sorter.sort(matrix)

    i = 1
    print(type(i))

    print("Input matrix")
    for row in matrix:
        print(row)

    print("Result")
    for row in res:
        print(row)