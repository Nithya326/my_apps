import pymysql

class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='db', user='root', password='password', database='employees_db')

    def get_all(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM employees")
            rows = cursor.fetchall()
            result = [{'id': r[0], 'name': r[1], 'role': r[2]} for r in rows]
            return result

    def get(self, emp_id):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM employees WHERE id=%s", (emp_id,))
            row = cursor.fetchone()
            return {'id': row[0], 'name': row[1], 'role': row[2]}

    def create(self, name, role):
        with self.conn.cursor() as cursor:
            cursor.execute("INSERT INTO employees (name, role) VALUES (%s, %s)", (name, role))
            self.conn.commit()

    def update(self, emp_id, name, role):
        with self.conn.cursor() as cursor:
            cursor.execute("UPDATE employees SET name=%s, role=%s WHERE id=%s", (name, role, emp_id))
            self.conn.commit()

    def delete(self, emp_id):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
            self.conn.commit()
