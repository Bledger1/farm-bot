from peewee import *

db = SqliteDatabase("root.db")

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
    vk_id = PrimaryKeyField(), #vk айди
    settlement = TextField(), #название поселение
    clan = TextField(null=True), #клан значение может быть пустым
    balance = AutoField(), #казна
    eat = AutoField() #еда
    residents = AutoField() #жители
    farmers = AutoField() #фермеры
    warrios = AutoField() #воины
    income = AutoField() #доход
    collecting = AutoField() #сбор
    сonsumption = AutoField() #потребление
    headquarters =AutoField() #штаб
    village = AutoField()#деревня
    garden = AutoField() #сад
    army = AutoField() #армия

if __name__ == '__main__':
    db.create_tables([User])
