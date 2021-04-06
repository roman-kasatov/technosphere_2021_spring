class CustomList(list):
    def __add__(self, other):
        res = [0] * max(len(self), len(other))
        for pos in range(len(self)):
            res[pos] += self[pos]
        for pos in range(len(other)):
            res[pos] += other[pos]
        return CustomList(res)

    def __sub__(self, other):
        res = [0] * max(len(self), len(other))
        for pos in range(len(self)):
            res[pos] += self[pos]
        for pos in range(len(other)):
            res[pos] -= other[pos]
        return CustomList(res)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        res = [0] * max(len(self), len(other))
        for pos in range(len(self)):
            res[pos] -= self[pos]
        for pos in range(len(other)):
            res[pos] += other[pos]
        return CustomList(res)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)


if __name__ == '__main__':
    b = [3, 2, 1]
    a = CustomList([1, 1, 4])

    print(b == a)
