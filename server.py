from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data["name"]
        Email = data["Email"]
        message= data["message"]
        database.write(f'\n{name},{Email},{message}')

def write_to_csv(data):
    with open('database2.csv', newline='', mode='a') as database2:
        name = data["name"]
        Email = data["Email"]
        message= data["message"]
        csv_write= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([name,Email,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
   if request.method == 'POST':
       data= request.form.to_dict()
       write_to_csv(data)
       return redirect('contact.html')
   else:
       return redirect('contact-wrong.html')