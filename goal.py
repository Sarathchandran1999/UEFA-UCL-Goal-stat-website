from flask import Flask,render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route('/')
def display():
    db=py.Connect(host='localhost',user='root',password='',database='ucl')
    cur=db.cursor()
    sq1='select * from goal'
    cur.execute(sq1)
    data=cur.fetchall()
    return render_template('home.html',data=data)
    
@app.route('/about')
def about():
    return render_template('aboutus.html')
@app.route('/create')
def create():
    return render_template('record.html')
@app.route('/store',methods=['POST'])
def store():
    sl=request.form['Nos.']
    pl=request.form['Player']
    team=request.form['Team']
    ga=request.form['Goals']
    db=py.Connect(host='localhost',user='root',password='',database='ucl')
    cur=db.cursor()
    sq3='insert into goal(slno,player,team,goals) values({},"{}","{}",{})'.format(sl,pl,team,ga)
    cur.execute(sq3)
    db.commit()
    return redirect('/')

@app.route('/edit/<rid>')
def edit(rid):
    db=py.Connect(host='localhost',user='root',password='',database='ucl')
    cur=db.cursor()
    sq2="select * from goal where slno={}".format(rid)
    cur.execute(sq2)
    data=cur.fetchall()
    db.commit()
    return render_template('edit.html',data=data)
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    sl=request.form['Nos.']
    pl=request.form['Player']
    team=request.form['Team']
    ga=request.form['Goals']
    db=py.Connect(host='localhost',user='root',password='',database='ucl')
    cur=db.cursor()
    sq4="update goal set slno={},player='{}',team='{}',goals={} WHERE slno={}".format(sl,pl,team,ga,rid)
    cur.execute(sq4)
    db.commit()
    return redirect('/')

@app.route('/delete/<rid>')
def delete(rid):
    db=py.Connect(host='localhost',user='root',password='',database='ucl')
    cur=db.cursor()
    sq5="delete from goal where slno={}".format(rid)
    cur.execute(sq5)
    data=cur.fetchall()
    db.commit()
    return redirect('/')

app.run(debug=True)
