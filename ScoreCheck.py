class Student:
    def __init__(self, name, stuID, english, c_language, python):
        self.name = name
        self.stuID = stuID
        self.scores = {'영어': english, 'C언어': c_language, '파이썬': python}
        self.total = sum(self.scores.values())
        self.average = self.total / len(self.scores)
        self.grade = self.find_grade()
        
    def find_grade(self):
        if self.average >= 95:
            return "A+"
        elif self.average >= 90:
            return "A"
        elif self.average >= 85:
            return "B+"
        elif self.average >= 80:
            return "B"
        elif self.average >= 75:
            return "C+"
        elif self.average >= 70:
            return "C"
        elif self.average >= 65:
            return "D+"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        name = input("이름: ")
        stuID = input("학번: ")
        english = int(input(f"{name} 학생의 영어 성적: "))
        c_language = int(input(f"{name} 학생의 C언어 성적: "))
        python = int(input(f"{name} 학생의 파이썬 성적: "))
        self.students.append(Student(name, stuID, english, c_language, python))
        print(f"{name} 학생 정보가 추가되었습니다.")
    
    def delete_student(self, identifier):
        for i, student in enumerate(self.students):
            if student.stuID == identifier or student.name == identifier:
                removed_student = self.students.pop(i)
                print(f"{removed_student.name} 학생의 정보가 삭제되었습니다.")
                return
        print("해당 학생을 찾을 수 없습니다.")
    
    def search_student(self, identifier):
        for student in self.students:
            if student.stuID == identifier or student.name == identifier:
                print(f"학번: {student.stuID}, 이름: {student.name}, 성적: {student.scores}")
                return
        print("해당 학생을 찾을 수 없습니다.")
    
    def sort_students_by_total_score(self):
        self.students.sort(key=lambda student: student.total, reverse=True)
    
    def count_students_above_80(self):
        return len([student for student in self.students if student.average >= 80])
    
    def print_students(self):
        print("성적관리 프로그램")
        print("================================================================================")
        print("학번        이름     영어    C-언어    파이썬    총점    평균    학점")
        print("================================================================================")
        for student in self.students:
            print(f"{student.stuID}    {student.name}    {student.scores['영어']}    {student.scores['C언어']}    {student.scores['파이썬']}    {student.total}    {student.average:.2f}    {student.grade}")
        print("================================================================================")

# 성적 관리 시스템 실행
grade_manager = GradeManager()

# 예시로 학생 5명 추가
for _ in range(5):
    grade_manager.add_student()

# 학생 정보 출력
grade_manager.print_students()

i = 0
while(i != 6):
    print("1. 학생 추가")
    print("2. 학생 삭제")
    print("3. 학생 탐색")
    print("4. 학생 정렬")
    print("5. 80점 이상 탐색")
    print("6. 종료")
    i = int(input("메뉴를 선택하세요: "))

    if i == 1:
        grade_manager.add_student()
    elif i == 2:
        k_info = input("삭제하고 싶은 학번 또는 이름을 입력하시오 :")
        grade_manager.delete_student(k_info)
    elif i == 3:
        k_info = input("검색하고 싶은 학번 또는 이름을 입력하시오 :")
        grade_manager.search_student(k_info)

    elif i == 4:
        grade_manager.sort_students_by_total_score()

    elif i == 5:
        count = grade_manager.count_students_above_80()
        print(f"평균 80점 이상 {count}명")
    elif i == 6:
        break;
    else:
        print("잘못 입력하셨습니다. 다시 입력하시오.")

    grade_manager.print_students()
