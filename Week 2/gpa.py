def calculate_gpa(report_card):
    grades = report_card.values()
    total = 0

    for grade in grades:
        if grade == 'A':
            total += 4
        elif grade == 'B':
            total +=3
        elif grade == 'C':
            total +=2
        elif grade == 'D':
            total +=1
    
    return (.2f"{total/len(report_card)}")

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))