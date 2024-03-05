import os
from openai import AzureOpenAI
import re
import pandas as pd
 
def nlp_to_sql_translator(message):
    client = AzureOpenAI(
        azure_endpoint = 'https://hackathon032024openai-1.openai.azure.com/openai/deployments/team2-model-deployment/chat/completions?api-version=2024-02-15-preview',
        api_key="78ceeb8a13124d1cb6ee493051fefd94",
        api_version="2024-02-15-preview"
    )
 
    message_text = [{"role":"system","content":"You are an Natural language to SQL translator that helps people query data in a SQL database. Please ensure that the reponse is in correct sql syntax."},
                    {"role":"user","content":"Create a select statement for the given chat request:" + message}]
 
 
    completion = client.chat.completions.create(
        model="team2-model-deployment", # model = "deployment_name"
        messages = message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        # stop=None
    )
 
    response_str = completion.choices[0].message.content

    res = response_str.split('```')[1::2]
    return res
 
def create_metadata(xlsx_name):
    df = pd.read_excel(xlsx_name)
    column_data = df.columns.values.tolist()
    metadata = f" Column: {column_data}. "
    for idx, row in enumerate(range(len(df))):
        metadata += f"Row: {idx} has values: {df.iloc[[row]].values.tolist()[0]}. "
    return metadata