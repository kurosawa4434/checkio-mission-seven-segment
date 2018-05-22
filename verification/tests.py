"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

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
            "input": [['B', 'C', 'a', 'f', 'g', 'c', 'd'],
                ['A', 'G', 'D', 'F', 'b', 'e']],
            "answer": 20,
        },
    ],
}
