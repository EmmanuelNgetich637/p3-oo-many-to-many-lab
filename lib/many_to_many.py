class Author:
    def __init__(self, name):
        self.name = name

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def books(self):
        return [contract.book for contract in self.contracts()]

    def contracts(self):
        return [c for c in Contract.all_contracts if c.author == self]

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [c for c in Contract.all_contracts if c.book == self]

    def authors(self):
        return [c.author for c in Contract.all_contracts if c.book == self]


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]


# Sample test function to show how to reset before testing
def test_contract_contracts_by_date():
    # Reset the class-level contracts list before creating new contracts
    Contract.all_contracts = []

    author1 = Author("Name 1")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    author2 = Author("Name 2")
    book4 = Book("Title 4")

    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

    # This should return only contracts with date '01/01/2001'
    result = Contract.contracts_by_date('01/01/2001')
    expected = [contract2, contract4]

    assert result == expected, f"Expected {expected}, but got {result}"


# Uncomment below to run the test manually
# test_contract_contracts_by_date()
