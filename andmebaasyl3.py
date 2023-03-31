import sqlite3

def lisaandmed():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    first_name = input('Sisesta eesnimi: ')
    last_name = input('Sisesta perenimi: ')
    email = input('Sisesta e-posti aadress: ')
    car_make = input('Sisesta auto mark: ')
    car_year = int(input('Sisesta auto tootmisaasta: '))
    car_price = float(input('Sisesta auto hind: '))
    c.execute('INSERT INTO sinukasutaja (first_name, last_name, email, car_make, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?)', 
              (first_name, last_name, email, car_make, car_year, car_price))
    conn.commit()
    print('Andmed lisatud')
    conn.close()

def vanemad_sinukasutaja():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sinukasutaja WHERE car_year < 2000 ORDER BY car_year ASC')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def keskmine_aasta_kalleim_hind():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    c.execute('SELECT AVG(car_year), MAX(car_price) FROM sinukasutaja')
    result = c.fetchone()
    print('Keskmine autode aasta:', result[0])
    print('Kõige kallim hind:', result[1])
    conn.close()

def uuemadautod():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    c.execute('SELECT car_make, car_year FROM sinukasutaja ORDER BY car_year DESC LIMIT 5')
    rows = c.fetchall()
    print('Uuemad 5 autot on:')
    for row in rows:
        print(row[0], row[1])
    conn.close()

def kallimadautod():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    c.execute('SELECT car_make, car_year FROM sinukasutaja ORDER BY last_name DESC LIMIT 5;')
    rows = c.fetchall()
    print('Kallimad 5 autot on:')
    for row in rows:
        print(row[0], row[1])
    conn.close()

def idkustutamine():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    idkustuta = input('Sisesta kustutatava andme ID: ')
    c.execute('DELETE FROM sinukasutaja WHERE id = ?', (idkustuta,))
    conn.commit()
    print('Andmed kustutatud')
    conn.close()

def diskrimineerimine():
    conn = sqlite3.connect('epood_llaanesoo.db')
    c = conn.cursor()
    sisend = input("Sisesta aasta mille järgi rida kustutada:")
    sisend2 = input("Sisesta mark mille järgi rida kustutada:")
    c.execute('DELETE FROM sinukasutaja WHERE car_year = ?', (sisend,))
    c.execute('DELETE FROM sinukasutaja WHERE car_make = ?', (sisend2,))
    if c.rowcount == 0:
        print("Andmeid ei leitud")
    else:
        conn.commit()
        print("Andmed kustutatud")
    conn.close()

def menu():
    while True:
        print('1. Andmete lisamine')
        print('2. Vanemad autod')
        print('3. Keskmine aasta ja kõige kallim hind')
        print('4. Uuemad automargid')
        print('5. Kallimad autod')
        print('6  Kustuta rida id järgi')
        print('7  Diskrimineerimine')
        print('8. Väljumine')
        choice = input('Valige toiming: ')
        if choice == '1':
            lisaandmed()
        elif choice == '2':
            vanemad_sinukasutaja()
        elif choice == '3':
            keskmine_aasta_kalleim_hind()
        elif choice == '4':
            uuemadautod()
        elif choice == '5':
            kallimadautod()
        elif choice == '6':
            idkustutamine()
        elif choice == '7':
            diskrimineerimine()
        elif choice == '8':
            break
        else:
            print('Vale valik!')

if __name__ == '__main__':
    menu()