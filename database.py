from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'myuser',
    'password': 'mypassword',
    'database': 'my_database'
}

@app.route('/users', methods=['GET'])
def get_users():
    # Connect to MySQL
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    
    # Execute a query
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    connection.close()
    
    # Return the result as JSON
    return jsonify([{"id": row[0], "name": row[1], "email": row[2]} for row in rows])

if __name__ == '__main__':
    app.run(debug=True)