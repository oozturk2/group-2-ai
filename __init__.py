from flask import Flask, request, render_template
from flask_cors import CORS
from backend.integrations.azure_open_ai import create_metadata, nlp_to_sql_translator
from backend.integrations.sql_helper import db_execute_sql
app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET","POST"])
def messages():
    if request.method=="POST":
        question = request.form['user_input']
        metadata_str = create_metadata('backend\\integrations\\files\\GPT_TMD.xlsx')
        response = nlp_to_sql_translator(f"This is my metadata tabel: {metadata_str}. Based on this metadata, please create a SQL query for this request {question}")
        start_index = response.find("```sql") + 6
        end_index = response.find("```", start_index)
        sql_script = response[start_index:end_index]
        chatbot_output = db_execute_sql(sql_script=sql_script)
        return render_template('index.html', chatbot_output=chatbot_output)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)