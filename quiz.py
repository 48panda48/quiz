import os
url="https://raw.githubusercontent.com/48panda48/quiz/master/version.txt"
import requests
response = requests.get(url).text
if str(response)!="0.9\nn":
    print("Update Available.")
    print(response)
    import webbrowser
    webbrowser.open('https://www.github.com/48panda48/quiz')
    import sys
    sys.exit()
from datetime import datetime
def get_time():
    now = datetime.now()
    return(now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
print("Choose Your Quiz")
quizes=[]
for file in os.listdir(os.getcwd()):
    if file.endswith(".qz"):
        print(file[:-3])
        quizes.append(file[:-3])
awnser = ""
while not awnser in quizes:
    awnser=input("Which Quiz?\n")

with open(awnser+".qz") as f:
    file=f.read().splitlines()
options={"in order":False,"repeat":False}
questions=file
timed=False
if file[0][2:8]=="option":
    for line in file[1:int(file[0][0])+1]:
        if line == "in order":
            options["in order"]=True
        if line =="repeat wrong at end":
            options["repeat"]=True
        if line[:5] =="timed":
            timed=True
            max_time=int(line[6:])
    questions=file[int(file[0][0])+1:]
if not options["in order"]:
    import random
score=0
amount=len(questions)
if timed:
    import time
    print(f"This quiz is timed. you have {time.strftime('%M:%S', time.gmtime(max_time))} To Complete the Quiz.\n Your time start in:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO")
    start_time=get_time()
while len(questions)!=0:
    if not options["in order"]:
        nextq=random.choice(questions)
    else:
        nextq=questions[0]
    q,a=nextq.split("\t")
    right=False
    if input(q).lower()==a.lower():
        score+=1
        right=True
    elif options["repeat"]:
        questions.remove(nextq)
        questions.append(nextq)
    if not options["repeat"] or right:
        questions.remove(nextq)
    if timed:
        if get_time()-start_time>max_time:
            print("Time up!!")
            break
        elif len(questions)==0:
            print(f"You finished with {time.strftime('%M:%S', time.gmtime(max_time-(get_time()-start_time)))} Left!!")
if not options["repeat"] or timed:
    print(f"You got {score} out of {amount}!!")
import time
time.sleep(5)
