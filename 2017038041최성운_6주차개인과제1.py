import copy


class GradeProcessing:
    student1 = [0, 0, 0, 0, 0, 0, 0, 0, 'Q+']
    student2 = [0, 0, 0, 0, 0, 0, 0, 0, 'Q+']
    student3 = [0, 0, 0, 0, 0, 0, 0, 0, 'Q+']
    student4 = [0, 0, 0, 0, 0, 0, 0, 0, 'Q+']
    student5 = [0, 0, 0, 0, 0, 0, 0, 0, 'Q+']
    all_list = [student1, student2, student3, student4, student5]

    def __init__(self):
        pass

    def print_menu(self):
        print("1. 데이터 추가\n2. 데이터검색\n3. 데이터삭제\n4. 데이터 정렬\n0. 프로그램종료\n")

    def cin_data(self, lst):
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
        lst[6] = (lst[3] + lst[4] + lst[5])
        lst[7] = (lst[6] / 3)
        self.calc_hakjum(lst)

    def print_data(self, lst):
        print("학과 : %s" % lst[0])
        print("학번 : %s" % lst[1])
        print("이름 : %s" % lst[2])
        print("국어 : %d" % lst[3])
        print("영어 : %d" % lst[4])
        print("수학 : %d" % lst[5])
        print("총점 : %d" % lst[6])
        print("평균 : %d" % lst[7])
        print("종합학점 : %s" % lst[8])

    def calc_hakjum(self, lst):
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

    def check_data(self , len):
        count = 0
        print("학번 또는 이름을 입력하세요: ")
        find = input()
        if find.isdigit():
            int(find)
        for i in range(len):
            if count != 0:
                break
            for j in range(1, 3):
                if find == self.all_list[i][j]:
                    self.print_data(self.all_list[i])
                    count += 1
                    break
        if count == 0:
            print("검색한 학생을 찾지 못했습니다.")

    def serch_student(self, len):
        data = input("삭제 할 학생의 학번 또는 이름을 입력하세요: ")
        swich = 0
        for i in range(len):
            for j in range(1, 3):
                if self.all_list[i][j] == data:
                    if i == len - 1:
                        self.all_list[len - 1].clear()
                        swich += 1
                        break
                    else:
                        while i < len - 1:
                            self.all_list[i] = copy.deepcopy(self.all_list[i + 1])
                            i += 1
                        self.all_list[len - 1].clear()
                        swich += 1
                        break
            if swich != 0:
                len -= 1
                return len

    def sort_data(self, len):
        for i in range(len):
            for j in range(3, 6):
                str(self.all_list[i][j])
        print("학번으로 정렬")
        num_list = sorted(self.all_list[:len], key=lambda number: number[1])
        print(num_list)
        print("학과로 정렬")
        name_list = sorted(self.all_list[:len], key=lambda number: number[0])
        print(name_list)


def main():
    length = 5
    start_processing = GradeProcessing()
    while True:
        start_processing.print_menu()
        check = int(input("사용할 기능의 번호를 입력하세요 : "))
        if check == 0:
            break
        if check == 1:
            start_processing.cin_data(GradeProcessing.student1)
            start_processing.cin_data(GradeProcessing.student2)
            start_processing.cin_data(GradeProcessing.student3)
            start_processing.cin_data(GradeProcessing.student4)
            start_processing.cin_data(GradeProcessing.student5)
        if check == 2:
            start_processing.check_data(length)
        if check == 3:
            length = start_processing.serch_student(length)
        if check == 4:
            start_processing.sort_data(length)


if __name__ == "__main__":
    main()
