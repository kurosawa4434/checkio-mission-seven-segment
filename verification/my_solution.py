from string import ascii_uppercase, ascii_lowercase

SEGMENTS = [{'a', 'b', 'c', 'd', 'e', 'f'},
            {'b', 'c'},
            {'a', 'b', 'g', 'e', 'd'},
            {'a', 'b', 'g', 'c', 'd'},
            {'b', 'c', 'g', 'f'},
            {'a', 'c', 'd', 'f', 'g'},
            {'a', 'c', 'd', 'e', 'f', 'g'},
            {'a', 'b', 'c'},
            {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
            {'a', 'b', 'c', 'd', 'f', 'g'}]


def seven_segment(lit, broken):

    '''
        /-A-/  /-a-/
       F   B  f   b
      /-G-/  /-g-/
     E   C  e   c
    /-D-/  /-d-/
    '''

    left_seg = set(map(str.lower, set(ascii_uppercase) & lit))
    right_seg = set(ascii_lowercase) & lit
    left_broken = set(map(str.lower, set(ascii_uppercase) & broken))
    right_broken = set(ascii_lowercase) & broken

    d1 = list(filter(lambda s: left_seg <= s <= left_seg | left_broken, SEGMENTS))
    d2 = list(filter(lambda s: right_seg <= s <= right_seg | right_broken, SEGMENTS))
    return len(d1) * len(d2)
