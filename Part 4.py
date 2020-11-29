#assigning Progression Outcome messages to a dictionary

progressions = {"pro":"Progress","pro_mt":"Progress (module trailer)","d_pro":"Do not Progress – module retriever","exc":"Exclude"}

#creating function for getting input marks

def student_mark_input():

    #gettings inputs for pass,defer and fail marks
    
    total_check=1

    #iteration for check total marks are less than 121

    while total_check==1:

        #calling functions for input and check vaied

        pass_mark=pass_input()
        defer_mark=defer_input()
        fail_mark=fail_input()

        #adding all the marks and assign into a variable 'total'

        total=pass_mark+defer_mark+fail_mark
        
        #check is the total is graeter than 120

        if (total>120) or(total<120):

            #print this and loop
    
            print("Total incorrect.\n")

        else:

            #ends loop

            total_check=0
    

    #returns pass_mark, defer_mark and fail_mark

    return pass_mark,defer_mark,fail_mark

#creating function for get input of pass marks and check that valied

def pass_input():

    #initialize this for loop

    type_match=1

    #loop for check value is valied

    while type_match==1:
        
        #added try catch to catch wrong type error

        try:

            #input passs mark

            pass_mark = int(input("Please Enter Your Credits At Pass : "))

            #check mark is between 0 and 120

            if (pass_mark==120) or (pass_mark==100) or (pass_mark==80) or (pass_mark==60) or (pass_mark==40) or (pass_mark==20) or (pass_mark==0):

                #stops loop

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
    
    #returning value of passmark

    return pass_mark

def defer_input():

    #this is like same as privius function, this is for input defer marks

    type_match=1

    while type_match==1:
        
        try:

            defer_mark = int(input("Please Enter Your Credits At Defer : "))
            if (defer_mark==120) or (defer_mark==100) or (defer_mark==80) or (defer_mark==60) or (defer_mark==40) or (defer_mark==20) or (defer_mark==0):

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
            type_match=1
    
    return defer_mark

def fail_input():

    #this is like same as privius function, this is for input fail marks

    type_match=1

    while type_match==1:
        
        try:

            fail_mark = int(input("Please Enter Your Credits At Fail : "))
            if (fail_mark==120) or (fail_mark==100) or (fail_mark==80) or (fail_mark==60) or (fail_mark==40) or (fail_mark==20) or (fail_mark==0):

                type_match=0
            
            else:

                print("Out of range.\n")
        
        except:
           
            print("Integer required\n")
            type_match=1
    
    return fail_mark

#creating function for check Progression Outcome and print the message

def progress_check(pass_mark,defer_mark,fail_mark):

    # imported variables from global scope

    global pro_count
    global trail_count
    global retriew_count
    global exclude_count
    
    #concatinate string values of pass_mark, defer_mark and fail_mark by '|' and assign it to 'marks'

    marks = str(pass_mark) + "|" + str(defer_mark) + "|" + str(fail_mark)

    #assign empty string for variable 'prog'
    
    prog = ''
    
    #checking marks for 'Progress' Progression Outcome

    if marks == '120|0|0':
    
        #assign Progression Outcome message to a new variable called 'prog'

        prog = progressions["pro"]

        # increased progress count

        pro_count=pro_count+1
    
    #checking marks for 'Progress (module trailer)' Progression Outcome

    elif (marks == '100|20|0') or (marks == '100|0|20') :
    
        prog = progressions["pro_mt"]

        trail_count=trail_count+1
    
    #checking marks for 'Do not Progress – module retriever' Progression Outcome

    elif (marks == '80|40|0') or (marks == '80|20|20') or (marks == '80|0|40') or (marks == '60|60|0') or (marks == '60|40|20') or (marks == '60|20|40') or (marks == '60|0|60') or (marks == '40|80|0') or (marks == '40|60|20') or (marks == '40|40|40') or (marks == '40|20|60') or (marks == '20|100|0') or (marks == '20|80|20') or (marks == '20|60|40') or (marks == '20|40|60') or (marks == '0|120|0') or (marks == '0|100|20') or (marks == '0|80|40') or (marks == '0|60|60'):
    
        prog = progressions["d_pro"]

        retriew_count=retriew_count+1
    
    #checking marks for 'Exclude' Progression Outcome

    elif (marks == '40|0|80') or (marks == '20|20|80') or (marks == '20|0|100') or (marks == '0|40|80') or (marks == '0|20|100') or (marks == '0|0|120'):
    
        prog = progressions["exc"]

        exclude_count=exclude_count+1
    
    else:
        print("Total Incorrect .")
    #print Progression Outcome message

    print(prog,"\n")

# initialized variables with starting values
run=1
pro_count=0
trail_count=0
retriew_count=0
exclude_count=0

#print dashes for identify outtputs clearly

print("------------------------------------------------------------")

while run==1:

    #calling student_mark_input function

    marks=student_mark_input()

    #calling progress_check function

    progress_check(marks[0],marks[1],marks[2])

    #print dashes for identify outtputs clearly

    response=0

    #loops prompt for another marks of student

    while response==0:
    
        #prompt for users action

        user_dec=input("Do You Want To Enter Marks Of Another Student or quite program ?(y/q) ").lower()

        if user_dec=='q':

            #if user entrer 'q' this will executed

            #setting this valus stops the loop       
            run=0
            response=1

            #calculates total students

            total_outcome=pro_count+trail_count+retriew_count+exclude_count
            

            print("\nVertical Histogram")
            print("------------------------------------------------------------\n")

            #heading for vertical histogram
            
            print("Progress \tTrailing \tRetriever \tExcluded")
            
            #create a list wich conntains all student counts to find max of them

            prog_list=[pro_count,trail_count,retriew_count,exclude_count]
            
            #calculate maximum ofcounts and assign it into a variable 'max_prog'

            max_prog=max(prog_list)
            
            #for loop to print vertical histogram

            for i in range(max_prog):

                # column 1

                if pro_count>i:
                  
                    print('   *',"\t\t",end='')
                
                else:
                
                    print("   \t\t",end='')
                
                #column 2

                if trail_count>i:
                
                    print('   *',"\t\t",end='')
                
                else:
                
                    print("   \t\t",end='')
                
                #column 3

                if retriew_count>i:
                
                    print('   *',"\t\t",end='')
                
                else:
                
                    print("   \t\t",end='')
                
                #column 4

                if exclude_count>i:
                
                    print('   *',"\t\t")
                
                else:
                
                    print("   \t\t")

        elif user_dec=='y':

            #this will execute when user input 'y' as action

            
            
            response=1

        else:

            #this will execute when user inputs wrong input

            print("Cannot Recognize Your Response ! \n")

print("------------------------------------------------------------")
