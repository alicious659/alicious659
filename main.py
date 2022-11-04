student_records = {
      "name": "James Webb",
      "id": "APT5005",
      "courses":[
         {"title": "English", "unit": 2, "code": "ENG101", "score": 60},
         {"title": "Chemistry I", "unit": 4, "code": "CHE101", "score": 70},
         {"title": "Maths", "unit": 3, "code": "MTH101", "score": 80},
         {"title": "Chemistry II", "unit": 4, "code": "CHE102", "score": 91}, 
         {"title": "History", "unit": 2, "code": "HIS102", "score": 40}
      ]
 }

items = {course:value for course,value in student_records.items()}
course_list = items['courses']
#print(course_list)

new_unit = [course['unit'] for course in course_list]

#print (new_unit)

new_score = [score['score'] for score in course_list]
your_score = []
your_indexGrade = []
for x in new_score:
   
      if x >= 70:
        your_score.append('A')
        your_indexGrade.append(5)
      elif x >=60 and x <=69:
         your_score.append('B')
         your_indexGrade.append(4)
      elif x >=50 and x <=59:
         your_score.append('C')
         your_indexGrade.append(3)
      elif x >=45 and x <=49:
         your_score.append('D')
         your_indexGrade.append(2)
      elif x >=40 and x <=44:
         your_score.append('E')
         your_indexGrade.append(1)
      elif x <=39 :
         your_score.append('F')
         your_indexGrade.append(0)
         
    



QP = [your_indexGrade[i] * new_unit[i] for i in range(len(new_unit))]
#print(QP)
TQP = 0
for total in QP:
   TQP +=total
#print(TQP)

Total_unit = 0
for add in new_unit:
   Total_unit +=add
#print(Total_unit)

CGPA = TQP/Total_unit

print(round(CGPA,2))

