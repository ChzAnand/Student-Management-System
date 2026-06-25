class Student:
  def __init__(self,student_id,name,age,marks):
    self.student_id=student_id
    self.name=name
    self.age=age
    self.marks=marks

  def display(self):
    print("\nStudent ID:", self.student_id)
    print("Name :",self.name)
    print("Age :",self.age)
    print("Marks :",self.marks)
class StudentManagementSystem:
  def __init__(self):
    self.students=[] #database

  def add_student(self):
    student_id=int(input("Enter Student ID: "))
    for stud in self.students:
      if stud.student_id==student_id:
        print("Student with same ID already exists")
        return
    name=input("Enter Student Name: ")
    age=int(input("Enter Student Age: "))
    marks=float(input("Enter Student Marks: "))

    student=Student(student_id,name,age,marks)#student class ka obj yha create hua haii...
    self.students.append(student)
    print("Student added successfully")
  
  def view_students(self):
    if not self.students:
      print("No Students found")
    else:
      print("\nStudent List:")

      for i in self.students:
        i.display()
  def search_student(self):
    student_id=int(input("Enter Student ID to search: "))
    for stud in self.students:
      if stud.student_id==student_id:
        stud.display()
      else:
        print("Student not fount")
  
  def update_marks(self):
    student_id=int(input("Enter Student ID to update marks: "))
    for stud in self.students:
      if stud.student_id==student_id:
        new_marks=float(input("Enter new marks: "))
        stud.marks=new_marks
        print("Marks updated successfully")
        return
    print("Student not founf")
  

  def delete_student(self):
    student_id=int(input("Enter Student ID to delete: "))
    for stud in self.students:
      if stud.student_id==student_id:
        self.students.remove(stud)
        print("Student deleted successfully")
        return
    print("Student not found")
  
  def high(self):
    
    topper=self.students[0]
    for stud in self.students:
      if stud.marks>topper.marks:
        topper=stud
    print("Topper:")
    topper.display()

sms=StudentManagementSystem()
while True:
  print("\nStudent Management System")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Marks")
  print("5. Delete Student")
  print("6. Topper")
  print("7. Exit")

  choice=input("Enter your choice (1-7): ")
  if choice=='1':
    n=int(input("Enter the no. of students you want to enter: "))
    for i in range(n):

      sms.add_student()
  elif choice=='2':
    sms.view_students()
  elif choice=='3':
    sms.search_student()
  elif choice=='4':
    sms.update_marks()
  elif choice=='5':
    sms.delete_student()
  elif choice=='6':
    sms.high()
  elif choice=='7':
    print("Exiting Student Management System")
    break
  else:
    print("Invalid choice. Please try again.")
   
  

  
    
