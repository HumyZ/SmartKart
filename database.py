from flask_sqlalchemy import SQLAlchemy

from flask_user import UserMixin

db = SQLAlchemy()

# Define the User data-model.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email = db.Column(db.String(1000), nullable=False, unique=True)
    password = db.Column(db.LargeBinary(1000), nullable=False)
    last_login = db.Column(db.DateTime())

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class Item(db.Model):
    __tablename__ = 'items'
    item_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    brand = db.Column(db.String(1000), nullable=False)
    item_name = db.Column(db.String(1000), nullable=False)
    item_price = db.Column(db.Float(), nullable=False)
    item_category = db.Column(db.String(1000), nullable=False)
    store = db.Column(db.String(1000), nullable=False)
    url = db.Column(db.String(1000))

convertToDict = lambda r: {c.name: getattr(r, c.name) for c in r.__table__.columns}
