student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def grade_from_score(score):
    if score >90:
        return('Outstanding')
    elif score <= 90 and score >80:
        return("Exceeds Expectations")
    elif score <= 80 and score >70:
        return("Acceptable")
    elif score <=70:
        return("Fail")


for key in student_scores:
    student_grades[key] = grade_from_score(student_scores[key])
    

# 🚨 Don't change the code below 👇
print(student_grades)
