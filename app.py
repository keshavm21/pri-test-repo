def get_user_query(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query


if __name__ == "__main__":
    print(get_user_query("alice"))
