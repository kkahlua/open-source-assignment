import copy
student1 = [0,0,0,0,0,0,0,0,'Q+']
student2 = [0,0,0,0,0,0,0,0,'Q+']
student3 = [0,0,0,0,0,0,0,0,'Q+']
student4 = [0,0,0,0,0,0,0,0,'Q+']
student5 = [0,0,0,0,0,0,0,0,'Q+']
all_list=[student1,student2,student3,student4,student5]
length=5


def print_menu():
    print("1. 데이터 추가\n2. 데이터검색\n3. 데이터삭제\n4. 데이터 정렬\n0. 프로그램종료\n")


def cin_data(lst):
    print("학과:")
    lst[0] = input()
    print("\n학번:")
    lst[1] = input()
    print("\n이름:")
    lst[2] = input()
    print("\n국어:")
    lst[3] = (int(input()))
    print("\n영어:")
    lst[4] = (int(input()))
    print("\n수학:")
    lst[5] = (int(input()))
    lst[6] = (lst[3]+lst[4]+lst[5])
    lst[7] = (lst[6] / 3)
    calc_hakjum(lst)


def print_data(lst):
    print("학과 : %s" % lst[0])
    print("학번 : %s" % lst[1])
    print("이름 : %s" % lst[2])
    print("국어 : %d" % lst[3])
    print("영어 : %d" % lst[4])
    print("수학 : %d" % lst[5])
    print("총점 : %d" % lst[6])
    print("평균 : %d" % lst[7])
    print("종합학점 : %s" % lst[8])


def calc_hakjum(lst):
    if lst[7] // 10 == 10:
        lst[8] = "A+"
    elif lst[7] // 10 == 9:
        if lst[7] % 10 >= 5:
            lst[8] = "A+"
        else:
            lst[8] = "A0"
    elif lst[7] // 10 == 8:
        if lst[7] % 10 >= 5:
            lst[8] = "B+"
        else:
            lst[8] = "B0"
    elif lst[7] // 10 == 7:
        if lst[7] % 10 >= 5:
            lst[8] = "C+"
        else:
            lst[8] = "C0"
    elif lst[7] // 10 == 6:
        if lst[7] % 10 >= 5:
            lst[8] = "D+"
    else:
        lst[8] = "F"


def check_data():
    count = 0
    print("학번 또는 이름을 입력하세요: ")
    find = input()
    if find.isdigit():
        int(find)
    for i in range(length):
        if count!=0:
            break
        for j in range(1, 3):
            if find == all_list[i][j]:
                print_data(all_list[i])
                count+=1
                break
    if count == 0:
        print("검색한 학생을 찾지 못했습니다.")


while True:
    print_menu()
    check = int(input("사용할 기능의 번호를 입력하세요 : "))
    if check == 0:
        break
    if check == 1:
        cin_data(student1)
        cin_data(student2)
        cin_data(student3)
        cin_data(student4)
        cin_data(student5)
    if check == 2:
        check_data()
    if check == 3:
        data = input("삭제 할 학생의 학번 또는 이름을 입력하세요: ")
        swich=0
        for i in range(length):
            for j in range(1, 3):
                if all_list[i][j] == data:
                    if i == length-1:
                        all_list[length-1].clear()
                        swich+=1
                        break
                    else:
                        while i<length-1:
                            all_list[i]=copy.deepcopy(all_list[i+1])
                            i+=1
                        all_list[length-1].clear()
                        swich+=1
                        break
            if swich!=0:
                length-=1
                break
    if check == 4:
        for i in range(length):
            for j in range(3, 6):

                str(all_list[i][j])
        print("학번으로 정렬")
        num_list = sorted(all_list[:length], key= lambda number: number[1])
        print(num_list)
        print("학과로 정렬")
        name_list = sorted(all_list[:length], key= lambda number: number[0])
        print(name_list)

