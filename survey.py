import streamlit as st
from fetch import*
from login import login_dict
from login import name_dict
from model import prediction
import MySQLdb
from pymysql import *
from pymysql import cursors

def submit(ans =None, question =None):
    marks= 0

    if question == "1" or question == "2" or question == "3"or question == "4"or question == "5"or question == "6":
            if ans == 'No-never':
                marks = 4
            elif ans == 'Sometimes':
                marks = 2
            else:
                marks = 0
        
    else:
        if ans == 'No':
            marks = 4
        elif ans == 'Unknown':
            marks = 2
        else:
            marks = 0

    # print(f"Question {question}: Marks = {marks}")
    return marks
    
    





diss = {}

def main():
    anssdic={}
    
    front_up()
    try:
        st.write('User Logged in as',name_dict['name'])
        pk = login_dict["key"]
        na = name_dict['name']
        #st.write("primary key" ,pk)
        st.write("Name " ,na)
    except:
        st.error(" Please Log in")
    
    st.title("SURVEY")
    
    
    if st.checkbox('Question I', key ='q1',value=True):
        st.info(" Did your child struggle to learn to count?")
        
        ansq1 = st.radio("Answer:", ['Yes-frequently','Sometimes','No-never'], key ='q1_radio')
        anssdic['ansq1'] =ansq1
        # if st.button("SUBMIT", key='q1_submit'):
        #     st.write(ansq1)
        #     marks1 = submit(ans = ansq1, question ="1")
        #     st.write(marks1)
        #     diss.update({'marks1':marks1})
        #     #st.write(anssdic)
        #     #st.write(diss)
            
            
    
    if st.checkbox('Question II', key ='q2',value=True):
        st.info("Does he/she say numbers out of order — long after peers have mastered this skill? ")
        
        ansq2 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No-never'], key ='q2_radio')
        anssdic['ansq2'] = ansq2
        # if st.button("SUBMIT", key='q2_submit'):
        #     st.write(ansq2)
        #     marks2 = submit(ans = ansq2, question ="2")
        #     diss.update({'marks2':marks2})
        #     #st.write(anssdic)
        #     #st.write(diss)
            
            
            
    
    if st.checkbox('Question III', key ='q3',value=True):
        st.info(" Does your child not seem to understand the connection between the symbol “4” and the word “four?” Does he make mistakes when reading or following directions involving number words and symbols?")
        
        ansq3 = st.radio("Answer:",  ['Yes-frequently','Sometimes','No -never'], key = 'q3_radio')
        anssdic['ansq3'] =ansq3
        # if st.button("SUBMIT", key='q3_submit'):
        #     st.write(ansq3)
        #     marks3 = submit(ans = ansq3, question ="3")
        #     diss.update({'marks3':marks3})
            #st.write(anssdic)
            #st.write(diss)
            
            
    
    if st.checkbox('Question IV', key ='q4',value=True):
        st.info("Does your child struggle to connect the concept of numbers to real-world items? When you ask him how many cookies are left, for example, does he seem confused by the question or answer incorrectly?")
        
        
        ansq4 = st.radio("Answer",['Yes-frequently','Sometimes','No-never'], key = 'q4_radio')
        anssdic['ansq4'] = ansq4
        # if st.button("SUBMIT", key='q4_submit'):
        #     st.write(ansq4)
        #     marks4 = submit(ans = ansq4, question ="4")
            
        #     diss.update({'marks4':marks4})
        #     #st.write(anssdic)
        #     #st.write(diss)
            
    
    if st.checkbox('Question V', key ='q5',value=True):
        st.info("Does your child not seem to understand the difference between adding and subtracting? Does she confuse the  +  and  –  symbols when completing math problems?")
        
        ansq5 = st.radio("Answer:", ['Yes-frequently','Sometimes','No-never'], key = 'q5_radio')
        anssdic['ansq5'] = ansq5
        # if st.button("SUBMIT", key='q5_submit'):
        #     st.write(ansq5)
        #     marks5 = submit(ans = ansq5, question ="5")
        #     diss.update({'marks5':marks5})
        #     #st.write(anssdic)
        #     #st.write(diss)
            
    
    if st.checkbox('Question VI', key ='q6',value=True):
        st.info("Does your child still count on his fingers past third grade?")
    
        ansq6 = st.radio("Answer:",['Yes-frequently','Sometimes','No-never'], key = 'q6_radio')
        anssdic['ansq6'] = ansq6
        # if st.button("SUBMIT", key='q6_submit'):
        #     st.write(ansq6)
        #     marks6 = submit(ans = ansq6, question ="6")
        #     diss.update({'marks6':marks6})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    if st.checkbox('Question VII', key ='q7',value=True):
        st.info(" Difficulty sustaining attention; seems ""hyper"" or ""daydreamer"" ")
        
        ansq7 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q7_radio')
        anssdic['ansq7'] = ansq7
        # if st.button("SUBMIT", key='q7_submit'):
        #     st.write(ansq7)
        #     marks7 = submit(ans = ansq7, question ="7")
        #     diss.update({'marks7':marks7})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    if st.checkbox('Question VIII', key ='q8',value=True):
        st.info("Confused by letters, numbers, words, sequences, or verbal explanations.")
        
        ansq8 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q8_radio')
        anssdic['ansq8'] =ansq8
        # if st.button("SUBMIT", key='q8_submit'):
        #     st.write(ansq8)
        #     marks8 = submit(ans = ansq8, question ="8")
        #     diss.update({'marks8':marks8})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    if st.checkbox('Question IX', key ='q9',value=True):
        st.info(" Reads and rereads with little comprehension")
        
        ansq9 = st.radio("Answer:",['Yes','No','Unknown'], key = 'q9_radio')
        anssdic['ansq9'] = ansq9
        # if st.button("SUBMIT", key='q9_submit'):
        #     st.write(ansq9)
        #     marks9 = submit(ans = ansq9, question ="9")
        #     diss.update({'marks9':marks9})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    if st.checkbox('Question X', key ='q10',value=True):
        st.info("Difficulty putting thoughts into words; speaks in halting phrases; leaves sentences incomplete.")

        
        ansq10 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q10_radio')
        anssdic['ansq10'] = ansq10
        # if st.button("SUBMIT", key='q10_submit'):
        #     st.write(ansq10)
        #     marks10 = submit(ans = ansq10, question ="10")
        #     diss.update({'marks10':marks10})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    
    
    if st.checkbox('Question XI', key ='q11',value=True):
        st.info("Can count, but has difficulty counting objects and dealing with money.")

        
        ansq11 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q11_radio')
        anssdic['ansq11'] = ansq11
        # if st.button("SUBMIT", key='q11_submit'):
        #     st.write(ansq11)
        #     marks11 = submit(ans = ansq11, question ="11")
        #     diss.update({'marks11':marks11})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    
    if st.checkbox('Question XII', key ='q12',value=True):
        st.info("ory for sequences, facts and information that has not been experienced.")

        
        ansq12 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q12_radio')
        anssdic['ansq12'] = ansq12
        # if st.button("SUBMIT", key='q12_submit'):
        #     st.write(ansq12)
        #     marks12 = submit(ans = ansq12, question ="12")
        #     diss.update({'marks12':marks12})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    if st.checkbox('Question XIV', key ='q13',value=True):
        st.info("Complains of dizziness, headaches or stomach aches while reading.")

        
        ansq13 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q13_radio')
        anssdic['ansq13']= ansq13
        # if st.button("SUBMIT", key='q13_submit'):
        #     st.write(ansq13)
        #     marks13 = submit(ans = ansq13, question ="13")
        #     diss.update({'marks13':marks13})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    if st.checkbox('Question XIV', key ='q14',value=True):
        st.info("Is reading extremely difficult? (Below grade or age level.")

        
        ansq14 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q14_radio')
        anssdic['ansq14']= ansq14
        # if st.button("SUBMIT", key='q14_submit'):
        #     st.write(ansq14)
        #     marks14 = submit(ans = ansq14, question ="14")
        #     diss.update({'marks14':marks14})
        #     #st.write(anssdic)
        #     #st.write(diss)
    
    
    
    
    
    
    if st.checkbox('Question XV', key ='q15',value=True):
        st.info("Is spelling ability poor? Letters missed, reversed etc?")

        
        ansq15 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q15_radio')
        anssdic['ansq15'] =ansq15
        # if st.button("SUBMIT", key='q15_submit'):
        #     st.write(ansq15)
        #     marks15 = submit(ans = ansq15, question ="15")
        #     diss.update({'marks15':marks15})
        #     #st.write(anssdic)
        #     #st.write(diss)


    
    if st.checkbox('Question XVI', key ='q16',value=True):
        st.info("Is it difficult to rhyme words?(Not sure? Play a rhyming game with your child or student).")

        
        ansq16 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q16_radio')
        anssdic['ansq16'] = ansq16
        # if st.button("SUBMIT", key='q16_submit'):
        #     st.write(ansq16)
        #     marks16 = submit(ans = ansq16, question ="16")
        #     diss.update({'marks16':marks16})
        #     #st.write(anssdic)
        #     #st.write(diss)

    
    
    if st.checkbox('Question XVII', key ='q17',value=True):
        st.info("Is there difficulty telling time on a clock with hands and/or tying shoes with laces?")

        
        ansq17 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q17_radio')
        anssdic['ansq17'] = ansq17
        # if st.button("SUBMIT", key='q17_submit'):
        #     st.write(ansq17)
        #     marks17 = submit(ans = ansq17, question ="17")
        #     diss.update({'marks17':marks17})
        #     #st.write(anssdic)
        #     #st.write(diss)

 
 
    if st.checkbox('Question XVIII', key ='q18',value=True):
        st.info("Is there difficulty finding the right words while speaking? Lots of ums, ahs, 'those things', and 'that stuff'.")

        
        ansq18 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q18_radio')
        anssdic['ansq18'] =ansq18
        # if st.button("SUBMIT", key='q18_submit'):
        #     st.write(ansq18)
        #     marks18 = submit(ans = ansq18, question ="18")
        #     diss.update({'marks18':marks18})
        #     #st.write(anssdic)
        #     #st.write(diss)


    if st.checkbox('Question XIX', key ='q19',value=True):
        st.info(" Pauses, repeats or makes frequent mistakes when reading aloud.")

        
        ansq19 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q19_radio')
        anssdic['ansq19'] =ansq19
        # if st.button("SUBMIT", key='q19_submit'):
        #     st.write(ansq19)
        #     marks19 = submit(ans = ansq19, question ="19")
        #     diss.update({'marks19':marks19})
        #     #st.write(anssdic)
        #     #st.write(diss)


    if st.checkbox('Question XX', key ='q20',value=True):
        st.info("Unusually high or low tolerance for pain.")

        
        ansq20 = st.radio("Answer:", ['Yes','No','Unknown'], key = 'q20_radio')
        anssdic['ansq20'] =ansq20
        # if st.button("SUBMIT", key='q20_submit'):
        #     st.write(ansq20)
        #     marks20 = submit(ans = ansq20, question ="20")
        #     diss.update({'marks20':marks20})
        #     st.write("Your answers",anssdic)
        #     #st.write(diss)
     
    if st.button("Submit the quiz", key='submit'):
        try:
            # st.write(ansq1)
            marks1 = submit(ans = ansq1, question ="1")
            diss.update({'marks1':marks1})
            # st.write(ansq20)
            marks2 = submit(ans = ansq2, question ="2")
            diss.update({'marks2':marks2})
            # st.write(ansq20)
            marks3 = submit(ans = ansq3, question ="3")
            diss.update({'marks3':marks3})
            # st.write(ansq20)
            marks4 = submit(ans = ansq4, question ="4")
            diss.update({'marks4':marks4})
            # st.write(ansq20)
            marks5 = submit(ans = ansq5, question ="5")
            diss.update({'marks5':marks5})
            # st.write(ansq20)
            marks6 = submit(ans = ansq6, question ="6")
            diss.update({'marks6':marks6})
            # st.write(ansq20)
            marks7 = submit(ans = ansq7, question ="7")
            diss.update({'marks7':marks7})
            # st.write(ansq20)
            marks8 = submit(ans = ansq8, question ="8")
            diss.update({'marks8':marks8})
            # st.write(ansq20)
            marks9 = submit(ans = ansq9, question ="9")
            diss.update({'marks9':marks9})
            # st.write(ansq20)
            marks10 = submit(ans = ansq10, question ="10")
            diss.update({'marks10':marks10})
            # st.write(ansq20)
            marks11 = submit(ans = ansq11, question ="11")
            diss.update({'marks11':marks11})
            # st.write(ansq20)
            marks12 = submit(ans = ansq12, question ="12")
            diss.update({'marks12':marks12})
            # st.write(ansq20)
            marks13 = submit(ans = ansq13, question ="13")
            diss.update({'marks13':marks13})
            # st.write(ansq20)
            marks14 = submit(ans = ansq14, question ="14")
            diss.update({'marks14':marks14})
            # st.write(ansq20)
            marks15 = submit(ans = ansq15, question ="15")
            diss.update({'marks15':marks15})
            # st.write(ansq20)
            marks16 = submit(ans = ansq16, question ="16")
            diss.update({'marks16':marks16})
            # st.write(ansq20)
            marks17 = submit(ans = ansq17, question ="17")
            diss.update({'marks17':marks17})
            # st.write(ansq20)
            marks18 = submit(ans = ansq18, question ="18")
            diss.update({'marks18':marks18})
            # st.write(ansq20)
            marks19 = submit(ans = ansq19, question ="19")
            diss.update({'marks19':marks19})
            # st.write(ansq20)
            marks20 = submit(ans = ansq20, question ="20")
            diss.update({'marks20':marks20})

            if bool(anssdic['ansq1']) and bool(anssdic['ansq2']) and bool(anssdic['ansq3']) and bool(anssdic['ansq4']) and bool(anssdic['ansq5']) and bool(anssdic['ansq6']) and bool(anssdic['ansq7']) and bool(anssdic['ansq8']) and bool(anssdic['ansq9']) and bool(anssdic['ansq10']) and bool(anssdic['ansq11']) and bool(anssdic['ansq12']) and bool(anssdic['ansq13']) and bool(anssdic['ansq14']) and bool(anssdic['ansq15']) and bool(anssdic['ansq16']) and bool(anssdic['ansq17']) and bool(anssdic['ansq18']) and bool(anssdic['ansq19']) and bool(anssdic['ansq20']) :
                conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="sih", port=3307)
                c = conn.cursor()
                query = 'INSERT INTO survey(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten,meleven,mtwelve,mthirteen, mfourteen,mfifteen,msixteen, mseventeen, meighteen,mnineteen,mtwenty) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,diss['marks1'],diss['marks2'],diss['marks3'],diss['marks4'],diss['marks5'],diss['marks6'],diss['marks7'],diss['marks8'],diss['marks9'],diss['marks10'],diss['marks11'],diss['marks12'],diss['marks13'],diss['marks14'],diss['marks15'],diss['marks16'],diss['marks17'],diss['marks18'],diss['marks19'],diss['marks20'])      
  
                #query = 'INSERT INTO quiz(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,dis['marks1'],dis['marks2'],dis['marks3'],dis['marks4'],dis['marks5'],dis['marks6'],dis['marks7'],dis['marks8'],dis['marks9'],dis['marks10'])
                c.execute(query)
                conn.commit()
        except KeyError:
             st.warning("Please Login")
            #  st.write("here")
        except MySQLdb.IntegrityError:
             st.warning("Already Submitted")
    
        except UnboundLocalError:
            st.warning("Please answer all questions")    
        
 #CREATE TABLE survey (pk int PRIMARY KEY,name varchar(100),mone int,mtwo int,mthree int,mfour int,mfive int ,msix int,mseven int,meight int,mnine int,mten int,meleven int,mtwelve int,mthirteen int , mfourteen int,mfifteen int,msixteen int, mseventeen int, meighteen int,mnineteen int,mtwenty int);
 #query = 'INSERT INTO survey(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten,meleven,mtwelve,mthirteen, mfourteen,mfifteen,msixteen, mseventeen, meighteen,mnineteen,mtwenty) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,diss['marks1'],diss['marks2'],diss['marks3'],diss['marks4'],diss['marks5'],diss['marks6'],diss['marks7'],diss['marks8'],diss['marks9'],diss['marks10'],diss['marks11'],diss['marks12'],diss['marks13'],diss['marks14'],diss['marks15'],diss['marks16'],diss['marks17'],diss['marks18'],diss['marks19'],diss['marks20'])      
    
    if st.button("Check your result", key='result'):
        
        try:
            with st.spinner(text ="DyslexiaML is Analyzing"):
                pred = prediction(user_prime_key = pk)
                if int(pred) == 2:
                    st.balloons()
                    # st.success("Your Child Does Not Has Dyslexia!! ")
                    st.success("Your Child is not a slow learner!!")
                elif int(pred) == 1:
                    st.success("Your Child Has Mild Symptoms of a slow learner. Consult Doctor ")
                    # st.success("Your Child Has Mild Dyslexia Symptoms. Consult Doctor ")
                else:
                    # st.success("Your Child Has Dyslexia Symptoms. Consult Doctor ")
                    st.success("Your Child Has Symptoms of a slow learner. Consult Doctor ")
        except UnboundLocalError:
            st.warning("Please Login")    
        
# import streamlit as st
# import MySQLdb
# from fetch import*
# from login import login_dict
# from login import name_dict
# from model import prediction

# def submit(ans=None, question=None):
#     marks = 0

#     if question in ["1", "2", "3", "4", "5", "6"]:
#         if ans == 'No-never':
#             marks = 4
#         elif ans == 'Sometimes':
#             marks = 2
#         else:
#             marks = 0
#     else:
#         if ans == 'No':
#             marks = 4
#         elif ans == 'Unknown':
#             marks = 2
#         else:
#             marks = 0

#     return marks

# def main():
#     st.title("SURVEY")

#     # Define the questions and options
#     questions = [
#         {
#             "question": "Did your child struggle to learn to count?",
#             "options": ['Yes-frequently', 'Sometimes', 'No-never']
#         },
#         {
#             "question": "Does he/she say numbers out of order — long after peers have mastered this skill?",
#             "options": ['Yes-frequently', 'Sometimes', 'No-never']
#         },
#         {
#             "question": "Does your child not seem to understand the connection between the symbol '4' and the word 'four?'",
#             "options": ['Yes-frequently', 'Sometimes', 'No -never']
#         },
#         {
#             "question": "Does your child struggle to connect the concept of numbers to real-world items?",
#             "options": ['Yes-frequently', 'Sometimes', 'No-never']
#         },
#         {
#             "question": "Does your child not seem to understand the difference between adding and subtracting?",
#             "options": ['Yes-frequently', 'Sometimes', 'No-never']
#         },
#         {
#             "question": "Does your child still count on his fingers past third grade?",
#             "options": ['Yes-frequently', 'Sometimes', 'No-never']
#         },
#         {
#             "question": "Difficulty sustaining attention; seems 'hyper' or 'daydreamer'",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Confused by letters, numbers, words, sequences, or verbal explanations.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Reads and rereads with little comprehension",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Difficulty putting thoughts into words; speaks in halting phrases; leaves sentences incomplete.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Can count, but has difficulty counting objects and dealing with money.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Memory for sequences, facts, and information that has not been experienced.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Complains of dizziness, headaches or stomach aches while reading.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Is reading extremely difficult? (Below grade or age level.)",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Is spelling ability poor? Letters missed, reversed etc?",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Is it difficult to rhyme words? (Not sure? Play a rhyming game with your child or student).",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Difficulty telling time on a clock with hands and/or tying shoes with laces?",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Difficulty finding the right words while speaking? Lots of ums, ahs, 'those things', and 'that stuff'.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Pauses, repeats or makes frequent mistakes when reading aloud.",
#             "options": ['Yes', 'No', 'Unknown']
#         },
#         {
#             "question": "Unusually high or low tolerance for pain.",
#             "options": ['Yes', 'No', 'Unknown']
#         }
#     ]

#     answers = {}

#     for i, q in enumerate(questions):
#         st.checkbox(f"Question {i+1}")
#         st.info(q["question"])
#         selected_option = st.radio(f"Answer:", q["options"])
#         answers[f"ansq{i+1}"] = selected_option

#     if st.button("Submit the quiz"):
#         try:
#             # Database connection
#             conn = MySQLdb.connect(host="localhost", user="your_db_user", passwd="your_db_password", db="your_db_name", port=3306)
#             c = conn.cursor()

#             # Insert data into the database
#             pk = "user_primary_key"  # Replace with the actual primary key
#             name = "user_name"  # Replace with the actual user name

#             # Extract the answers from the 'answers' dictionary
#             values = [pk, name] + [answers[f"ansq{i+1}"] for i in range(len(questions))]

#             # Create an INSERT query to insert data into your database table
#             query = """INSERT INTO survey(pk, name, mone, mtwo, mthree, mfour, mfive, msix, mseven, meight, mnine, mten,
#                                             meleven, mtwelve, mthirteen, mfourteen, mfifteen, msixteen, mseventeen, meighteen,
#                                             mnineteen, mtwenty)
#                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#             c.execute(query, values)
#             conn.commit()
#             st.success("Survey data submitted successfully!")

#         except Exception as e:
#             st.error(f"Error: {str(e)}")
    
#     if st.button("Check your result", key='result',value=True):
        
#         try:
#             with st.spinner(text ="DyslexiaML is Analyzing"):
#                 pred = prediction(user_prime_key = pk)
#                 if int(pred) == 2:
#                     st.balloons()
#                     st.success("Your Child Does Not Has Dyslexia!! ")
#                 elif int(pred) == 1:
#                     st.success("Your Child Has Mild Dyslexia Symptoms. Consult Doctor ")
#                 else:
#                     st.success("Your Child Has Dyslexia Symptoms. Consult Doctor ")
#         except UnboundLocalError:
#             st.warning("Please Login")  

# if __name__ == "__main__":
#     main()
