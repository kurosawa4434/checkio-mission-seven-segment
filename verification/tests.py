"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
from random import choices, randint
from my_solution import seven_segment

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

all_seg = set('abcdefgABCDEFG')


def make_test(num):

    def making():
        while True:
            left = list(SEGMENTS[randint(0, 9)])
            left_lit = ''.join(set(choices(left, k=len(left))))

            right = list(SEGMENTS[randint(0, 9)])
            right_lit = ''.join(set(choices(right, k=len(right)))).upper()
            lit_seg = list(left_lit + right_lit)

            broken = list(all_seg - set(left_lit + right_lit))
            broken_seg = list(set(choices(broken, k=len(broken)*2)))

            answer = seven_segment(set(lit_seg), set(broken_seg))
            if answer:
                return {'input': [lit_seg, broken_seg], 'answer': answer}
            
    return [making() for _ in range(num)]


TESTS = {
    "Basics": [
        {
            "input": [['B', 'C', 'b', 'c'],
                ['A']],
            "answer": 2,
        },
        {
            "input": [['B', 'C', 'a', 'f', 'g', 'c', 'd'],
                ['A', 'G', 'D', 'e']],
            "answer": 6,
        },
        {
            "input": [['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'],
                ['G', 'g']],
            "answer": 4,
        },
        {
            "input": [['B', 'C', 'a', 'f', 'g', 'c', 'd'],
                ['A', 'G', 'D', 'F', 'b', 'e']],
            "answer": 20,
        },
        {
            "input": [['A', 'B', 'C', 'b', 'c', 'f', 'g'],
                ['G', 'd']],
            "answer": 1,
        },
        {
            "input": [[],
                ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'a', 'b', 'c', 'd', 'e', 'f', 'g']],
            "answer": 100,
        },
    ],
    "Randoms": make_test(10),
    
}
