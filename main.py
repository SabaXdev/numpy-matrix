import numpy as np
import pandas as pd

georgian_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა', 'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა', 'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']
georgian_surnames = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია', 'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი', 'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ისტორია', 'ბიოლოგია']

student_names = [(np.random.choice(georgian_names) + ' ' + np.random.choice(georgian_surnames)) for _ in range(100)]

grades = np.random.randint(1, 101, size=(100, len(subjects)))

grades = np.insert(grades.astype(str), 0, student_names, axis=1)


# Task 1: გამოთვალეთ თითოეულ სტუდენტის საშუალო ქულა და ყველაზე მაღალი საშუალო ქულის მქონე სტუდენტი დაბეჭდეთ
def avg_grades():
    print("--------------- დავალება 1 ---------------")
    print("\n")
    avg_grades = np.mean(grades[:, 1:].astype(int), axis=1)
    highest_avg_grade_index = np.argmax(avg_grades)
    print("ყველაზე მაღალი საშუალო ქულის მქონე სტუდენტი:")
    print(grades[highest_avg_grade_index])
    print("\n")


# Task 2: იპოვეთ მათემატიკაში ყველაზე მაღალი და ყველაზე დაბალი ქულის მქონი სტუდენტი და დაბეჭდეთ
def best_and_worst_math_students():
    print("--------------- დავალება 2 ---------------")
    print("\n")
    math_grades = grades[:, 2]
    math_grades_numeric = math_grades.astype(int)

    max_grade = np.max(math_grades_numeric)
    min_grade = np.min(math_grades_numeric)

    highest_math_grade_index = np.where(math_grades_numeric == max_grade)[0]
    lowest_math_grade_index = np.where(math_grades_numeric == min_grade)[0]

    print("ყველაზე მაღალი ქულის მქონე სტუდენტები მათემატიკაში:")
    for idx in highest_math_grade_index:
        # print(f"Student {idx} has a grade of {max_grade} in Math")
        print(f"სტუდენტს, რომლის ID-ია {idx} მათემატიკაში აქვს {max_grade} ქულა")

    print("\nყველაზე დაბალი ქულის მქონე სტუდენტები მათემატიკაში:")
    for idx in lowest_math_grade_index:
        # print(f"Student {idx} has a grade of {min_grade} in Math")
        print(f"სტუდენტს, რომლის ID-ია {idx} მათემატიკაში აქვს {min_grade} ქულა")
    print("\n")


# Task 3: დაბეჭდეთ ყველა სტუდენტი რომლის ინგლისურის ქულაც მეტია საშუალო ინგლისურის ქულაზე
def english_grade_greater_than_average():
    print("--------------- დავალება 3 ---------------")
    print("\n")

    english_grades = grades[:, subjects.index('ინგლისური') + 1].astype(int)
    avg_english_grade = np.mean(english_grades)
    print("\nსტუდენტები,რომელთა ქულაც მეტია საშუალო ქულაზე ინგლისურში")
    for index, grade in enumerate(english_grades):
        if grade > avg_english_grade:
            print(grades[index])
    print("\n")


# # Visualise table
def print_grades_table():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    df = pd.DataFrame(grades, columns=['Student Name'] + subjects)

    print(df)

avg_grades()
best_and_worst_math_students()
english_grade_greater_than_average()
# print_grades_table()


