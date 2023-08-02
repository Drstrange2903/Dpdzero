from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Vraj_2903",
    "database": "dpdzero",
}

def get_db_connection():
    return mysql.connector.connect(**mysql_config)

@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        full_name = data["full_name"]
        email = data["email"]
        age =data["age"]
        username=data["username"]
        gender=data["gender"]
        password=data["password"] 
        id=data["id"]       

        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO users (full_name, email,age,username,gender,password,id) VALUES (%s, %s)"
        cursor.execute(insert_query, (full_name, email,age,username,gender,password,id))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "User created successfully"}), 201
    except KeyError as e:
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(select_query, (user_id,))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        full_name = data["full_name"]
        email = data["email"]
        age =data["age"]
        username=data["username"]
        gender=data["gender"]
        password=data["password"] 
        id=data["id"]

        connection = get_db_connection()
        cursor = connection.cursor()

        update_query = "UPDATE users SET full_name = %s, email = %s,age = %s,username = %s,gender = %s,password = %s WHERE id = %s"
        cursor.execute(update_query, (full_name, email, user_id,age,username,gender,password,id))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "User updated successfully"}), 200
    except KeyError as e:
        return jsonify({"error": "Invalid data format"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM users WHERE id = %s"
        cursor.execute(delete_query, (user_id,))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)