'''open() ตัวแรกคือชื่อไฟล์ ต่อมาคือ โหมด "r"=การอ่าน "a"=เพิ่มข้อความต่อท้ายไปเรื่อยๆ "w"=คือการเขียนทับตัวไฟล์เดิม "x"=การสร้างไฟล์'''

file = open("C:\\Users\Acer\Desktop\CoursePython_Borntodev\Coses-Python_By-BorntoDev\section12\demo.txt", "a")
file.write("Haha From Bext Lecture")


file = open("C:\\Users\Acer\Desktop\CoursePython_Borntodev\Coses-Python_By-BorntoDev\section12\demo.txt", "w")
file.write("Haha From Bext Lecture")
