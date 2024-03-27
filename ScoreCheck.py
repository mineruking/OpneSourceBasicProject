'''
Made by Mineru
2024/03/20
Score Program
'''
import math

stuIDlist = []
namelist = []
scoreOfEng = []
scoreOfC = []
scoreOfPy = []
subject = ["영어", "C언어", "파이썬"]
scorelist = []
sumscore = []
def find_rank(arr, arr2, name):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                arr2[j], arr[j+1] = arr[j+1], arr[j]
    rank = 1
    for n in arr2:
        if n == name:
            return rank
        rank += 1


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

def getinfo(i):
    print(i + 1, "번째 학생 이름을 입력하시오:")
    name = input()
    print(i + 1, "번쨰 학생의 학번을 입력하시오:")
    stuID = input()

    for j in subject:
        print(name, "학생의", j, "성적을 입력하시오:")
        temp = int(input())
        if j == "영어":
            eng = temp
        elif j == "C언어":
            clang = temp
        else:
            py = temp
    return name, stuID, eng, clang, py

def avgScore(*score):
    sumOfScore = sum(score)
    avgOfScore = sumOfScore / len(score)
    return sumOfScore, avgOfScore

def print_score(names):
    print("                              성적관리 프로그램         ")
    print(" =============================================================================")
    print(" 학번          이름    영어      C-언어      파이썬         총점       평균         학점          등수   ")
    print(" =============================================================================")
    k = 0
    for i in names:
        print(stuIDlist[k],"    ", i,"    ",scoreOfEng[k],"     ",scoreOfC[k], "     ", scoreOfPy[k],"      ",sumscore[k],"       ",scorelist[k],"        ",find_score(scorelist[k]),"     ", find_rank(scorelist, names, i))
        k += 1


for i in range(5):
    name, stuID, eng, clang, py = getinfo(i)
    namelist.append(name)
    stuIDlist.append(stuID)
    scoreOfEng.append(eng)
    scoreOfC.append(clang)
    scoreOfPy.append(py)
    sumres, avgres = avgScore(scoreOfEng[i], scoreOfC[i],scoreOfPy[i])
    sumscore.append(sumres)
    scorelist.append(avgres)
5
print_score(namelist)