students = [
    {"name": "A", "mark": {"Tamil": 85, "English": 90, "Maths": 95, "Science": 80, "Social": 75}},
    {"name": "B", "mark": {"Tamil": 88, "English": 85, "Maths": 90, "Science": 82, "Social": 80}}]
    # 2) Two students — one higher overall average


    # {"name": "c", "mark": {"Tamil": 90, "English": 80, "Maths": 85, "Science": 75, "Social": 70}},
    # {"name": "d", "mark": {"Tamil": 80, "English": 70, "Maths": 75, "Science": 65, "Social": 60}},
    # # 1) Distinct overall averages — simple order


    # {"name": "e", "mark": {"Tamil": 92, "English": 88, "Maths": 85, "Science": 95, "Social": 90}},
    # {"name": "f", "mark": {"Tamil": 90, "English": 90, "Maths": 85, "Science": 95, "Social": 90}}
    # 3) Two students — overall tie and sub-average tie → full tie



for el in range(len(students)):
    for avg in range(len(students[el2][1])):
            avg1+=students[el][1][avg]
            avg1=avg1/len(students[el][1])
    small=el
    for el2 in range(el,len(students)):
        for el3 in range(len(students[el2][1])):
            avg2+=students[el2][1][el3]
            avg2=avg2/len(students[el2][1])
    if avg1>avg2:
         avg1=avg2   
        