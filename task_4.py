res_students = {'Khabarov Fyodor Tarasovich': [290, 'accepted'],
                'Loktionova Aleksandra Borisovna': [256, 'not accepted'],
                'Mitrofanov Viktor Leonidovich': [261, 'accepted'],
                'Andreyev Denis Rostislavovich': ['an exam is not passed', 'not accepted']}
enrollee = {'Khabarov Fyodor Tarasovich': ["History", "R 88", "M 80", "H 93", "P -", "L 99"],
            'Loktionova Aleksandra Borisovna': ["Physics", "R 90", "M 96", "H 78", "P 70", "L -"],
            'Mitrofanov Viktor Leonidovich': ["Physics", "R 87", "M 91", "P 78", "L 66", "H 93"],
            'Andreyev Denis Rostislavovich': ["History", "M 71", "R 95",  "H -", "P -", "L 88"]}
olympiad = {'Andreyev Denis Rostislavovich': ["history"],
            'Khabarov Fyodor Tarasovich': ["history", "russian"],
            'Loktionova Aleksandra Borisovna': ["literature"],
            'Mitrofanov Viktor Leonidovich': ["math"]}
exams = {"Physics": ["Russian", "Math", "Physics"], "History": ["Russian", "History", "Literature"]}
min_score = {"Physics": 260, "History": 280}

students = {}

for key, value in enrollee.items():
    std_exams = [_[0] for _ in exams[value[0]]]
    sum_std = 0
    for i in range(1, 6):
        exm = value[i].split(' ')
        if exm[0] in std_exams:
            if exm[1] == '-':
                sum_std = 'an exam is not passed'
                break
            sum_std += int(exm[1])
            for val in olympiad[key]:
                if val[0].upper() == exm[0]:
                    sum_std += 5
    if not isinstance(sum_std, str) and min_score[value[0]] <= sum_std:
        students[key] = [sum_std, 'accepted']
    else:
        students[key] = [sum_std, 'not accepted']