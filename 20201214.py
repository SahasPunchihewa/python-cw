#assigning Progression Outcome messages to a dictionary

progressions = {"pro":"Progress","pro_mt":"Progress (module trailer)","d_pro":"Do not Progress – module retriever","exc":"Exclude"}

#creating function for getting input marks

def student_mark_input():

    #gettings inputs for pass,defer and fail marks
    
    total_check=1

    while total_check==1:

        pass_mark=pass_input()
        defer_mark=defer_input()
        fail_mark=fail_input()
        total=pass_mark+defer_mark+fail_mark
        
        if total>120:
            
            print("Total incorrect.\n")

        else:

            total_check=0
    

    #returns pass_mark, defer_mark and fail_mark

    return pass_mark,defer_mark,fail_mark

def pass_input():

    type_match=1

    while type_match==1:
        
        try:

            pass_mark = int(input("Please Enter Your Credits At Pass : "))
            if (pass_mark<=120) and (pass_mark>=0):

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
    
    return pass_mark

def defer_input():

    type_match=1

    while type_match==1:
        
        try:

            defer_mark = int(input("Please Enter Your Credits At Defer : "))
            if (defer_mark<=120) and (defer_mark>=0):

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
            type_match=1
    
    return defer_mark

def fail_input():

    type_match=1

    while type_match==1:
        
        try:

            fail_mark = int(input("Please Enter Your Credits At Fail : "))
            if (fail_mark<=120) and (fail_mark>=0):

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
            type_match=1
    
    return fail_mark

#creating function for check Progression Outcome and print the message

def progress_check(pass_mark,defer_mark,fail_mark):
    
    #concatinate string values of pass_mark, defer_mark and fail_mark by '|' and assign it to 'marks'

    marks = str(pass_mark) + "|" + str(defer_mark) + "|" + str(fail_mark)

    #assign empty string for variable 'prog'
    
    prog = ''
    
    #checking marks for 'Progress' Progression Outcome

    if marks == '120|0|0':
    
        #assign Progression Outcome message to a new variable called 'prog'

        prog = progressions["pro"]
    
    #checking marks for 'Progress (module trailer)' Progression Outcome

    elif (marks == '100|20|0') or (marks == '100|0|20') :
    
        prog = progressions["pro_mt"]
    
    #checking marks for 'Do not Progress – module retriever' Progression Outcome

    elif (marks == '80|40|0') or (marks == '80|20|20') or (marks == '80|0|40') or (marks == '60|60|0') or (marks == '60|40|20') or (marks == '60|20|40') or (marks == '60|0|60') or (marks == '40|80|0') or (marks == '40|60|20') or (marks == '40|40|40') or (marks == '40|20|60') or (marks == '20|100|0') or (marks == '20|80|20') or (marks == '20|60|40') or (marks == '20|40|60') or (marks == '0|120|0') or (marks == '0|100|20') or (marks == '0|80|40') or (marks == '0|60|60'):
    
        prog = progressions["d_pro"]
    
    #checking marks for 'Exclude' Progression Outcome

    elif (marks == '40|0|80') or (marks == '20|20|80') or (marks == '20|0|100') or (marks == '0|40|80') or (marks == '0|20|100') or (marks == '0|0|120'):
    
        prog = progressions["exc"]
    
    #print Progression Outcome message

    print(prog)

#print dashes for identify outtputs clearly

print("------------------------------------------------------------")

#calling student_mark_input function

marks=student_mark_input()

#calling progress_check function

progress_check(marks[0],marks[1],marks[2])

#print dashes for identify outtputs clearly

print("------------------------------------------------------------")