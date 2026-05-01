from dataclasses import dataclass, field

class InventoryError(Exception):
    pass


@dataclass
class Item:
    sku: str
    name: str
    price: float
    quantity: int
    tag: str = field(default="NEW", init=False)

    def __post_init__(self):
        if self.price <= 0:
            raise InventoryError(f"Invalid price for SKU:{self.sku}")

    @property
    def total_value(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f"[{self.sku}] {self.name} x {self.quantity} ${self.total_value} ({self.tag})"

    def __lt__(self , other):
        return self.total_value < other.total_value


class StockChecker:
    def __init__(self, items, max_price):
        self.items = items
        self.max_price = max_price
        self.index =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        item = self.items[self.index]
        self.index +=1

        if item.price <= self.max_price:
            item.tag = "STOCKED"
        else:
            item.tag = "REJECTED"

        return item


def stock_report(checker):
    stocked = 0
    rejected = 0

    for item in checker:
        if item.tag == "STOCKED":
            stocked += 1
        else:
            rejected +=1

        yield str(item)

    yield f"Summary: {stocked} stocked, {rejected} rejected"


class WarehouseSession:
    def __init__(self, name):
        self.name = name
        self._items = []

    def __enter__(self):
        print(f"===Opening:{self.name}===")
        return self

    def receive(self, item):
        self._items.append(item)

    def check(self, max_price):
        checker = StockChecker(self._items, max_price)
        return stock_report(checker)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is InventoryError:
            print(f"!!! Error:{exc_val}")
            return True

        print(f"===Closing:{self.name}({len(self._items)} items)===")

with WarehouseSession("Main") as wh:
    wh.receive(Item("A001", "Keyboard", 49.99, 20))
    wh.receive(Item("A002", "Monitor", 599.99, 10))
    wh.receive(Item("A003", "Mouse", 25.0, 8))

    for line in wh.check(500.0):
        print(line)

    print(wh._items[0] < wh._items[1])

print()

with WarehouseSession("Outlet") as wh:
    wh.receive(Item("B001", "Cable", -5.0, 10))
