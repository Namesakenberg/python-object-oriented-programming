class User:
    def __init__(self):
        self.username = ''
        self.password = ''

    def Register(self):
        self.username = input('enter username: ')   
        self.password = input('enter password: ')

    def login(self):
        checkname = input('enter username: ')   
        checkpwd = input('enter password: ')

        if self.username == checkname and self.password == checkpwd:
            print("login successful")
            return True
        else:
            print("incorrect details or not registered")
            return False


class Student(User):
    def __init__(self):
        super().__init__()
        self.course = {}

    def enroll(self):
        course_temp = input('enter the course name: ')
        if course_temp not in self.course:
            self.course[course_temp] = -1
            print(f'enrolled in {course_temp}')
        else:
            print('already enrolled')

    def rate(self):
        course_check = input('enter the course to rate: ')
        if course_check in self.course and self.course[course_check] == -1:
            rating = int(input('enter rating (0–5): '))
            if 0 <= rating <= 5:
                self.course[course_check] = rating
                print('rated successfully')
            else:
                print('invalid rating')
        else:
            print('cannot rate')

    def get_rating(self):
        return f"ratings: {self.course}"


sid = Student()
sid.Register()

if sid.login():
    sid.enroll()
    sid.rate()
    print(sid.get_rating())
