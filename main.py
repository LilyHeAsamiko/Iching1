# flask

from flask import Flask, render_template, request, session, redirect, url_for
from importlib import reload
import requests

from flask import Flask, render_template, request, session, redirect, url_for
from importlib import reload
import requests
import time
import sys
import re
import logging
import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler

def reject():
  print('It is not in the time for Recordıng!')

def repeat():
  print('You have recorded today!')

def CARD(card):   
  print('Welcome to extend the vocabulary!')
  card += 1
  return card

def W5uGe(digitNum):
  Num = int(digitNum)
  if len(digitNum) >1:
    Num = int(digitNum[0])
  if Num == 1 or Num == 2:
    W5uGe == 'Mu'
  elif Num == 3 or Num == 4:
    W5uGe == 'Shui'
  elif Num == 5 or Num == 6:
    W5uGe == 'Tu'
  elif Num == 7 or Num == 8:
    W5uGe == 'Jin'
  elif Num == 9 or Num == 0:
    W5uGe == 'Shui'
  else：
    assert(W5uGe<= 9, 'W5uGe is supposed to be one single digit number!')
  return W5uGe

def S3anCai(TianGC, RenGC, DiGC):
  Frst = W5uGe(int(TianGC))
  Scd = W5uGe(int(RenGC))
  Thrd = W5uGe(int(DiGC))
  S3anCai = [Frst, Scd, Thrd]
  return S3anCai

#创建flask duixiang
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'


def reject():
  print('It is not in the time for Recordıng!')

def repeat():
  print('You have recorded today!')

def CARD(card):   
  print('Welcome to extend the vocabulary!')
  card += 1
  return card

def get_stroke(c):
    # 如果返回 0, 则也是在unicode中不存在kTotalStrokes字段
    start = [13311,19968,63744,131072,173824,177984,178208,194995]
    end = [19893, 40917, 64045, 173782, 177972, 178205,183969, 194998]
    strokes_path = https://github.com/helmz/Corpus/blob/master/zh_dict/strokes.txt

    strokes = []
    with open(strokes_path, 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))

    unicode_ = ord(c)

    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        print("c should be a CJK char, or not have stroke in unihan data.")
        # can also return 0
        
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/w5ge3cai")
def w5ge3cai():
  kd = request.args.get("kd")
  print(kd)
  if len(kd) == 2:
    surname = kd[0]
    lastname = kd[1]
    TianG = int(surname) + 1
    RenG = int(surname) + int(lastname)
    DiG = int(lastname) + 1
    ZongG = int(surname) + int(lastname)
    WaiG =  2
  
  elif len(kd) == 3:
    surname = kd[0]
    middlename = kd[1]
    lastname = kd[2]
    TianG = int(surname) + 1
    RenG = int(surname) + int(lastname)
    DiG = int(lastname) + int(middlename)
    ZongG = int(surname) + int(middlename) + int(lastname)
    WaiG =  int(lastname) + 1
    
  elif len(kd) == 4:
    surname = int(kd[0])+int(kd[1])
    middlename = kd[2]
    lastname = kd[3]
    TianG = surname+1
    RenG = int(surname) + int(lastname)
    DiG = int(lastname) + int(middlename)
    ZongG = int(surname) + int(middlename) + int(lastname)
    WaiG =  int(lastname) + 1
    
  else:
    return('Wrong input!')
   
  if len(TianG) >1:
      TianGC = TianG[0]
  else:
      TianGC = TianG
  TianGCW = W5uGe(TianGC)
  if len(RenG) >1:
    RenGC = RenG[0]
  else:
    RenGC =RenG 
  RenGCW = W5uGe(RenGC)
  if len(DiG) >1:
    DiGC = DiG[0]
  else:
    DiGC =DiG  
  DiGCW = W5uGe(DiGC)
  if len(WaiG) >1:
    WaiGC = WaiG[0]
  else:
    WaiGC =WaiG  
  WaiGCW = W5uGe(WaiGC)
  if len(ZongG) >1:
    ZongC = ZongG[0]
  else:
    ZongGC =ZongG  
  ZongCW = W5uGe(ZongGC)
  W5uG = [TianGCW, RenGCW, DiGCW, WaiGCW, ZongCW]
  S3C = S3anCai(TianGC, RenGC, DiGC)
    return render_template("w5ge3cai.html",**{
  "kd": kd,
  "W5uG": W5uG,
  "S3C": S3C
})
    
@app.route("/meihuayishu")
def meihuayishu():  
  return render_template('meihuayishu.html')

def main():
  c1 = input('Hi, please input your surname: ')
  c01 = get_stroke(c1)
  c2 = input('Hi, please input your First name: ')
  c02 = get_stroke(c2)
  c3 = input('Hi, please input your Middle name: . If none just input 0')
  c03 = get_stroke(c3)
  t0 = time.time()
  loct = time.localtime(t0)
  card = 0
  if (loct.tm_hour == 0 and loct.tm_min == 0 and   loct.tm_sec == 0):
    card = 0
  if card == 0:
    sched = BlockingScheduler()
    sched.add_job(func = CARD, trigger = 'cron', month = '*', day = '*', hour = '8', minute = '*', args=[card])
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '0-7', minute = '*')
    sched.add_job(func = reject, trigger = 'cron', month = '*', day = '*', hour = '9-23', minute = '*')
    card += 1
  if card > 0:  
    repeat()
