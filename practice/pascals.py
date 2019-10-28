def pascal_triangle(n):
    """
    Print and do Pascal's Triangle in O(n^2) time complexity.
    """
    for line in range(1, n+1):
        C = 1

        for i in range(1, line + 1): 
            print(C, end=" ")
            C = int(C * (line - i) / i)
        print("")

pascal_triangle(5)
