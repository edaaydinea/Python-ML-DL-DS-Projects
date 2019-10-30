import getpass


class Daily_planner(object):
    def __init__(self):
        self.username = "ryan"
        self.password = "ysk%123"
        self.check_here()
        self.day_planner()

    def check_here(self):
        input_username = input("Enter username:").lower()
        input_password = getpass.getpass("Enter your password:")

        if self.username == input_username and self.password == input_password:
            print("Access granted, Welcome to the system!")

            time_h_now = float(input("What's the time now? Please use 24h format [8:00 AM and 3:00 PM] [8:00 - 15:00]"))
            self.day_planner(time_h_now)

        else:
            print("Username or password is not correct, access denied")

    def day_planner(time_h_now):
        daily_task = {10: "Programming Lecture, Room A",
                      12: "Computer Vision Lecture, Room C",
                      13: "Lunch Time, Cafetaria!(Fun time)",
                      15: "Group Project Meeting, Room E"}
        for task_time in daily_task.keys():
            if time_h_now <= task_time:
                print("You should attend:", daily_task[task_time])
                break
        my_file = open("Lecture_Notes.txt")
        print(my_file.read())


student = Daily_planner()
