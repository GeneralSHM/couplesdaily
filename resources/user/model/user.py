from flask_sqlalchemy import SQLAlchemy

mysql = SQLAlchemy()


class User(mysql.Model):
    __tablename__ = 'user'
    id = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.Text, nullable=False)
    username = mysql.Column(mysql.String, nullable=False)