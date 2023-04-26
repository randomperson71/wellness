from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Set
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('wellness-384909-19a235143883.json', scope)
client = gspread.authorize(creds)

# Define the home page with a form to input numberFind
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the value of numberFind from the form
        numberFind = request.form['numberFind']

        # Open the sheet and find the cell with the value
        sheet_name = 'copy71'

        ###########################################################

        #Sheet 1


        sheet1 = client.open(sheet_name).worksheet("p1")
        cell_list = sheet1.findall(numberFind)

        if cell_list:
            # Get the first cell in which the value is found
            cell = cell_list[0]
            row_index = cell.row

            # Get the value in the same column as the cell
            column_index = cell.col
            value1 = "Period 1: " + sheet1.cell(1, column_index).value

        else:
            value1 = "Period 1: No Activity Chosen"

        ###############################################################

        #Sheet 2

        sheet2 = client.open(sheet_name).worksheet("p2")
        cell_list = sheet2.findall(numberFind)

        if cell_list:
            # Get the first cell in which the value is found
            cell = cell_list[0]
            row_index = cell.row

            # Get the value in the same column as the cell
            column_index = cell.col
            value2 = "Period 2: " + sheet2.cell(1, column_index).value

        else:
            value2 = "Period 2: No Activity Chosen"

        ################################################################

        #Sheet 3

        sheet3 = client.open(sheet_name).worksheet("p3")
        cell_list = sheet3.findall(numberFind)

        if cell_list:
            # Get the first cell in which the value is found
            cell = cell_list[0]
            row_index = cell.row

            # Get the value in the same column as the cell
            column_index = cell.col
            value3 = "Period 3: " + sheet3.cell(1, column_index).value

        else:
            value3 = "Period 3: No Activity Chosen"

        ###############################################################

        #Sheet 4

        sheet4 = client.open(sheet_name).worksheet("p4")
        cell_list = sheet4.findall(numberFind)

        if cell_list:
            # Get the first cell in which the value is found
            cell = cell_list[0]
            row_index = cell.row

            # Get the value in the same column as the cell
            column_index = cell.col
            value4 = "Period 4: " + sheet4.cell(1, column_index).value

        else:
            value4 = "Period 4: No Activity Chosen"

        values = [value1, value2, value3, value4]

        # Render the template with the value
        return render_template('newresult.html', values=values, numberFind=numberFind)
    else:
        # Render the template with the form
        return render_template('home.html')

# Define the result page to display the value
@app.route('/newresult')
def newresult():
    values = request.args.getlist('values')
    numberFind = request.args.get('numberFind')
    return render_template('newresult.html', values=values, numberFind=numberFind)

# Define the error page to display an error message
@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
