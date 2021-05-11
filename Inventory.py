import Exeptions


class Inventory(dict):
    len = 0

    def purchase(self, inputItem):

        if inputItem.type not in self.keys():
            raise Exeptions.InvalidItemType(inputItem.type)

        if inputItem not in self.get(inputItem.type):
            raise Exeptions.OutOfStock

        inputItem.lock()
        self.get(inputItem.type).remove(inputItem)
        inputItem.unlock()
        self.len -= 1
        return self.len

    def addItem(self, inputItem):
        if inputItem.type in self.keys():
            self[inputItem.type].append(inputItem)
        else:
            self[inputItem.type] = [inputItem]
        self.len += 1
