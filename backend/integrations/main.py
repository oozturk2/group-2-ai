from azure_open_ai import create_metadata, nlp_to_sql_translator, load_prompt_message

metadata = create_metadata()
prompt_message = load_prompt_message()
response = nlp_to_sql_translator(f'Hello. Using this metadata {metadata}, please create me a SQL-query based on the {prompt} message')
