# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44 * 1024 * 1024
book_size = 100 * 50 * 25 * 4
num_books = disk_size // book_size
print("Количество книг, помещающихся на дискету:", int(num_books))
