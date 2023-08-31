from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for Flask flash messages

# Database configuration
db_config = {
    'host': 'your_host',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_db'
}

@app.route('/')
def index():
    return render_template('feedback_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = {
            'full_name': request.form.get('full_name'),
            'email_address': request.form.get('email_address'),
            'phone_number': request.form.get('phone_number'),
            'product_name': request.form.get('product_name'),
            'purchase_date': request.form.get('purchase_date'),
            'product_quality': request.form.get('product_quality'),
            'expectations_met': request.form.get('expectations_met'),
            'ease_of_use': request.form.get('ease_of_use'),
            'recommendation': request.form.get('recommendation'),
            'likes': request.form.get('likes'),
            'dislikes': request.form.get('dislikes'),
            'comments': request.form.get('comments'),
            'follow_up': request.form.get('follow_up')
        }

        # Connect and insert data into MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        insert_query = ("INSERT INTO feedback (full_name, email_address, phone_number, product_name, purchase_date, "
                        "product_quality, expectations_met, ease_of_use, recommendation, likes, dislikes, comments, follow_up) "
                        "VALUES (%(full_name)s, %(email_address)s, %(phone_number)s, %(product_name)s, %(purchase_date)s, "
                        "%(product_quality)s, %(expectations_met)s, %(ease_of_use)s, %(recommendation)s, %(likes)s, "
                        "%(dislikes)s, %(comments)s, %(follow_up)s)")
        cursor.execute(insert_query, data)
        conn.commit()
        cursor.close()
        conn.close()

        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('index'))
    except Exception as e:
        flash('An error occurred. Please try again.', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
