import streamlit as st
from fetch import*
# import SessionState
from login import login_dict
from login import name_dict
import MySQLdb
from pymysql import *
from pymysql import cursors
import os



def submit(ans =None, question =None):
    marks= 0
    if question =="1":
        if ans =='Yes':
            marks = 4
        else:
            marks = 0
            
    
    elif question =="2":
        if ans == 'Grapes':
            marks = 4
        else:
            marks=0
               
    if question =="3":
        if ans =='No':
            marks=4
        else:
            marks =0
    
    elif question =="4":
        if ans == "The First Letter":
            marks =4
        else:
            marks =0
    
    if question =="5":
        if ans =="C":
            marks=4
        else:
            marks=0
    
    elif question =="6":
        if ans == "b":
            marks = 4
        else:
            marks=0
    
    
    if question =="7":
        if ans =="ED":
            marks=4
        else:
            marks=0
    
    elif question =="8":
        if ans =="DOG":
            marks=4
        else:
            marks=0
    
    
    
    if question =="9":
        if ans == "First one is left and next one is right":
            marks=4
        else:
            marks=0
			
    
    elif question =="10":
        if ans == "cake":
            marks=4
        else:
            marks=0
    
    return marks



dis = {}
    
def main():
    
    ansdic={}
    
    front_up()
    st.title("QUIZ")
    #st.write('User Logged in',name_dict.values())
    try:
        st.write('User Logged in as',name_dict['name'])
        pk = login_dict["key"]
        na = name_dict['name']
        #st.write("primary key" ,pk)
        st.write("name " ,na)
    except:
        st.error(" Please Log in")
    
    if st.checkbox('Question I', key ='q1', value=True):
        st.info("Check whether these two alphabets  are same or not?")
        st.image(image = 'pages/SIH_assets/1_1.png',width=100)
        st.image(image = 'pages/SIH_assets/1_2.png', width=100)
        
        ansq1 = st.radio("Answer:", ['Yes','No'], key ='q1_radio')
        ansdic['ansq1'] =ansq1
        # if st.button("SUBMIT", key='q1_submit'):
        #     st.write(ansq1)
        #     marks1 = submit(ans = ansq1, question ="1")
        #     dis.update({'marks1':marks1})
         
    
    if st.checkbox('Question II', key ='q2', value=True):
        st.info("Guess the fruit in the picture. ")
        st.image(image = 'pages/SIH_assets/2.png',width=100)
        
        ansq2 = st.radio("Answer:", ['Orange','Banana','Grapes','Mango'], key ='q2_radio')
        ansdic['ansq2'] =ansq2
        # if st.button("SUBMIT", key='q2_submit'):
        #     marks2 =submit(ans = ansq2, question ="2")
        #     dis.update({'marks2':marks2})
            #st.write(dis)
            #st.write(ansdic)
            
    if st.checkbox('Question III', key ='q3', value=True):
        st.info("Check whether these two alphabets  are same or not?")
        st.image(image = 'pages/SIH_assets/3_1.png',width=100)
        st.image(image = 'pages/SIH_assets/3_2.png',width=100)
        
        
        ansq3 = st.radio("Answer:", ['Yes','No'], key = 'q3_radio')
        ansdic['ansq3'] =ansq3
        # if st.button("SUBMIT", key='q3_submit'):
        #     st.write(ansq3)
        #     marks3=submit(ans = ansq3, question ="3")
        #     dis.update({'marks3':marks3})
            #st.write(ansq3)
            #st.write(dis)
            
    
    if st.checkbox('Question IV', key ='q4', value=True):
        st.info("Which letter is G?")
        st.image(image = 'pages/SIH_assets/4_1.png',width=100)
        st.image(image = 'pages/SIH_assets/4_2.png',width=100)
        
        
        ansq4 = st.radio("Answer,from left to right:", ['The First Letter','The Second Letter'], key = 'q4_radio')
        ansdic['ansq4'] =ansq4
        # if st.button("SUBMIT", key='q4_submit'):
        #     st.write(ansq4)
        #     marks4 = submit(ans = ansq4, question ="4")
        #     dis.update({'marks4':marks4})
        #     #st.write(dis)
            #st.write(dis)
            
    if st.checkbox('Question V', key ='q5', value=True):
        st.info("Which letter CAT starts with?")
        # st.image(image = 'pages/SIH_assets/5_1.png',width=100)
        # st.image(image = 'pages/SIH_assets/5_2.png',width=100)
        
        
        ansq5 = st.radio("Answer:", ['F','C','A','T'], key = 'q5_radio')
        ansdic['ansq5'] =ansq5
        # if st.button("SUBMIT", key='q5_submit'):
        #     st.write(ansq5)
        #     marks5 = submit(ans = ansq5, question ="5")
        #     dis.update({'marks5':marks5})
            
    
    if st.checkbox('Question VI', key ='q6',value=True):
        st.info("What is the smaller version of this letter?")
        st.image(image = 'pages/SIH_assets/6_1.png',width=100)
        # st.image(image = 'https://github.com/dyslexiaworkin/artgallery/blob/master/C.png?raw=true',width=100)
        
        
        ansq6 = st.radio("Answer:", ['c','b'], key = 'q6_radio')
        ansdic['ansq6'] =ansq6
        # if st.button("SUBMIT", key='q6_submit'):
        #     st.write(ansq6)
            
        #     marks6 = submit(ans = ansq6, question ="6")
        #     dis.update({'marks6':marks6})
            
            #st.write(dis)
            
    
    if st.checkbox('Question VII', key ='q7',value=True):
        st.info("What do you hear?")
        st.audio(data = 'pages/SIH_assets/7.mpeg')	
        
        ansq7 = st.radio("Answer:", ['AB','ED'], key = 'q7_radio')
        ansdic['ansq7'] =ansq7
        # if st.button("SUBMIT", key='q7_submit'):
        #     st.write(ansq7)
        #     marks7 = submit(ans = ansq7, question ="7")
        #     dis.update({'marks7':marks7})
            
    
    if st.checkbox('Question VIII', key ='q8',value=True):
        st.info("What do you see in the picture?")
        st.image(image = 'pages/SIH_assets/8.png',width=100)
        
        ansq8 = st.radio("Answer:", ['GOD','DOG'], key = 'q8_radio')
        ansdic['ansq8'] =ansq8
        # if st.button("SUBMIT", key='q8_submit'):
        #     st.write(ansq8)
        #     marks8 = submit(ans = ansq8, question ="8")
        #     dis.update({'marks8':marks8})
            
    
    if st.checkbox('Question IX', key ='q9',value=True):
        st.info("Which hand is left and Which hand is right?")
        st.image(image = 'pages/SIH_assets/9.png',width=100)
        
        ansq9 = st.radio("Answer:", ['First one is right and next one is left','First one is left and next one is right'], key = 'q9_radio')
        ansdic['ansq9'] =ansq9
        # if st.button("SUBMIT", key='q9_submit'):
        #     st.write(ansq9)
        #     marks9 = submit(ans = ansq9, question ="9")
        #     dis.update({'marks9':marks9})
            #st.write(dis)
    
    if st.checkbox('Question X', key ='q10',value=True):
        st.info("What do you hear?")
        st.audio(data = 'pages/SIH_assets/10.mpeg')	
        
        ansq10 = st.radio("Answer:", ['cake','lake','take','fake'], key = 'q10_radio')
        ansdic['ansq10'] =ansq10
        # if st.button("SUBMIT", key='q10_submit'):
        #     st.write(ansq10)
        #     marks10 = submit(ans = ansq10, question ="10")
        #     dis.update({'marks10':marks10})
        #     st.write("Your Answers",ansdic)
            
    
    
    if st.button("Submit the quiz", key='submit'):
        #st.write("hello")
        try:
            # st.write(ansq1)
            marks1 = submit(ans = ansq1, question ="1")
            dis.update({'marks1':marks1})
            # st.write(ansq1)
            marks2 = submit(ans = ansq2, question ="2")
            dis.update({'marks2':marks2})
            # st.write(ansq2)
            marks3 = submit(ans = ansq3, question ="3")
            dis.update({'marks3':marks3})
            # st.write(ansq3)
            marks4 = submit(ans = ansq4, question ="4")
            dis.update({'marks4':marks4})
            # st.write(ansq4)
            marks5 = submit(ans = ansq5, question ="5")
            dis.update({'marks5':marks5})
            # st.write(ansq5)
            marks6 = submit(ans = ansq6, question ="6")
            dis.update({'marks6':marks6})
            # st.write(ansq6)
            marks7 = submit(ans = ansq7, question ="7")
            dis.update({'marks7':marks7})
            # st.write(ansq7)
            marks8 = submit(ans = ansq8, question ="8")
            dis.update({'marks8':marks8})
            # st.write(ansq8)
            marks9 = submit(ans = ansq9, question ="9")
            dis.update({'marks9':marks9})
            # st.write(ansq9)
            marks10 = submit(ans = ansq10, question ="10")
            dis.update({'marks10':marks10})
            #st.write(bool(ansdic['ansq1']))
            #st.write(dis['marks1'])
            #st.write(dis.keys())
            #st.write(ansdic.keys())
            #st.write("hello3")
            if bool(ansdic['ansq1']) and bool(ansdic['ansq2']) and bool(ansdic['ansq3']) and bool(ansdic['ansq4']) and bool(ansdic['ansq5']) and bool(ansdic['ansq6']) and bool(ansdic['ansq7']) and bool(ansdic['ansq8']) and bool(ansdic['ansq9']) and bool(ansdic['ansq10']) :
                #st.write("hello4")
                conn = MySQLdb.connect(host="localhost", user="root", passwd="password", db="sih", port=3307)
                c = conn.cursor()
                
                query = 'INSERT INTO quiz(pk,name,mone,mtwo,mthree,mfour,mfive,msix,mseven,meight,mnine,mten) VALUES ("%s", "%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (pk,na,dis['marks1'],dis['marks2'],dis['marks3'],dis['marks4'],dis['marks5'],dis['marks6'],dis['marks7'],dis['marks8'],dis['marks9'],dis['marks10'])
                c.execute(query)
                conn.commit()
                #table stiil to be created by shell
        except MySQLdb.IntegrityError:
             st.warning("Already Submitted")
        except:
            st.warning("Please answer all questions")
            
# CREATE TABLE quiz (pk int PRIMARY KEY,name varchar(100),mone int,mtwo int,mthree int,mfour int,mfive int ,msix int,mseven int,meight int,mnine int,mten int);
