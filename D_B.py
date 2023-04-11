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
