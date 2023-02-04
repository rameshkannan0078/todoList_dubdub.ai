from flask import Flask,render_template,request,redirect
import sqlite3
import os
app = Flask(__name__)

conn = sqlite3.connect('todolist.db',check_same_thread=False)



@app.route("/",methods=['GET'])
def hello():
    posts = conn.execute('SELECT * FROM listitems').fetchall()
    print(posts)
    return render_template('index.html', posts=posts)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':
    addTodo = request.form['addTodo']
    try:
        cur=conn.cursor()
        cur.execute("Insert into listitems(items,marked) values (?,?)",[addTodo,""])
        conn.commit()
 
        msg = "Record successfully added"
    except Exception as e :
        conn.rollback()
        print(e)
        msg = "error in insert operation"
      
    finally:
         print(msg)
         return redirect('/')


@app.route('/delete/<int:id>')
def delete_task(id):
    conn.execute('Delete from listitems where id=?',[id])
    conn.commit()
    return redirect('/')


@app.route('/updateMark/<int:id>')
def updateMark_task(id):
    conn.execute('update listitems set marked=True  where id=?',[id])
    conn.commit()
    return redirect('/')

@app.route('/RemoveMark/<int:id>')
def RemoveMark_task(id):
    conn.execute('update listitems set marked=?  where id=?',['',id])
    conn.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update_todo(id):
    todo = request.form['updateTodo']
    conn.execute("UPDATE listitems SET items =? WHERE id = ?", (todo, id))
    conn.commit()
    return redirect('/')

 
if __name__ == "__main__":
   port = int(os.environ.get('PORT', 5000))
   app.run(debug=True, host='0.0.0.0', port=port)
