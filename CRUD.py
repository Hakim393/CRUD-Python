import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Terhubung dengan Database!")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task_name TEXT NOT NULL,
                priority INTEGER NOT NULL
            );
        ''')
        print("Tabel berhasil dibuat!")
    except sqlite3.Error as e:
        print(e)

def add_task(conn, task_name, priority):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (task_name, priority)
            VALUES (?, ?);
        ''', (task_name, priority))
        conn.commit()
        print("Data berhasil ditambahkan!")
    except sqlite3.Error as e:
        print(e)

def view_all_tasks(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tasks;
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_task(conn, task_id, new_task_name, new_priority):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            Pembaharuan Data
            SET task_name = ?, priority = ?
            WHERE id = ?;
        ''', (new_task_name, new_priority, task_id))
        conn.commit()
        print("Pembaharuan Data telah berhasil!")
    except sqlite3.Error as e:
        print(e)

def delete_task(conn, task_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tasks
            WHERE id = ?;
        ''', (task_id,))
        conn.commit()
        print("Data berhasil dihapus!")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "tasks.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)

        while True:
            print("\nSilahkan memilih :")
            print("1. Tambahkan Data")
            print("2. Perlihatkan semua Data")
            print("3. Update Data")
            print("4. Hapus Data")
            print("5. Keluar")

            choice = input("Masukan pilihan (1-5) : ")

            if choice == '1':
                task_name = input("Masukan nama Data : ")
                priority = input("Masukan Nilai Data : ")
                add_task(conn, task_name, priority)
            elif choice == '2':
                print("Semua Data :")
                view_all_tasks(conn)
            elif choice == '3':
                task_id = input("Masukan ID Data untuk diupdate : ")
                new_task_name = input("Masukan nama Data yang baru : ")
                new_priority = input("Masukan nilai data yang baru : ")
                update_task(conn, task_id, new_task_name, new_priority)
            elif choice == '4':
                task_id = input("Masukan ID Data untuk di hapus : ")
                delete_task(conn, task_id)
            elif choice == '5':
                break
            else:
                print("Pilihan gagal, masukan pilihan dari 1 - 5")

        conn.close()
    else:
        print("Error! Tidak dapat membuat Database.")

if __name__ == '__main__':
    main()
