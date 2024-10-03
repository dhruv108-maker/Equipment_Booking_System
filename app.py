from queries import queries
from dbcofig import db_connection
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pymysql
from pymysql import MySQLError
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key in production


@app.route('/register_user', methods=['POST'])
def signup():
    try:
        username = request.form['username']
        name_parts = username.split(' ', 1)  # Split on the first space only
        if len(name_parts) == 2:
            first_name, last_name = name_parts
        else:
            first_name = name_parts[0]
        last_name = ''  # If there's no last name, set it to an empty string
        email = request.form['email']
        phone_no = request.form['phone_no']
        password = request.form['password']

        #Using hashing techniques to stroe password securly
       

        role_id = request.form['role_id']

        # Check if the email ends with @gsfcunivercity.ac.in
        if email.endswith('@gsfcuniversity.ac.in'):
            is_member = 1  # True
        else:
            is_member = 0  # False

        # Connect to MySQL database and insert user data
        connection = db_connection()
        with connection.cursor() as cursor:
            # Update the SQL query to include the 'member' column
            sql = queries['signup']
            cursor.execute(sql, ( first_name, last_name, email, phone_no, password, role_id))  # Store plain password and membership status

        connection.commit()
        connection.close()

        flash('Registration successful!', 'success')
        return redirect(url_for('home'))

    except MySQLError as e:
        # Check if the error is a duplicate entry error
        if e.args[0] == 1062:
            flash('This email is already registered. Please use a different email.', 'danger')
        else:
            flash('An unexpected error occurred. Please try again later.', 'danger')
        return redirect(url_for('user_login'))  # Redirect to the login page

    except Exception as e:
        print(f"Error: {str(e)}")
        flash('An unexpected error occurred. Please try again later.', 'danger')
        return redirect(url_for('user_login'))

@app.route('/user_login', methods=['POST'])
def login():
    login_input = request.form['login_input']  # This will hold email, username, or phone number
    password = request.form['login_password']
    

    try:
        connection = db_connection()
        with connection.cursor() as cursor:
            # SQL query to fetch password, email, role_id, and username
            sql = queries['login']
            cursor.execute(sql, (login_input, password))
            result = cursor.fetchone()
            print(f"Query result: {result}")

        if result:
            # FirstName, LastName, Email, Password, RoleID 
            stored_password = result['Password']  # Accessing dictionary correctly
            email = result['Email']  # Fetch the Email with correct case
            role_id = result['RoleID']
            f_name = result['FirstName']
            l_name = result['LastName']
            username = f_name + " " + l_name

            print(f"Stored password: '{stored_password}', Input password: '{password}'")

            if stored_password == password:
                # Store the user details in session
                session['login_input'] = login_input  # Store the login input for later use
                session['email'] = email  # Store the email in session
                session['RoleID'] = role_id  # Store the role ID
                session['username'] = username  # Store the username in session

                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                print("Passwords do not match.")
                flash('Invalid password.', 'danger')
                return redirect(url_for('user_login'))

        else:
            flash('No user found with this email, username, or phone number.', 'danger')
            return redirect(url_for('user_login'))

    except Exception as e:
        print(f"Error during login: {type(e).__name__}: {str(e)}")
        flash('An unexpected error occurred. Please try again later.', 'danger')
        return redirect(url_for('user_login'))


@app.route("/")
def user_login():
    return render_template('login.html')

@app.route("/home")
def home():
    try:
        # Ensure the user is logged in by checking if the email exists in the session
        if 'email' not in session:
            flash('You need to log in to view this page.', 'danger')
            return redirect(url_for('user_login'))

        user_email = session['email']
        role_id = session.get('RoleID')

        # Connect to the database to fetch sample data
        connection = db_connection()
        with connection.cursor() as cursor:
            # Assuming you have a table 'samples' in your database
            query = queries['equipment_info']
            cursor.execute(query)
            equipments = cursor.fetchall()  # Fetch all sample records
            print(equipments)  # Debugging: print the fetched samples

        connection.close()

        # Pass the fetched samples data to the index.html template
        return render_template('index.html', equipments=equipments, role_id=role_id)

    except Exception as e:
        print(f"Error: {str(e)}")
        flash('An unexpected error occurred. Please try again later.', 'danger')
        return redirect(url_for('home'))








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

