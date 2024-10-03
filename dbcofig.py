import pymysql
def db_connection():
    return pymysql.connect(
        host='HOSTED_IP_ADDRESS',
        user='USER_NAME',  # Your MySQL username
        password='PASSWORD',  # Your MySQL password
        database='DATABASE_NAME',  # Your database name
        charset='utf8mb4',  # Ensures proper encoding
        cursorclass=pymysql.cursors.DictCursor  # Returns results as dictionaries
)


