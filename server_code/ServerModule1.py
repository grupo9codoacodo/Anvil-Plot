import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

import mysql.connector
cnx = mysql.connector.connect(user='anvil', password='catalina01',
                              host='127.0.0.1',
                              database='anvil')

@anvil.server.callable
def get_user_signups():
    cur = cnx.cursor()
    cur.execute("""
        SELECT COUNT(*), DATE_TRUNC('week', signup_date) AS d
             FROM users
             WHERE signup_date > NOW() - INTERVAL '3 months'
             GROUP BY DATE_TRUNC('week', signup_date)
             ORDER BY d;
    """)
    return list(cur)