import Exeptions


class Item:
    def __init__(self, item_type):
        self.type = item_type
        self.isLocked = False

    def lock(self):
        if self.isLocked:
            raise Exeptions.LockedItem(self.type)
        self.isLocked = True

    def unlock(self):
        self.isLocked = False
