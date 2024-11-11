#TODO: Create Database before altering API routes, and update these values
class Config:
    MYSQL_HOST = "localhost"        # Change to Docker MySQL hostname later
    MYSQL_USER = "root"             # MySQL username
    MYSQL_PASSWORD = "yourpassword" # MySQL password
    MYSQL_DB = "flaskdb"            # Database name
