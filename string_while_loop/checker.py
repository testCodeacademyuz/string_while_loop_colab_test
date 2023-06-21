import requests

class CheckSolution:
    def __init__(self, task_name):
        """
        This class is used to check and send results to server.

        Args:
            task_name (str): Task name from server.
        """
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        """
        This method is used to send results to server.

        Args:
            tg_username (str): Telegram username.
            isSolved (bool): True if solved, False if not solved.
            homework_name (str): Homework name from server.
        """
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        # print(data)
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        if response.status_code == 404:
            print("❗️ Siz kursga ro'yxatga olinmagansiz!")
        elif response.status_code == 201:
            print("❕ Sizning javobingiz muvafaqqiyatli yuborildi!")
        else:
            print("Sizda noma'lum xatolik yuz berdi!")