"""Base Schema"""

from settings.settings import manage_database


def create_tables():
    manage_database.create_table("CREATE TABLE regions(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) NOT NULL)")
    manage_database.create_table(
        """CREATE TABLE countries(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) NOT NULL, 
        language VARCHAR NOT NULL, region_id INTEGER NOT NULL, 
        FOREIGN KEY(region_id) REFERENCES regions(id))""")
    manage_database.create_table(
        """CREATE TABLE metrics(id INTEGER PRIMARY KEY AUTOINCREMENT, time DOUBLE NOT NULL, 
        country_id INTEGER NOT NULL,
        FOREIGN KEY(country_id) REFERENCES countries(id))""")
