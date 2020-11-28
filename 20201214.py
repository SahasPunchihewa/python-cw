progressions = {"pro":"Progress","pro_mt":"Progress (module trailer)","d_pro":"Do not Progress – module retriever","exc":"Exclude"}

def student_mark_input():
    pass_mark = int(input("Please Enter Your Credits At Pass : "))
    defer_mark = int(input("Please Enter Your Credits At Defer : "))
    fail_mark = int(input("Please Enter Your Credits At Fail : "))
    return pass_mark,defer_mark,fail_mark

def progress_check(pass_mark,defer_mark,fail_mark):
    
    marks = str(pass_mark) + "|" + str(defer_mark) + "|" + str(fail_mark)
    #print(marks)
    prog = ''
    
    if marks == '120|0|0':
    
        prog = progressions["pro"]
    
    elif (marks == '100|20|0') or (marks == '100|0|20') :
    
        prog = progressions["pro_mt"]
    
    elif (marks == '80|40|0') or (marks == '80|20|20') or (marks == '80|0|40') or (marks == '60|60|0') or (marks == '60|40|20') or (marks == '60|20|40') or (marks == '60|0|60') or (marks == '40|80|0') or (marks == '40|60|20') or (marks == '40|40|40') or (marks == '40|20|60') or (marks == '20|100|0') or (marks == '20|80|20') or (marks == '20|60|40') or (marks == '20|40|60') or (marks == '0|120|0') or (marks == '0|100|20') or (marks == '0|80|40') or (marks == '0|60|60'):
    
        prog = progressions["d_pro"]
    
    elif (marks == '40|0|80') or (marks == '20|20|80') or (marks == '20|0|100') or (marks == '0|40|80') or (marks == '0|20|100') or (marks == '0|0|120'):
    
        prog = progressions["exc"]
    
    print(prog)

print("------------------------------------------------------------")
marks=student_mark_input()
progress_check(marks[0],marks[1],marks[2])
print("------------------------------------------------------------")