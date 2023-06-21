from string_while_loop import CheckSolution
from string_while_loop import test_cases

class TestCaseRunner(CheckSolution):
    def __init__(self, task_name, homework_name, task):
        """
        This class is used to run test cases.

        Args:
            task_name (str): Task name(Example: task01)
            homework_name (str): Homework name(Example: SlicingHomework)
            task (str): Test case name(Example: taskOne)
        """
        self.homework_name = homework_name
        self.task = task
        super().__init__(task_name)
    
    def test_cases_runner(self, solution):
        """
        This method is used to run test cases.

        Args:
            solution (function): Student's solution function
        
        Returns:
            list: List of dictionaries
        """
        results = []
        for test_case in test_cases[self.task]:
            try:
                inputs = tuple(test_case["input"])
                answer = solution(*inputs) 
            except:
                answer = "None"
            excepted = test_case["expected"]

            result = {
                "input": map(str, test_case["input"]),
                "answer": answer,
                "expected": excepted,
                "isSolved": answer == excepted
            }
            results.append(result)
        return results
    
    def check(self, solution, tg_username):
        """
        This method is used to check student's solution.

        Args:
            solution (function): Student's solution function
            tg_username (str): Telegram username
        """
        results = self.test_cases_runner(solution)
        isSolved = all([result["isSolved"] for result in results])
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(results, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

task = [
    "taskOne",
    "taskTwo",
    "taskThree",
    "taskFour",
    "taskFive",
    "taskSix",
    "taskSeven",
    "taskEight",
    "taskNine",
    "taskTen",]

q1 = TestCaseRunner(task_name="strWhile01", homework_name="string_while_loop", task=task[0])
q2 = TestCaseRunner(task_name="strWhile02", homework_name="string_while_loop", task=task[1])
q3 = TestCaseRunner(task_name="strWhile03", homework_name="string_while_loop", task=task[2])
q4 = TestCaseRunner(task_name="strWhile04", homework_name="string_while_loop", task=task[3])
q5 = TestCaseRunner(task_name="strWhile05", homework_name="string_while_loop", task=task[4])
q6 = TestCaseRunner(task_name="strWhile06", homework_name="string_while_loop", task=task[5])
q7 = TestCaseRunner(task_name="strWhile07", homework_name="string_while_loop", task=task[6])
q8 = TestCaseRunner(task_name="strWhile08", homework_name="string_while_loop", task=task[7])
q9 = TestCaseRunner(task_name="strWhile09", homework_name="string_while_loop", task=task[8])
q10 = TestCaseRunner(task_name="strWhile10", homework_name="string_while_loop", task=task[9])