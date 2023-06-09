# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t67YsWod8xZROA5y5S2pNC9r1RHkCK--

Teacher end - To Add questions in CSV
"""

import pandas as pd
import sys
qstn=[]
op1=[]
op2=[]
op3=[]
op4=[]
crct_ans=[]
flg=1
#Specify number of qstion u are going to enter
n=int(input("Enter number of questions you want to add!"))
#n value should be greater than 0 if not exception will be catched and flag get raised
try:
  if(n<=0):
    print("Please enter valid value!")
    flg=0
    sys.exit()
except:
  print("Program exited")
for i in range(0,n):
  q=input("Enter your Question..")
  qstn.append(q)
  for j in range(1,5):
    o=input(f"Enter option {j}:")
    o=o.lower()
    if(j==1):
      op1.append(o)
    elif(j==2):
      op2.append(o)
    elif(j==3):
      op3.append(o)
    elif(j==4):
      op4.append(o)
    else:
      print("Some error in loop!")
  c_ans=input("Enter correct option value")
  c_ans=c_ans.lower()
  crct_ans.append(c_ans)
d={"Question":qstn,"Option1":op1,"Option2":op2,"Option3":op3,"Option4":op4,"Correct_answer":crct_ans}
df=pd.DataFrame(d)
df.to_csv("myquiz.csv",mode='a',index=False,header=False)
if flg:
  print("Question Added Successfully")



"""Student or User end who can take quiz!"""

import pandas as pd
import random as rd
f=pd.read_csv("/content/myquiz.csv")
#Find no of ques in CSV FILE
len_of_ds=len(f)
class userQuiz:
  def __init__(self):
    self.score=0
    self.flag=0
  def getQuiz(self,quiz_count):
    #get ques col from csv and convert to list
    qt=f['Questions'].tolist()
    #grouping 4 option col into options list 
    options=f.loc[:,['option1','option2','option3','option4']].values.tolist()
    rand_options=[]
    l=len(options)
    #get Correct answer col and convert to list
    crct_ans=f["Correct_answer"].tolist()
    quiz={}
    #Need to randomize option on each option list
    #using sample will randomize without repition i.e same option cannot occur twice
    for i in range(0,l):
      rand_options.append(rd.sample(options[i],k=4))
    #updating quiz by checking entered value
    #if less means it will work else Database error will flag
    if quiz_count<=l:
      for i in range(0,quiz_count):
        quiz.update({qt[i]:rand_options[i]})
    else:
      print("Database Error")
      print(f"No.of questions in Database:{l} \n Entered count is:{quiz_count}")
      self.flag=1
    #return bcz it is passed as argument to start quiz
    return quiz,crct_ans
  def startQuiz(self,quiz_ques,quiz_cr_ans):
    if self.flag==1:
      print("Session Terminated!!!")
      quit()
    option_li=['a','b','c','d']
    #combining question with qstion nmbr with option
    for qno,(qs,op) in enumerate(quiz_ques.items(),start=1):
      #print qstn no
      print(f'\n\nQuestion no :{qno}:')
      #print qstn 
      print(f'{qs}')
      #convert a,b,c,d with option list dict
      option_assignment=dict(zip(option_li,op))
      print()
      for key,value in option_assignment.items():
        print(f"{key}) {value}")
        #get user choice of option
      user_choice=input(f"Please enter options {[i for i in option_li]}")
      if user_choice in option_li:
        user_answer=option_assignment.get(user_choice)
        correct_ans=quiz_cr_ans[qno-1]
        #if equals score increase
        if(user_answer.strip().__eq__(correct_ans.strip())):
          self.score=self.score+1
          print("Well done!Correct Answer")
        else:
          print(f"OOPS! Wrong Answer{user_choice}){user_answer}\nCorrect answer is: {correct_ans}!!")
      else:
        print("INVALID CHOICE OPTION!! Please enter choices given!!")
        print("NOTE:If you enter option not in list then you will get 0 for that question.\n Please be carefull while respond")
        continue
  def getResult(self,n_ques):
    if self.flag==1:
      print("NO RESULTS TO SHOW!!")
      exit()
    p=self.score/n_ques*100
    print("#"*7,"RESULT","#"*7)
    if(p>90):
      print("\n\You Performed Really Great Outstanding!!")
      print(f"No.of Questions Correct:{self.score}")
      print(f"Percentage you got     :{p}")
      print("\n\nTHANK YOU FOR TAKING QUIZ USER!!!")
    elif(p>60) and (p<90):
      print("\nYou Performed Well!!")
      print(f"No.of Questions Correct:{self.score}")
      print(f"Percentage you got     :{p}")
      print("\nTHANK YOU FOR TAKING QUIZ USER!!!")
    elif(p>35) and (p<50):
      print("\nYou Need to Improve!!")
      print(f"No.of Questions Correct:{self.score}")
      print(f"Percentage you got     :{p}")
      print("\nTHANK YOU FOR TAKING QUIZ USER!!!")
    else:
      print("\nTASK FAILED!! Keep Practice Quiz...")
      print(f"No.of Questions Correct:{self.score}")
      print(f"Percentage you got     :{p}%")
      print("\nTHANK YOU FOR TAKING QUIZ USER!!!")
while(1):
  uch=input("Are you willing to Take Quiz...Type y|Y to take or n|N to quit ")
  if(uch=="y" or uch=="Y"):
    n=int(input("Enter number of questions you want to take quiz?"))
    #if gets executed only n is less than no of question in csv
    if n>len_of_ds:
      print(f"You're typing BIG NUMBER!.. We have small dataset which contains {len_of_ds} only dood!")
    o1=userQuiz()
    a=o1.getQuiz(n)
    b=o1.startQuiz(a[0],a[1])
    o1.getResult(n)
  elif(uch=="n" or uch=="N"):
    print("##USER SIGNING OFF##")
    print("Have a Good day!")
    break
  else:
    print("INVALID OPTION!!")
    print("Bye Bye")
    break