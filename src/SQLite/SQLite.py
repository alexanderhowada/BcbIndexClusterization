import sqlite3
from pandas import DataFrame

class SQLite:
	"""
	Simple SQLite connection.
	Notice that this class has no regard for SQL injections
	and its only purpose is to facilitate INSERT and SELECT
	statements for this project

	Example:
		DB = SQLite('test.db')
		DB("CREATE TABLE IF NOT EXISTS asdf(ids INTEGER PRIMARY KEY AUTOINCREMENT, value FLOAT)")
		DB('
			INSERT INTO asdf(value) VALUES (10.3), (3.1415)')
		df = DB.get_dataframe("select * from asdf")
		print(df)
		DB('DROP TABLE asdf')
	"""
	def __init__(self, db_name):
		self.db_name = db_name

	def __call__(self, query):
		"""
		Execute and commit query
		"""
		with sqlite3.connect(self.db_name) as con:
			cur = con.cursor()
			cur.execute(query)
			con.commit()

	def get_dataframe(self, query):
		"""
		Execute and returns a pandas.DataFrame.
		Does not commit.
		"""
		with sqlite3.connect(self.db_name) as con:
			cur = con.cursor()
			cur.execute(query)

			columns = [description[0] for description in cur.description]
			df = DataFrame(cur.fetchall())
			df.columns = columns
		return df

if __name__ == '__main__':
	DB = SQLite('test.db')

	DB("CREATE TABLE IF NOT EXISTS asdf(ids INTEGER PRIMARY KEY AUTOINCREMENT, value FLOAT)")
	DB("""
		INSERT INTO asdf(value) VALUES (10.3), (3.1415);
	""")
	df = DB.get_dataframe("select * from asdf")
	print(df)
	DB('DROP TABLE asdf')

