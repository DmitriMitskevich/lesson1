# В вашей БД из предыдущего занятия удалите половину записей. А вторую половину измените.

import sqlite3
conn = sqlite3.connect("database.db")
with conn:
    curs = conn.cursor()
    list1 = """CREATE TABLE IF NOT EXISTS справочник_персоналий_участников_конференции(
    'Ф.И.О.' TEXT,
    'ученая степень' TEXT,
    'научное направление' TEXT,
    'место работы' TEXT,
    'кафедра' TEXT,
    'должность' TEXT,
    'страна' TEXT,
    'город' TEXT,
    'адрес' TEXT,
    'рабочий телефон' INTEGER,
    'электронная почта' TEXT
    );"""
    curs.execute(list1)
    conn.commit()

with conn:
    curs = conn.cursor()
    list2 = """INSERT INTO справочник_персоналий_участников_конференции VALUES(
    'Демчук Артур Леонович',
    'доцент',
    'экологическая политология',
    'МГУ им.М.В.Ломоносова',
    'сравнительная политология',
    'и.о. заведующего кафедрой сравнительной политологии факультета политологии ',
    'Россия',
    'Москва',
    'пр.Ломоносова д',
    '+7(495)9391000',
    'info_demch@rector.msu.ru'
    );"""
    curs.execute(list2)
    conn.commit()

list3 = """SELECT * FROM справочник_персоналий_участников_конференции WHERE "ученая степень" = "доцент" AND "город" = "Москва";"""
curs.execute(list3)
vyb = curs.fetchall()
print(vyb)

curs.execute("""UPDATE справочник_персоналий_участников_конференции SET "Ф.И.О." = "Королёв Виктор Степанович" WHERE "Ф.И.О." = "Демчук Артур Леонович";""")
curs.execute("""UPDATE справочник_персоналий_участников_конференции SET "ученая степень" = "доктор" WHERE "ученая степень" = "доцен";""")
curs.execute("""UPDATE справочник_персоналий_участников_конференции SET "место работы" = "БГУ" WHERE "место работы" = "МГУ им.М.В.Ломоносова";""")
curs.execute("""UPDATE справочник_персоналий_участников_конференции SET "должность" = "ректор" WHERE "должность" = "и.о. заведующего кафедрой сравнительной политологии факультета политологии";""")
curs.execute("""UPDATE справочник_персоналий_участников_конференции SET "город" = "Минск" WHERE "город" = "Москва";""")
conn.commit()

curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN 'научное направление';""")
curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN 'кафедра';""")
curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN "страна";""")
curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN "адрес";""")
curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN "рабочий телефон";""")
curs.execute("""ALTER TABLE справочник_персоналий_участников_конференции DROP COLUMN "электронная почта";""")
conn.commit()

a1 = curs.execute("""SELECT * FROM справочник_персоналий_участников_конференции""")
for i in a1:
    print(i)

with conn:
    attendee = """CREATE TABLE IF NOT EXISTS информация_связанная_с_участием_в_конференции(
    'докладчик или участник' TEXT, 
    'дата рассылки приглашения' INTEGER, 
    'дата поступления заявки' INTEGER, 
    'тема доклада' TEXT,
    'отметка о поступлении тезисов' TEXT, 
    'дата приезда' INTEGER, 
    'потребность в гостинице' TEXT, 
    'дата отъезда' INTEGER    
    );"""
    curs.execute(attendee)
    conn.commit()

with conn:
    attendee2 = """INSERT INTO информация_связанная_с_участием_в_конференции VALUES(
    'Демчук Артур Леонович',
    '10.03.2023',
    '15.03.2023',
    'Политика регулирования экологических конфликтов',
    '+',
    '02.04.2023',
    '+',
    '04.04.2023'
    );"""
    curs.execute(attendee2)
    conn.commit()

attendee3 = """SELECT "тема доклада" FROM информация_связанная_с_участием_в_конференции WHERE "докладчик или участник" LIKE 'Д%';"""
curs.execute(attendee3)
vyb2 = curs.fetchall()
print(vyb2)

curs.execute("""UPDATE информация_связанная_с_участием_в_конференции SET "докладчик или участник"="Королёв Виктор Степанович" WHERE "докладчик или участник"="Демчук Артур Леонович";""")
curs.execute("""UPDATE информация_связанная_с_участием_в_конференции SET "тема доклада"="Особенности принятия решений в конфликтных ситуациях" WHERE "тема доклада"="Политика регулирования экологических конфликтов";""")
curs.execute("""UPDATE информация_связанная_с_участием_в_конференции SET "потребность в гостинице"="-" WHERE "потребность в гостинице"="+";""")
conn.commit()

curs.execute("""ALTER TABLE информация_связанная_с_участием_в_конференции DROP COLUMN 'дата рассылки приглашения';""")
curs.execute("""ALTER TABLE информация_связанная_с_участием_в_конференции DROP COLUMN 'дата поступления заявки';""")
curs.execute("""ALTER TABLE информация_связанная_с_участием_в_конференции DROP COLUMN 'отметка о поступлении тезисов';""")
curs.execute("""ALTER TABLE информация_связанная_с_участием_в_конференции DROP COLUMN 'дата приезда';""")
curs.execute("""ALTER TABLE информация_связанная_с_участием_в_конференции DROP COLUMN 'дата отъезда';""")
conn.commit()

sk = curs.execute("""SELECT * FROM информация_связанная_с_участием_в_конференции""")
for i in sk:
    print(i)

with conn:
    info_conf = """CREATE TABLE IF NOT EXISTS информация_о_конференции(    
    'название конференции' TEXT,
    'дата проведения' INTEGER,
    'место проведения' TEXT,
    'организаторы' TEXT,
    'спонсоры' TEXT,
    'количество дней проведения конференции' INTEGER,
    'количество участников' INTEGER,
    'количество докладчиков' INTEGER    
    );"""
    curs.execute(info_conf)
    conn.commit()

with conn:
    info_conf2 = """INSERT INTO информация_о_конференции VALUES(
    'Управление экологическими конфликтами в современном мире',
    '03.04.2023-05.04.2023',
    'БГУ г.Минск',
    'ОТДЕЛЕНИЕ ГУМАНИТАРНЫХ НАУК И ИСКУССТВ НАЦИОНАЛЬНОЙ АКАДЕМИИ НАУК БЕЛАРУСИ ИНСТИТУТ ИСТОРИИ НАН БЕЛАРУСИ;
     РОССИЙСКОЕ ОБЩЕСТВО ПОЛИТОЛОГОВ',
    'НАН БЕЛАРУСИ; МОСКОВСКИЙ ДОМ НАЦИОНАЛЬНОСТЕЙ',
    4,
    56,
    33
    );"""
    curs.execute(info_conf2)
    conn.commit()

info_conf3 = """SELECT * FROM информация_о_конференции;"""
curs.execute(info_conf3)
vyb3 = curs.fetchall()
print(vyb3)

curs.execute("""UPDATE информация_о_конференции SET "название конференции"="Экологические конфликты: природа, виды, способы урегулирования" WHERE "название конференции"="Управление экологическими конфликтами в современном мире";""")
curs.execute("""UPDATE информация_о_конференции SET "дата проведения"="15.06.2023-20.06.2023" WHERE "дата проведения"="03.04.2023-05.04.2023";""")
curs.execute("""UPDATE информация_о_конференции SET "место проведения"="МГУ г.Москва" WHERE "место проведения"="БГУ г.Минск";""")
conn.commit()

curs.execute("""ALTER TABLE информация_о_конференции DROP COLUMN 'организаторы';""")
curs.execute("""ALTER TABLE информация_о_конференции DROP COLUMN 'спонсоры';""")
curs.execute("""ALTER TABLE информация_о_конференции DROP COLUMN 'количество дней проведения конференции';""")
curs.execute("""ALTER TABLE информация_о_конференции DROP COLUMN 'количество участников';""")
curs.execute("""ALTER TABLE информация_о_конференции DROP COLUMN 'количество докладчиков';""")
conn.commit()

sel = curs.execute("""SELECT * FROM информация_о_конференции""")
for i in sel:
    print(i)