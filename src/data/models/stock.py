from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.types import Boolean, Integer, String, DateTime, Float

from ..database import db
from ..mixins import CRUDModel

class Stock(CRUDModel):
    __tablename__ = 'stock'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    firma = Column(String(60), nullable=False, index=True)
    zkratka = Column(String(10), nullable=False, index=True)
    jmenovitaHodnota = Column(Float, nullable=False, index=False)
    posledni_cena = Column(Float, default=False)
    datum_insertu= Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def vypis_spolecny_radek():
        return db.session.query(Stock.firma,func.avg(Stock.posledni_cena).label("Prumerna_cena")).group_by("firma")
