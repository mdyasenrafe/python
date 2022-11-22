class Pair:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def find_pair(self):
        for i in range(len(self.arr)):
            for x in range(len(self.arr)):
                if (self.arr[i] + self.arr[x] == self.target):
                    return i, x


print(Pair([10, 20, 10, 40, 50, 60, 70], 50).find_pair())
