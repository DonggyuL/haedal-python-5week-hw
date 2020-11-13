import csv

with open("lecture.csv", 'w', newline='') as lecture:
    wr = csv.writer(lecture)
    wr.writerow(['강의 코드', '강의명', '교수님', '학점'])

for i in range(7):
    lecture_code = input("강의 코드: ")
    lecture_name = input("강의명: ")
    prof_name = input("교수님 성함: ")
    credit = input("학점[2학점/3학점]: ")

    with open("lecture.csv", 'a', newline='') as lecture:
        wr = csv.writer(lecture)
        wr.writerow([lecture_code, lecture_name, prof_name, credit])
