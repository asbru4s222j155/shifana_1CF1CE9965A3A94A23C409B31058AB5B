class Student :

  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,key=lambda student:student.cgpa,reverse=True)
 #Syntax - lambda arg:exp 
  return sorted_students

#Example usage:
student =[
  Student("Hari","A123",7.8),
  Student("Dharani","A124",8.9),
  Student("Nivetha","A125",9.1),
  Student("Abitha","A126",9.9),
]

sorted_students = sort_students(student)

#First the sortd list of students
for student in sorted_students:
  print("Name: {}, Roll Number:{}, CGPA:{}".format(student.name,student.roll_number,
                                                   student.cgpa))