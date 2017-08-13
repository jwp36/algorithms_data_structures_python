import sys
sys.path.insert(0, '..')

from LinearDataStructures import Stack

class TowersOfHanoi:
    def __init__(self, numDisks):
        self.leftStack = Stack.Stack()
        self.midStack = Stack.Stack()
        self.rightStack = Stack.Stack()

        for diskNumber in reversed(range(numDisks)):
            #Add 1 to make 1's base`
            self.leftStack.push(diskNumber + 1)

    def move_tower(self, fromStack, withStack, toStack, height):
        if height == 1:
            self.move_disk(fromStack, toStack)
        else:
            self.move_tower(fromStack, toStack, withStack, height - 1)
            self.move_disk(fromStack, toStack)
            self.move_tower(withStack, fromStack, toStack, height - 1)

    def move_disk(self, fromStack, toStack):
        disk_num = fromStack.peek()
        print("Moving disk number: %d" % disk_num)
        toStack.push(fromStack.pop())


if __name__ == "__main__":
    numDisks = 3
    towersOfHanoi = TowersOfHanoi(numDisks)
    towersOfHanoi.move_tower(towersOfHanoi.leftStack, towersOfHanoi.midStack, towersOfHanoi.rightStack, numDisks)


