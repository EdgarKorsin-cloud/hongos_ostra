from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class Siembra(Base):
    __tablename__ = "siembra"
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_type = Column(String)
    incubation_start_date = Column(String)
    incubation_end_date = Column(String)
    fructification_start = Column(String)


class Inventario(Base):
    __tablename__ = "inventario"
    id = Column(Integer, primary_key=True)
    anti_plagas = Column(Integer, default=0)
    anti_hongos = Column(Integer, default=0)
    booster = Column(Integer, default=0)
    atrapa_moscas = Column(Integer, default=0)
    sustrato = Column(Integer, default=0)
    micelio = Column(Integer, default=0)

engine = create_engine("sqlite:///siembra.db", echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


class Inventory_Manager:
    def __init__(self):
        self.session = Session()

        if not self.session.query(Inventario).first():
            self.session.add(Inventario())
            self.session.commit()

    def anadir_siembra(self, product, incubacion, product_type):
        nueva_siembra = Siembra(
            product_name=product,
            product_type=product_type,
            incubation_start_date=incubacion
        )
        self.session.add(nueva_siembra)
        self.session.commit()
        return True

    def get_supplies(self):
        inv = self.session.query(Inventario).first()
        return {
            "Anti-plagas": inv.anti_plagas,
            "Anti-hongos": inv.anti_hongos,
            "Booster": inv.booster,
            "Atrapa-moscas": inv.atrapa_moscas,
            "Sustrato": inv.sustrato,
            "Micelio": inv.micelio
        }

    def update_supplies(self, antiplagas, antihongos, booster, atrapamos, sustrato, micelio):
        inv = self.session.query(Inventario).first()
        inv.anti_plagas = antiplagas
        inv.anti_hongos = antihongos
        inv.booster = booster
        inv.atrapa_moscas = atrapamos
        inv.sustrato = sustrato
        inv.micelio = micelio
        self.session.commit()

    def update_dates(self, siembra_id, incubation_end, fructification_start):
        siembra = self.session.query(Siembra).filter_by(id=siembra_id).first()

        if siembra:
            siembra.incubation_end_date = incubation_end
            siembra.fructification_start = fructification_start
            self.session.commit()
            return True
        return False
