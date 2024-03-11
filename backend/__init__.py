from flask import Flask, request
from flask_cors import CORS
from integrations.azure_open_ai import create_metadata, nlp_to_sql_translator
from integrations.sql_helper import db_execute_sql, db_read
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/api/messages", methods = ["GET","POST"])
def messages():
    if request.method=="POST":
        question = request.json.get('message')
        print(db_read('factTable'))
        metadata_str = create_metadata('backend\\integrations\\files\\GPT_TMD.xlsx')
        print(metadata_str)
        response = nlp_to_sql_translator(f"This is my metadata tabel: {metadata_str}. Based on this metadata, please create a SQL query for this request {question}")
        print(response)
        start_index = response.find("```sql") + 6
        end_index = response.find("```", start_index)
        sql_script = response[start_index:end_index]
        print(sql_script)
        output_data = db_execute_sql(sql_script=sql_script)
        print("_______________________________")
        print(output_data)
    return str(output_data)

if __name__=="__main__":
    app.run( debug=True)