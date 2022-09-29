from flaskext.mysql import MySQL
from source import app


# use your database name and password
mysql=MySQL()
 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '****'
app.config['MYSQL_DATABASE_DB'] = 'Application'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app) #initilizing the app
