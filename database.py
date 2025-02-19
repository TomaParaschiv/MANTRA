import psycopg2
#------------------------------------------------------------------#
#------------------------- DATABASE CLASS -------------------------#
class Database:
    def __init__(self, db_name, user, password, host="localhost", port="5432"):
        """
        Manages the connection to the PostgreSQL database.
        -Potential to return records of items in one set meal, daily totals to a sql table, and during a full day, the records will stay in the app, so it doesn't reset every time its ran.
        """
        try:
            self.connection = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def get_item(self, name):
        """
        Fetches a single row (kcal, protein, carbs, fats, category) from 'food' table.
        matching the given name (case-insensitive).
        :param name: Name of the food/drink item to look up.
        :return: Tuple (kcal, protein, carbs, fats, category) or None if not found.
        """
        try:
            query = 'SELECT kcal, protein, carbs, fats, category FROM food WHERE LOWER(name) = LOWER(%s)'
            self.cursor.execute(query, (name,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error fetching item from database: {e}")
            return None

    def get_all_food_names(self):
        """
        Fetches all names from the 'food' table for use in the autocomplete combo box.
        -Potential to change logic/add and help with spelling while the user is typing.
        :return: List of food/drink names.
        """
        try:
            self.cursor.execute("SELECT name FROM food")
            return [row[0] for row in self.cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching food names: {e}")
            return []

    def close_connection(self):
        """
        Closes the cursor and the database connection.
        """
        self.cursor.close()
        self.connection.close()

