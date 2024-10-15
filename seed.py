from app import db
from models import User, Task
from werkzeug.security import generate_password_hash

def seed_db():
    db.create_all()
    user1 = User(username="user1", password=generate_password_hash("password1", method='sha256'))
    db.session.add(user1)
    task1 = Task(title="Buy groceries", user_id=1)
    task2 = Task(title="Read a book", user_id=1)
    db.session.add(task1)
    db.session.add(task2)
    db.session.commit()

if __name__ == "__main__":
    seed_db()