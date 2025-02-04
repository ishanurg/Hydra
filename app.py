import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import werkzeug
import socket
import psutil

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'xls', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anomaly')
def anomaly():
    return render_template('anomaly.html')

@app.route('/nas')
def nas():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('nas.html', files=files)

@app.route('/sniffer')
def sniffer():
    return render_template('sniffer.html')

@app.route('/traffic_filter')
def traffic_filter():
    return render_template('traffic_filter.html')




# File Upload Route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('nas', error='No file part'))
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(url_for('nas', error='No selected file'))
    
    if file and allowed_file(file.filename):
        try:
            filename = werkzeug.utils.secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('nas', message='File uploaded successfully'))
        except Exception as e:
            return redirect(url_for('nas', error=str(e)))
    
    return redirect(url_for('nas', error='File type not allowed'))

# File Delete Route
@app.route('/delete/<filename>')
def delete_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return redirect(url_for('nas', message='File deleted successfully'))
        else:
            return redirect(url_for('nas', error='File not found'))
    except Exception as e:
        return redirect(url_for('nas', error=str(e)))

# File Download Route
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
@app.route('/network_dashboard')
def network_dashboard():
    return render_template('network_dashboard.html')
#def network_dashboard():
 #   return redirect("http://localhost:3000/lua/login.lua")
if __name__ == '__main__':
    app.run(debug=True)
