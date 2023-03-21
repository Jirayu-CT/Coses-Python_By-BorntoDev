'''open() ตัวแรกคือชื่อไฟล์ ต่อมาคือ โหมด "r"=การอ่าน '''
file = open("C:\\Users\Acer\Desktop\CoursePython_Borntodev\Coses-Python_By-BorntoDev\section12\demo.txt", "r")

'''.read() คือการอ่าน'''
print(file.read())
print(file.read(16))

'''.readline คือการอ่านทีล่ะบรรทัด'''
print(file.readline())
print(file.readline())
