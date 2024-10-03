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