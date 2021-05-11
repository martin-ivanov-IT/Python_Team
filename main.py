from Inventory import Inventory
import Exeptions
from Item import Item

item = Item("Phone")
item3 = Item("Phone")
item2 = Item("Handy")
inv = Inventory()
inv.addItem(item)

try:
    inv.purchase(item)
except Exeptions.InvalidItemType:
    print(f"sorry we dont sell {item.type}")
except Exeptions.OutOfStock:
    print(f"{item.type} is out of stock")
print(inv.len)
