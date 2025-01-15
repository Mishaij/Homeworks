class MyList:
    def __init__(self, *args):
        self.l = list(args)

    def repr(self):
        return repr(self.l)

    def len(self):
        return len(self.l)

    def getitem(self, index):
        return self.l[index]

    def setitem(self, index, value):
        self.l[index] = value

    def Del(self, index):
        return self.l[index]

    def iter(self):
        return iter(self.l)

    def contains(self, item):
        return item in self.l

    def append(self, item):
        self.l.append(item)

    def extend(self, iterable):
        self.l.extend(iterable)

    def insert(self, index, item):
        self.l.insert(index, item)

    def remove(self, item):
        self.l.remove(item)

    def pop(self, index=-1):
        return self.l.pop(index)

    def clear(self):
        self.l.clear()

    def index(self, item, start=0, end=None):
        return self.l.index(item, start, end)

    def count(self, item):
        return self.l.count(item)

    def sort(self, *, key=None, reverse=False):
        self.l.sort(key=key, reverse=reverse)

    def reverse(self):
        self.l.reverse()

    def copy(self):
        return MyList(*self.l)

    def add(self, other):
        if isinstance(other, MyList):
            return MyList(*(self.l + other.l))
        elif isinstance(other, list):
            return MyList(*(self.l + other))
        else:
            raise TypeError("Can only concatenate MyList (or list) to MyList")