'''
Made by Mineru
2024/03/20
Score Program
'''

def find_rank(score, scorelist):
    sorted_scores = sorted(scorelist, reverse=True)
    return sorted_scores.index(score) + 1

def find_score(scr):
    if scr >= 95:
        return "A+"
    elif scr >= 90:
        return "A"
    elif scr >= 85:
        return "B+"
    elif scr >= 80:
        return "B"
    elif scr >= 75:
        return "C+"
    elif scr >= 70:
        return "C"
    elif scr >= 65:
        return "D+"
    elif scr >= 60:
        return "D"
    else:
        return "F"

def getinfo(num):
    print(f"{num}번째 학생의 정보를 입력해주세요.")
    name = input("이름: ")
    stuID = input("학번: ")
    scores = {}
    for subj in ["영어", "C언어", "파이썬"]:
        scores[subj] = int(input(f"{name} 학생의 {subj} 성적: "))
    return name, stuID, scores

def print_score(student_info):
    print("                              성적관리 프로그램         ")
    print(" =============================================================================")
    print(" 학번          이름    영어      C-언어      파이썬         총점       평균         학점          등수   ")
    print(" =============================================================================")

    scores = [sum(student['scores'].values()) / len(student['scores']) for student in student_info]

    for student in student_info:
        total = sum(student['scores'].values())
        avg = total / len(student['scores'])
        grade = find_score(avg)
        rank = find_rank(avg, scores)
        print(f"{student['stuID']}     {student['name']}    {student['scores']['영어']}     {student['scores']['C언어']}     {student['scores']['파이썬']}      {total}       {avg:.2f}        {grade}     {rank}")

    print("전체 성적 평균 : ", sum(scores) / len(scores))
    print("영어 성적 평균 : ", sum(student['scores']['영어'] for student in student_info) / len(student_info))
    print("C언어 성적 평균: ", sum(student['scores']['C언어'] for student in student_info) / len(student_info))
    print("Python 성적 평균 : ", sum(student['scores']['파이썬'] for student in student_info) / len(student_info))

# 여기서부터 추가된 코드 부분
def insert_student_info(student_info):
    name, stuID, scores = getinfo(len(student_info) + 1)
    student_info.append({'name': name, 'stuID': stuID, 'scores': scores})
    print(f"{name} 학생 정보가 추가되었습니다.")

def delete_student_info(student_info, identifier):
    for i, student in enumerate(student_info):
        if student['stuID'] == identifier or student['name'] == identifier:
            removed_student = student_info.pop(i)
            print(f"{removed_student['name']} 학생의 정보가 삭제되었습니다.")
            return
    print("해당 학생을 찾을 수 없습니다.")

def search_student_info(student_info, identifier):
    for student in student_info:
        if student['stuID'] == identifier or student['name'] == identifier:
            print(f"학번: {student['stuID']}, 이름: {student['name']}, 성적: {student['scores']}")
            return
    print("해당 학생을 찾을 수 없습니다.")

def sort_students_by_total_score(student_info):
    return sorted(student_info, key=lambda x: -sum(x['scores'].values()))

def count_students_above_80(student_info):
    count = 0
    for student in student_info:
        if sum(student['scores'].values()) / len(student['scores']) >= 80:
            count += 1
    return count

student_info = []

for i in range(5):
    name, stuID, scores = getinfo(i+1)
    student_info.append({'name': name, 'stuID': stuID, 'scores': scores})

print_score(student_info)

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
        insert_student_info(student_info)
    elif i == 2:
        info_del = input("삭제할 학번 혹은 이름을 입력하시오 :")
        delete_student_info(student_info, info_del)
    elif i == 3:
        keyword_info =input("검색하고 싶은 학번 또는 이름을 입력하시오 :")
        search_student_info(student_info, keyword_info)
    elif i == 4:
        sorted_students = sort_students_by_total_score(student_info)
        print_score(sorted_students)
    elif i == 5:
        print(f"80점 이상인 학생 수: {count_students_above_80(student_info)}")
    elif i == 6:
        break;
    else :
        print("잘못 입력하셨습니다. 다시 입력하시오.")