from flask import Flask 
from models import db,Artisan,Product

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artisan.db'
db.init_app(app)

with app.app_context():
  db.create_all()

@app.route('/')
def home():
  return "Artisan Assist is running"

if __name__=='__main__':
  app.run(debug=True)
