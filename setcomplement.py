from collections import MutableSet


class SetComplement(MutableSet):
    def __init__(self, s):
        self.set = set(s)

    def __contains__(self, e):
        return e not in self.set

    def __iter__(self):
        raise NotImplementedError('figure out how to iterate over everything not in the self.set')

    def __len__(self):
        '''if self.set is not infinite (Python limitation), perhaps we always are?'''
        return float('inf') # raises an overflow error on attempt to convert to intq

    def add(self, e):
        self.set.discard(e)

    def discard(self, e):
        self.set.add(e)

    def __repr__(self):
        return 'SetComplement({0})'.format(repr(self.set))


def main():
    s = set('abc')
    sc = SetComplement(s)
    print sc
    sc.add('c')
    print sc
    sc.discard('c')
    print sc


if __name__ == '__main__':
    main()
