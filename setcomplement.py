from collections import MutableSet


class SetComplement(MutableSet):
    
    #def __new__(cls, s):
        #'''TODO: make this make sense for a complement of a complement'''
        #return super(SetComplement, cls).__new__(s)
    
    def __init__(self, s):
        self.set = set(s)

    def __contains__(self, e):
        return e not in self.set

    def __iter__(self):
        '''
        since iteration order is arbitrary, could just iterate over everything in memory
        not in the self.set, then start 
        iterating over a itertools.count(max_int_size_in_memory)
        '''
        raise NotImplementedError('figure out how to iterate over everything not in the self.set')

    def __len__(self):
        '''if self.set is not infinite (Python limitation), perhaps we always are?'''
        # TODO: subclass int and create an `inf` for it. probably just use float('inf') for comparisons
        return float('inf') # raises an overflow error on attempt to convert to int

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
