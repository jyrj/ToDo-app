import sys
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://jyrj:1234@localhost:5432/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
#going to flask migrate

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description =db.Column(db.String(), nullable=False)
    completed =db.Column(db.Boolean(), nullable=False, default=False)
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

#db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error= False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description

    except:
        db.session.rollback()
        error= True
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify (body)

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))
    
@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html', 
    lists=Todo.query.all(),
    active_list=Todo.query.get(list_id),
    todos=Todo.query.filter_by(list_id=list_id).order_by('id').all())

@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))

if __name__=='__main__':
    app.run(debug=True)

    dfskjkj 
    srf kjshfjk 
     lsjf lj adj 
       
       
 
 