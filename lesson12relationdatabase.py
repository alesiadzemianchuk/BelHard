from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, Float
from sqlalchemy import select, insert, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///Car1.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    name = Column(String)



class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(String)
    brand = Column(Integer, ForeignKey('brands.id'))
    brand1 = relationship("Brand",back_populates="cars")


Brand.cars = relationship(Car, order_by=Car.id, back_populates="brand1")
Base.metadata.create_all(engine)


def Create():
    c2 = Brand(name=input('Введите наименование:'))
    session.add(c2)
    session.commit()
    print(f'Добавлена строка')


def Read():
    result2 = session.query(Brand).all()
    for i in result2:
        print("id: ", i.id, "Name: ", i.name)


def Update():
    result3 = session.query(Brand).update({Brand.name: "Auto " + Brand.name}, synchronize_session=False)
    session.commit()
    print('Обновление строки')


def Delete():
    result4 = session.query(Brand).filter(Brand.name == 'Autocitroen').delete()
    session.commit()
    print('Удаление строки')


def CreateCar():
    c1 = Car(model=input('Введите модель авто:'), release_year=input('Введите год выпуска: '), brand=input('Введите целое число, кот. соответствует бренду:'))
    session.add(c1)
    session.commit()
    print(f'Добавлена строка')

def ReadCar():
    result1 = session.query(Car).all()
    for i in result1:
        print("id: ", i.id, "Model: ", i.model, "Release_year: ", i.release_year, "Brand_id: ", i.brand)


def UpdateCar():
    result5 = session.query(Car).update({Car.model: "Auto " + Car.model}, synchronize_session=False)
    session.commit()
    print('Обновление строки')


def DeleteCar():
    result6 = session.query(Car).filter(Car.release_year < '1999').delete()
    session.commit()
    print('Удаление строки')


def Total1():
    result7 = session.query(Brand).join(Car).filter(Car.brand == 5).all()
    for i in result7:
        for cr in i.cars:
            print()
        print("id: ", i.id, "Name: ", i.name, "Model: ", cr.model, "Release_year: ", cr.release_year)


while True:
    choice = int(input(f'Введите номер \n1 для добавления строки в таблицу Brand,\n2 для демонстрации таблицы Brand,\n3 для изменения данных в таблице Brabd,\n4 для удаления данных из Brand'
                       f'\n11 для добавления строки в таблицу Car,\n12 для демонстрации таблицы Car,\n13 для изменения данных в таблице Car,\n14 для удаления данных из Car '
                       f'\n15 для вывода наименования и модели в одной таблице \nили \n0 для выхода:'))
    if choice == 0:
        break
    else:
        {1: Create, 2: Read, 3: Update, 4:Delete, 11: CreateCar, 12: ReadCar, 13: UpdateCar, 14: DeleteCar, 15: Total1}.get(choice)()


