from flask import Flask, request
from flask_cors import CORS
from integrations.azure_open_ai import create_metadata, nlp_to_sql_translator
from integrations.sql_helper import db_execute_sql
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/api/messages", methods = ["GET","POST"])
def messages():
    if request.method=="POST":
        question = request.json.get('message')
        #df = pd.read_excel('I:\12-Data Management\z_Ozturk\Hackhaton\GPT_TMD.xlsx')        
        #column_data = df.columns.values.tolist()
        metadata_str = create_metadata(r'I:\12-Data Management\z_Ozturk\Hackhaton\GPT_TMD.xlsx')
        response = nlp_to_sql_translator(f"This is my metadata tabel: {metadata_str}. Please create a SQL query for this request {question}")
        sql_script = response[0].replace('\n', ' ')[3:]
        print(sql_script)
        output_data = db_execute_sql(database_name='PyAutomate', server_name='DK2CPHDM01\DM01', sql_script=sql_script)
        print("_______________________________")
        print(output_data)
    return str(output_data)

if __name__=="__main__":
    app.run( debug=True)