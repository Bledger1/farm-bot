from peewee import *

db = SqliteDatabase("root.db")

class BaseModel(Model):

    class Meta:
        database = db
        
class User(BaseModel):
    vk_id = IntegerField(primary_key=True) #vk айди
    settlement = TextField() #название поселение
    clan =  TextField(null=True) #клан значение может быть пустым
    balance = IntegerField(default=0) #казна
    eat = IntegerField(default=0) #еда
    residents = IntegerField(default=0) #жители
    farmers = IntegerField(default=0) #фермеры
    warrios = IntegerField(default=0) #воины
    income = IntegerField(default=0) #доход
    collecting = IntegerField(default=0) #сбор
    сonsumption = IntegerField(default=0) #потребление
    headquarters =IntegerField(default=0) #штаб
    village = IntegerField(default=0)#деревня
    garden = IntegerField(default=0) #сад
    army = IntegerField(default=0) #армия

class Clan(BaseModel):
    clan_name = TextField(User2, primary_key=True)
    members = CharField()

if __name__ == '__main__':
    db.create_tables([User, Clan])
