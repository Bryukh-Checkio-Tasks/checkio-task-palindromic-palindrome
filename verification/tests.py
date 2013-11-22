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
            "input": "asd",
            "answer": False
        },
        {
            "input": "palindrome",
            "answer": False
        },
        {
            "input": "ssssssss",
            "answer": True
        },
        {
            "input": "qwertytrewq",
            "answer": True
        },
        {
            "input": "123456",
            "answer": False
        },
        {
            "input": "hello1olleh",
            "answer": False
        },


    ],
    "Extra": [
        {
            "input": "asd dsa",
            "answer": True
        },
        {
            "input": "000000000000",
            "answer": True
        },
        {
            "input": "master retsm",
            "answer": False
        }
    ]
}
