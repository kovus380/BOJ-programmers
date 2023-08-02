n, m = map(int, input().split())

books = list(map(int, input().split()))
books.append(0)
books.sort()

zero_index = books.index(0)
left_books = books[:zero_index]
right_books = books[zero_index + 1:][::-1]

answer = 0
for side in [left_books, right_books]:
    answer +=  abs(sum(side[::m])) * 2

answer -= max(abs(books[0]), abs(books[-1]))

print(answer)