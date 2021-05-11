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
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Sorry we dont sell {0} '.format(self.message)
        else:
            return 'Sorry, InvalidItemType'


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
