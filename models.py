from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Artisan(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(100), nullable=False)
  craft=db.Column(db.String(100))
  story=db.Column(db.Text)
  photo_path=db.Column(db.String(200))
  share_photo=db.Column(db.Boolean, default=False)

  products=db.relationship('Product', backref='artisan', lazy=True)

class Product(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  artisan_id=db.Column(db.Integer, db.ForeignKey('artisan.id'), nullable=False)
  category=db.Column(db.String(50))
  spoken_text=db.Column(db.Text)
  details=db.Column(db.Text)
  description=db.Column(db.Text)
  