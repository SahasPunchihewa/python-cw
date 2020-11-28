#asign values to three lists one for pass marks , one for defer marks and the other for fail marks

pass_list=[120,100,100,80,60,40,20,20,20,0]
defer_list=[0,20,0,20,40,40,40,20,0,0]
fail_list=[0,0,20,20,20,40,60,80,100,120]

#assigning Progression Outcome messages to a dictionary

progressions = {"pro":"Progress","pro_mt":"Progress (module trailer)","d_pro":"Do not Progress – module retriever","exc":"Exclude"}

#initializing values in to 0

pro_count=0
trail_count=0
retriew_count=0
exclude_count=0

#create function for the checking

def checker():

    #import variables form global scope

    global pro_count
    global trail_count
    global retriew_count
    global exclude_count

    #loop for get each record of marks

    for i in range (len(pass_list)):

        #concatinate marks to compare

        marks=str(pass_list[i])+'|'+str(defer_list[i])+'|'+str(fail_list[i])

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
        
        #print Progression Outcome message

        print(prog)
        
        

        
def histogram(pro_count,trail_count,retriew_count,exclude_count):
    
    #calculates total students
    
    total_outcome=pro_count+trail_count+retriew_count+exclude_count
    print()

    
        #show histogrem of student progresses
    
    print("Horizontal Histogram\nProgress \t",pro_count," : ",'*'*pro_count,"\nTrailer \t",trail_count," : ",'*'*trail_count,"\nRetriever \t",retriew_count," : ",'*'*retriew_count,"\nExcluded \t",exclude_count," : ",'*'*exclude_count,"\n\n",total_outcome," outcomes in total.")


#calling functions

checker()
histogram(pro_count,trail_count,retriew_count,exclude_count)
