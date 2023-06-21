test_cases = {
    "taskOne":[
        {
            "input": ["python 2023"],
            "expected": 4
        },
        {
            "input": ["code python 3.10"],
            "expected": 3
        },
        {
            "input": ["python"],
            "expected": 0
        },
    ],
    "taskTwo":[
        {
            "input": ["python 2023"],
            "expected": 6
        },
        {
            "input": ["code python 3.10"],
            "expected": 10
        },
        {
            "input": ["1324#@$%#@"],
            "expected": 0
        },
    ],
    "taskThree":[
        {
            "input": ["#hashtag@$"],
            "expected": 3
        },
        {
            "input": ["code# 1"],
            "expected": 1
        },
        {
            "input": ["python 2023"],
            "expected": 0
        },
    ],
    "taskFour":[
        {
            "input": ["CODEACADEMY"],
            "expected": 11
        },
        {
            "input": ["code python 3.10"],
            "expected": 0
        },
        {
            "input": ["CHat gpt-3"],
            "expected": 2
        },
    ],
    "taskFive":[
        {
            "input": ["CodeAcademy"],
            "expected": 9
        },
        {
            "input": ["code python 3.10"],
            "expected": 10
        },
        {
        "input": ["POSTMAN"],
            "expected": 0
        },
    ],
    "taskSix":[
        {
            "input": ["CodeAcademy"],
            "expected": 6
        },
        {
            "input": ["!@#rty123qas"],
            "expected": 5
        },
        {
            "input": ["POSTMAN"],
            "expected": 5
        },
    ],
    "taskSeven":[
        {
            "input": ["1234567898"],
            "expected": 5
        },
        {
            "input": ["!@#r44ty123qas"],
            "expected": 3
        },
        {
            "input": ["POSTMAN"],
            "expected": 0
        },
    ],

    "taskEight":[
        {
            "input": ["1234567898"],
            "expected": 5
        },
        {
            "input": ["!@#r44ty123qasOO"],
            "expected": 2
        },
        {
            "input": ["OOOOO#@$%#@"],
            "expected": 0
        },
    ],
    "taskNine":[
        {
            "input": ["987654"],
            "expected": 39
        },
        {
            "input": ["!@#r44ty123qasOO"],
            "expected": 14
        },
        {
            "input": ["OOOOO#@$%#@"],
            "expected": 0
        },
    ],
    "taskTen":[
        {
            "input": ["589765"],
            "expected": 26
        },
        {
            "input": ["98421"],
            "expected": 10
        },
        {
            "input": ["OOOOO#@$%#@"],
            "expected": 0
        },
    ],
}