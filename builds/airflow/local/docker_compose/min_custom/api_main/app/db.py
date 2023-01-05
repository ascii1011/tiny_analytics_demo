from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up the database connection and model
engine = create_engine(os.environ["DATABASE_URL"])
Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

Base.metadata.create_all(engine)

# Create a session to manage database transactions
Session = sessionmaker(bind=engine)
session = Session()

# Add a user profile to the database
def add_user_profile(name, email):
    try:
        # Start a nested transaction
        with session.begin_nested():
            # Create a new user profile object
            user_profile = UserProfile(name=name, email=email)
            # Add the user profile to the session
            session.add(user_profile)
            # Commit the transaction
            session.commit()
    except Exception as e:
        # Roll back the transaction if an error occurs
        session.rollback()
        raise e

# Update a user profile in the database
def update_user_profile(id, name, email):
    try:
        # Start a nested transaction
        with session.begin_nested():
            # Update the user profile
            user_profile = session.query(UserProfile).filter_by(id=id).one()
            user_profile.name = name
            user_profile.email = email
            # Commit the transaction
            session.commit()
    except Exception as e:
        # Roll back the transaction if an error occurs
        session.rollback()
        raise e

# Delete a user profile from the database
def delete_user_profile(id):
    try:
        # Start a nested transaction
        with session.begin_nested():
            # Delete the user profile
            user_profile = session.query(UserProfile).filter_by(id=id).one()
            session.delete(user_profile)
            # Commit the transaction
            session.commit()
    except Exception as e:
        # Roll back the transaction if an error occurs
        session.rollback()
        raise
