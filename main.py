class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'MyCustomError has been raised'


class OutOfStock(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return format(self.message)
        else:
            return 'Sorry, that item is out of stock'


class InvalidItemType(Exception):
    pass


class LockedItem(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Sorry the item: {0} is locked '.format(self.message)
        else:
            return 'LockedItem has been raised'


class Item:
    def __init__(self, item_type):
        self.type = item_type
        self.isLocked = False
        self.isOnStock = False


class Inventory(list):

    def lock(self, inputItem):
        if inputItem in self:
            if inputItem.isLocked:
                raise LockedItem(inputItem.type)
            inputItem.isLocked = True
        else:
            raise InvalidItemType

    def unlock(self, inputItem):
        if inputItem in self:
            inputItem.isLocked = False

    def purchase(self, inputItem):
        # if inputItem.isLocked:
        #     raise LockedItem(inputItem.type)

        if inputItem not in self:
            raise InvalidItemType(inputItem.type)

        if not inputItem.isOnStock:
            raise OutOfStock

        inputItem.isOnStock = False
        return len(self)

   

item = Item("Phone")
inv = Inventory()
inv.append(item)

inv.lock(item)
# except InvalidItemType:
#     print(f"{item.type} is not in invenory and can not be locked")


numLeft = inv.purchase(item)
# except InvalidItemType:
#     print(f"Sorry we dont sell {item.type}")
# except OutOfStock:
#     print("Sorry the item is out of stock")
# else:
#     print(f"Purchase complete. There are {numLeft} items left")
# finally:
#     inv.unlock(item.type)


