import pandas as pd
def assign_grade(score):
    if score >= 90:
        gpa = 4
    elif score >= 80:
        gpa = 3
    elif score >= 70:
        gpa = 2
    else:
        gpa = 1
    
    return gpa
scores = pd.read_csv('scores.csv', header = 0, index_col=0)
gpa_grade = scores.applymap(assign_grade)
pd.set_option('precision',2)
means = gpa_grade.mean()
print(means)
total_class_average = means.mean()
print(f'The class GPA is {total_class_average:.2f}')