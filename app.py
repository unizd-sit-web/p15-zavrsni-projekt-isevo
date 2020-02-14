from flask import Flask, redirect, url_for, render_template, request,abort
import webbrowser
from random import randrange
from flask_sqlalchemy import SQLAlchemy
import sqlite3  
from flask import *

app=Flask(__name__)




@app.route("/")
def index():
   author="YELLOWSTONE"
   return render_template("index.html",author=author)

@app.route("/about/")
def about():
   return render_template("about.html")




#dodavanje korisnika u bazu
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"] 
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email) values (?,?)",(name,email))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the user to the list"  
        finally:  
            return render_template("result.html",msg=msg)  
            con.close()   





#ispis korisnika iz baze
@app.route("/register")
def register(): 
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("register.html",rows = rows)   







@app.route("/login")
def login():
   return render_template("login.html")    



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

#metoda za provjeru tocnih odgovora za quizFilm.html
def guessMovie():
   brojac=0
   niz=[""]*5
   if request.form["tipe1"]=="a":
      brojac=brojac+1
      niz[0]="a"
   if request.form["tipe2"]=="d":
      brojac=brojac+1
      niz[1]="d"
   if request.form["tipe3"]=="a":
      brojac=brojac+1
      niz[2]="a"
   if request.form["tipe4"]=="c":
      brojac=brojac+1
      niz[3]="b"
   if request.form["tipe5"]=="c":
      brojac=brojac+1
      niz[4]="d"
  
   return brojac




@app.route("/quizFilm",methods = ["POST", "GET"])
def quizFilm():
   
   if request.method=='POST':
      brojac=guessMovie()
      if brojac>0 and brojac==4:
         poruka="And the oscar goes to you.You are an expert in movies"
      else:
         poruka="Meh.Refresh your memories!"


      return render_template("quizFilm.html",poruka=poruka)    
   else:
      return render_template("quizFilm.html")





@app.route("/quizCartoon",methods = ["POST", "GET"])
def quizCartton():
   if request.method=='POST':
      #spremanje i prebrojavanje odgovora za quizCartoon.html
      niz_tocnih_odgovora=[0]*7
      odgovor1=request.form["tipe1"]   
      odgovor2=request.form["tipe2"]
      odgovor3=request.form["tipe3"]
      odgovor4=request.form["tipe4"]
      odgovor5=request.form["tipe5"]
      odgovor6=request.form["tipe6"]
      odgovor7=request.form["tipe7"]
      
      if odgovor1=="b":
            niz_tocnih_odgovora[0]=1
      if odgovor2=="a":
            niz_tocnih_odgovora[1]=1
      if odgovor3=="a":
            niz_tocnih_odgovora[2]=1
      if odgovor4=="a":
            niz_tocnih_odgovora[3]=1
      if odgovor5=="b":
            niz_tocnih_odgovora[4]=1
      if odgovor6=="c":
            niz_tocnih_odgovora[5]=1
      if odgovor7=="c":
            niz_tocnih_odgovora[6]=1
       
      brojac_0=brojac_1=0


      for i in range (len(niz_tocnih_odgovora)):
         if niz_tocnih_odgovora[i]!=0:
            brojac_1=brojac_1+1
         else:
            brojac_0=brojac_0+1
   
      message=""
      print(niz_tocnih_odgovora)
      print("broj tocnih",brojac_1)
      print("broj krivih",brojac_0)
      if brojac_0<brojac_1 and brojac_1==7:
         message="Excellent"
      elif brojac_0 <brojac_1 and brojac_1<7:
         message="MEH!  You can do better! You have",brojac_1,"correct answers"
      else:
         message="You shoud refresh memories!"

      #ispis poruke     
      return render_template("quizCartoon.html",message=message)    
   else:
      return render_template("quizCartoon.html")
 

#spremanje odgovora za HarryPotter.html
def answersHogwarts():
   niz=[""]*8
   if request.form["tipe1"]=="a":
      niz[1]="a"
   elif request.form["tipe1"]=="b":
      niz[1]="b"
   elif request.form["tipe1"]=="c":
      niz[1]="c"
   elif request.form["tipe1"]=="d":
      niz[1]="d"
   if request.form["tipe2"]=="a":
      niz[2]="a"
   elif request.form["tipe2"]=="b":
      niz[2]="b"
   elif request.form["tipe2"]=="c":
         niz[2]="c"
   elif request.form["tipe2"]=="d":
         niz[2]="d"
   if request.form["tipe3"]=="a":
         niz[3]="a"
   elif request.form["tipe3"]=="b":
         niz[3]="b"
   elif request.form["tipe3"]=="c":
         niz[3]="c"
   elif request.form["tipe3"]=="d":
         niz[3]="d"
   if request.form["tipe4"]=="a":
         niz[4]="a"
   elif request.form["tipe4"]=="b":
         niz[4]="b"
   elif request.form["tipe4"]=="c":
         niz[4]="c"
   elif request.form["tipe4"]=="d":
         niz[4]="d"
   if request.form["tipe5"]=="a":
         niz[5]="a"
   elif request.form["tipe5"]=="b":
         niz[5]="b"
   elif request.form["tipe5"]=="c":
         niz[5]="c"
   elif request.form["tipe5"]=="d":
         niz[5]="d"
   if request.form["tipe6"]=="a":
         niz[6]="a"
   elif request.form["tipe6"]=="b":
         niz[6]="b"
   elif request.form["tipe6"]=="c":
         niz[6]="c"
   elif request.form["tipe6"]=="d":
         niz[6]="d"
   if request.form["tipe7"]=="a":
         niz[7]="a"
   elif request.form["tipe7"]=="b":
         niz[7]="b"
   elif request.form["tipe7"]=="c":
         niz[7]="c"
   elif request.form["tipe7"]=="d":
         niz[7]="d"
   return niz

#brojanje odgovora
def counting(niz):
   br1=br2=br3=br4=0
   for i in range (len(niz)):
      if niz[i]=="a":
         br1=br1+1
      elif niz[i]=="b":
         br2=br2+1
      elif niz[i]=="c":
         br3=br3+1
      else:
         br4=br4+1

      if br1>br2 and br1>br4 and br1>br4:
         poruka="Griffyndor"
      elif br2>br1 and br2>br3 and br2>br4:
         poruka="Hupplepuff"
      elif br3>br1 and br3>br2 and br3>br4:
         poruka="Ravenclaw"
      elif br4>br1 and br4>br2 and br4>br3:
         poruka="Slytherin"

   return poruka

@app.route("/HarryPotter.html",methods = ["POST", "GET"])
def marvelVSdc():
   if request.method=='POST':
      niz= answersHogwarts()
      message=counting(niz)
      print(message)
      return render_template("HarryPotter.html",message=message)    
   else:
      return render_template("HarryPotter.html")







if __name__ == "__main__":
   app.run(debug=True)


       
