from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, Float
from sqlalchemy import select, insert, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine('sqlite:///Car.db', echo=True)
Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(Base):
    __tablename__ = 'car'

    model = Column(String)
    release_year = Column(String)
    brand = Column(String, ForeignKey('brand.id'))






#conn = engine.connect()

# brand = Table(
#     'product', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('price', Float),
#     Column('quantity', Integer),
#     Column('comments', String)
# )

Base.metadata.create_all(engine)


def Create():
    ins = product.insert().values(name=input('Введите наименование:'), price=float(input('Введите цену:')),
                                  quantity=int(input('Введите количество:')), comments=input('Введите комментарий:'))
    result1 = conn.execute(ins)
    print(f'Добавлена строка')



def Read():
    read = product.select()
    result2 = conn.execute(read)
    for i in result2:
        print(i)


def Update():
    priceold = float(input('Введите цену для изменения'))
    pricenew = float(input('Введите новую цену'))
    up = product.update().where(product.c.price == priceold).values(price=pricenew)
    result3 = conn.execute(up)
    print('Обновление строки')


def Delete():
    name2 = input('Введите продукт для удаления')
    del1 = product.delete().where(product.c.name == name2)
    result4 = conn.execute(del1)
    print('Удаление строки')



while True:
    choice = int(input(f'Введите номер \n1 для добавления строки в таблицу,\n2 для демонстрации таблицы,\n3 для изменения данных в таблице,\n4 для удаления данных \nили \n0 для выхода:'))
    if choice == 0:
        break
    else:
        {1: Create, 2: Read, 3: Update, 4: Delete}.get(choice)()


