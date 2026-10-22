import sqlite3


def get_user_query(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query


def find_user(conn, username):
    return conn.execute(get_user_query(username)).fetchall()


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (username TEXT, email TEXT)")
    conn.execute("INSERT INTO users VALUES ('alice', 'alice@example.com')")
    print(find_user(conn, "alice"))
