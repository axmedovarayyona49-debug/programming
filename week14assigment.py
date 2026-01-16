def make_catalog(books):
    catalog = {}

    for b in books:
        catalog[b[0]] = b[1]  

    return catalog


def check_books(catalog, returned):
    not_returned = set()
    extra_books = set()

    for isbn in catalog:
        if isbn not in returned:
            not_returned.add(isbn)

    for isbn in returned:
        if isbn not in catalog:
            extra_books.add(isbn)

    return not_returned, extra_books


def make_report(catalog, missing):
    result = []

    for isbn in missing:
        result.append("MISSING: " + catalog[isbn] + " (ISBN: " + str(isbn) + ")")

    result.sort()
    return result


borrowed = [
    (1001, "The Great Gatsby", "John"),
    (1002, "1984", "Sarah"),
    (1003, "Python 101", "Mike")
]

returned = [1003, 1001, 9999]

catalog = make_catalog(borrowed)
missing, extra = check_books(catalog, returned)
report = make_report(catalog, missing)

print(missing)
print(extra)
print(report)
