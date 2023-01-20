from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__all__ = ["TapdCN"]

# Set up the database connection and model
engine = create_engine('postgresql://tapd:tapd@postgres/tapd')
Base = declarative_base()
class Domain(Base):
    __tablename__ = 'tapd'
    id = Column(Integer, primary_key=True)
    ref_domain_id = Column(Integer)
    domain = Column(String)
    state = Column(Integer)

class TapdCN():

    def __init__(self):

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_domain(self, ref_domain_id, domain, state):
        try:
            with self.session.begin_nested():
                _domain = Domain(ref_domain_id=ref_domain_id, domain=domain, state=state)
                self.session.add(_domain)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def update_domain(self, id, state):
        try:
            with self.session.begin_nested():
                _domain = self.session.query(Domain).filter_by(id=id).one()
                _domain.state = state
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    def delete_domain(self, id):
        try:
            with self.session.begin_nested():
                _domain = self.session.query(Domain).filter_by(id=id).one()
                self.session.delete(_domain)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise
