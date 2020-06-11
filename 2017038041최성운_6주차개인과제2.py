import threading


class Hap:
    result = 0

    def __init__(self, value):
        self.hapvalue = value

    def multi_hap(self):
        for i in range(1, self.hapvalue+1):
            self.result += i
        print(self.result)


def main():
    hap1 = Hap(1000)
    hap2 = Hap(100000)
    hap3 = Hap(10000000)
    th1 = threading.Thread(target=hap1.multi_hap)
    th2 = threading.Thread(target=hap2.multi_hap)
    th3 = threading.Thread(target=hap3.multi_hap)
    th1.start()
    th2.start()
    th3.start()


if __name__ == "__main__":
    main()
