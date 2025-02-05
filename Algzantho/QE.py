def max(matrix, queries, rows, cols):
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows):
        for j in range(cols):
            prefix[i + 1][j + 1] = (
                matrix[i][j]
                + prefix[i][j + 1]
                + prefix[i + 1][j]
                - prefix[i][j]
            )

    def cells(x1, y1, x2, y2):
        return (
            prefix[x2 + 1][y2 + 1]
            - prefix[x1][y2 + 1]
            - prefix[x2 + 1][y1]
            + prefix[x1][y1]
        )

    results = []
    for x, y, k in queries:
        low, high = 0, min(rows, cols) 
        max_side = 0
        while low <= high:
            mid = (low + high) // 2
            x1, y1 = x - mid, y - mid
            x2, y2 = x + mid, y + mid
            if x1 >= 0 and y1 >= 0 and x2 < rows and y2 < cols:
                black_cells = cells(x1, y1, x2, y2)
                if black_cells <= k:
                    max_side = mid
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                high = mid - 1
        results.append((2 * max_side + 1) ** 2)
    return results


r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(q)]
results = max(matrix, queries, r, c)
for res in results:
    print(res)
