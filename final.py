import string
import random
#################chatbot 1.0 ultimate(pro version)###################

default = "pardon me!!!\ni could not understand you?\nenter other querry u want to inquire??"
form_out="01-01-2012\nenter other querry u want to inquire??"
last_form_sub="25-01-2012\nenter other querry u want to inquire??"
test_date="01-02-2012\nenter other querry u want to inquire??"
rest_result_date="15-02-2012\nenter other querry u want to inquire??"
how_result="via net and post\nenter other querry u want to inquire??"
type_exam="mcq\nenter other querry u want to inquire??"
how_interview="it is held in parts etc etc....\nenter other querry u want to inquire??"
syllabus="10+2 level quetions to be asked\nenter other querry u want to inquire??"
faculty="we have wold class faculty\nenter other querry u want to inquire??"
infrastructure="we have state of the art campus....etc etc.....\nenter other querry u want to inquire??"
exams_held="chill re!!! it is quite easy!!\nenter other querry u want to inquire??"
interview_date="25-02-2012\nenter other querry u want to inquire??"
events="check the following link ww.cic.du.ac.in/events\nenter other querry u want to inquire??"
sem_date="dates to be announced later\nenter other querry u want to inquire??"
sem_result="dates to be anounced\nenter other querry u want to inquire??"
check_site="please check cic.du.ac.in for further info\nenter other querry u want to inquire??"
location="rubby sevens building,cavalry lanes\nany other querry u want to inquire??"
full_form="cluster innovation center,university of delhi\nany other querry u want to inquire??"
############   word search  #########################
def feasy(input,n,output):
    
    if input in n:
        print output


#############   particular search   #################
def find_words(text,search,output):
    

   dText = {}
   dSearch = {}

   dText = text.split()
   dSearch = search.split()

   lenText = len(dText)
   lenSearch = len(dSearch)

   found_word = 0

   for text_word in dText:
      for search_word in dSearch:
         if hash(search_word) == hash(text_word):
            found_word += 1

   if found_word == lenSearch:
       print output

##########################################
def admission():
    print 'admission for all the courses is done in two stages:\n'
    print '1.written test\n'
    print '2.interview\n'
    print "\nfor more info I strongly recommend you to visit CIC's website\n"
#########################################
def intro():
    print "\nThe Cluster Innovation Centre (CIC) is a unique place\nwithin the University of Delhi.\nCIC provides a springboard for new ideas to emerge \nand constantly translate them to workable projects in the real world."
    print "At CIC, we strive to break the functional fixedness of academia\nand look at the world with a new perspective using state of art facilities."
def innovation():
    print "\nThe program will include training in core Mathematics,\nIT and science disciplines and additional courses on innovation\nand technology management, entrepreneurship, business, communications, etc."
################function how##################
def how(input):
    input=string.lower(input)
    find_words(input,"result",how_result)
    find_words(input,"interview",how_interview)
    find_words(input,"faculty",faculty)
    find_words(input,"infrastructure",infrastructure)
    find_words(input,"exams" or "exam",exams_held)
    find_words(input,"reach",location)
###############function when###################
def when(input):
    input=string.lower(input)
    if  "admission" and ("form" or "forms") in input:
        find_words(input,"out",form_out)
        find_words(input,"last",last_form_sub)
    find_words(input,"interview",interview_date)
    find_words(input,"result",rest_result_date)
    find_words(input,"events",events)
    find_words(input,"interview",interview_date)
    find_words(input,"fest",events)
    if "enterance" in input:
        find_words(input,"exams",test_date)
        find_words(input,"exam",test_date)
        find_words(input,"result",rest_result_date)
    if "semester"or "sem" in input :
        find_words(input,"exams",sem_date)
    find_words(input,"workshop",events)
######################function what##############
def what(input):
    find_words(input,"last date",last_form_sub)
    find_words(input,"form out",form_out)
    find_words(input,"exam",type_exam)
    find_words(input,"result",rest_result_date)
    find_words(input,"interview date",interview_date)
    find_words(input,"syllabus",syllabus)
    find_words(input,"result date",rest_result_date)
    find_words(input,"course",check_site)
    find_words(input,"courses",check_site)
    find_words(input,"location",location)
    if "cic" in input:
        find_words(input,"cic",full_form)
        intro1=raw_input("do you want to know more about it ?")
        if intro1=="yes" or "y" or "haan" :
            intro()
    
    if "admission" in input:
        admission()
    if "eligibility" in input :
        eligibility()
####################function where##############
def where(input):
    find_words(input,"located",location)
    find_words(input,"cic",location)
####################eligiblity##################
def eligibility():
    print "let me check if you can apply for CIC entrance examination\nanswer the following questions in yes or no only"
    e1=raw_input("\nhave you passed 12th class??\n")
    if e1 == "yes":
        e2=raw_input("did you study mathematics in 12th class??\n")
        if e2 == "yes":
            e3=raw_input("what was your aggregate percentage in best three subjects??\n")
            if e3 >= "60" :
                e4=raw_input("have you registered for any of DU course??\n")
                if e4 == "yes":
                    e5=raw_input("what is your age??\n")
                    if e5 <=  "21":
                        e6 = raw_input("are you a graduate?\n")
                        if e6 == "no" or "yes":
                            print "Congratulations!! , you are eligible to apply for B.Tech courses\n"
                            e7 = raw_input("have studied mathematics for atleast one year in graduation?\n")
                            
                            if e7 == "yes" :
                                    print "Congratulations!! , you are eligible to apply for master of mathematics education course\n"          
                                     
                            else:
                                print "\nsorry you are not eligible to give enterance exam for master of mathematics education course"
                        else:
                            print "\nsorry you are not eligible to give enterance exam"
                    else:
                        print "\nsorry you are not eligible to give enterance exam"
                else:
                    print "\nsorry you are not eligible to give enterance exam"
            else:
                print "\nsorry you are not eligible to give enterance exam"
        else:
            print "\nsorry you are not eligible to give enterance exam"
            
                
                    
                        
                            
    else:
        print "\nsorry you are not eligible to give enterance exam"
###################################################################
def busier(input):
    
    x=random.randint(1,10)
    if x== 1 :
        print "what do you mean by this ?"
    elif x==2 :
        print "what is ", input," ?? "
    elif x==3 :
        print "what", input ," ?? "
    elif x==4 :
        print "i only understand english \nplease try something else :( "
    elif x==5 :
        print "kindly be more specific about ",input
    elif x==6 :
        print input, "??...."
    elif x==7 :
        print "i think i dont know that !!:( \n:("
    elif x==8:
        print "hmmm\ni dont think that's relevant"
    elif x==9 :
        print "ohhh change the question or check what u have typed and try asking me again"
    else :
        print "what u mean by " ,input
        
def main():
    print"Cluster Innovation Centre :-)"
    input=raw_input("hello there\n")
    n1={"bye","bii"}
    c=1
    while ((input not in n1) and (c==1)):
        input=string.lower(input)
        n={"hello","hi","namastey","hey","yes","how","he"}
        output="how can i help you"
        print "\n"
        feasy(input,n,output)
        input=raw_input("")
        
        if "how" in input :
            how(input)
        elif ( "when" in input):
            when(input)
        elif( "what" in input):
            what(input)
        elif("where" in input):
            where(input)
        elif ("eligibility" in input):
            eligibility()
        elif ("eligible "in input):
            eligibility()
        elif "like" in input:
            print "\nwhat resemblence do you see?"
        elif "i think" in input:
            print "\nwhat makes you think that?"
        elif "always" in input:
            print "\ncan you think of a specific example?"
        elif "all" in input:
            print "\nin what way?"
        elif "of me" in input:
            print "\ndoes it please you to believe that?"
        elif "can't" in input:
            print "\nwhy?"
        elif "don't" in input:
            print "\nhow can you say that?"
       
        elif (("bye" or "bii" or "exit" or "null") not in input):
            busier(input)
        else:
            c=1
            print"bye it was nice talking to you"
           
main()
raw_input("............:) :) .............")
