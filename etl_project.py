
## Extract ##

import pandas as pd

df = pd.read_csv('Airline Dataset Updated - v2.csv')
first_name, nationality, airport_name, flight_status = df['First Name'].tolist(), df['Nationality'].tolist(), df['Airport Name'].tolist(), df['Flight Status'].tolist()

## Transform ##

!pip install openai

openai_api_key = 'api key'

import openai

openai.api_key = openai_api_key

def generate_ai_information(name, nationality, airport_name, flight_status):
    if flight_status == 'On Time':
        completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
               "role": "system",
               "content": "Você é um funcionário de uma companhia área."
            },
            {
               "role": "user",
               "content": f"Crie uma mensagem para {name} no idioma de sua {nationality} dizendo que seu voo partindo do {airport_name} está no horário."
            }
          ]
        )
        return completion.choices[0].message.content.strip('\"')
    elif flight_status == 'Delayed':
        completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
               "role": "system",
               "content": "Você é um funcionário de uma companhia área."
            },
            {
               "role": "user",
               "content": f"Crie uma mensagem para {name} no idioma de sua {nationality} dizendo que seu voo partindo do {airport_name} está Atrasado."
            }
          ]
        )
        return completion.choices[0].message.content.strip('\"')
    else:
        completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
               "role": "system",
               "content": "Você é um funcionário de uma companhia área."
            },
            {
               "role": "user",
               "content": f"Crie uma mensagem para {name} no idioma de sua {nationality} dizendo que seu voo partindo do {airport_name} foi Cancelado."
            }
          ]
        )
        return completion.choices[0].message.content.strip('\"')

i = 0
flight_information = []
for passenger in first_name:
    if flight_status[i] == 'On Time':
        information = generate_ai_information(passenger, nationality[i], airport_name[i], flight_status[i])
        flight_information.append(information)
        i += 1
    elif flight_status[i] == 'Delayed':
        information = generate_ai_information(passenger, nationality[i], airport_name[i], flight_status[i])
        flight_information.append(information)
        i += 1
    else:
        information = generate_ai_information(passenger, nationality[i], airport_name[i], flight_status[i])
        flight_information.append(information)
        i += 1

## Load ##


new_df = pd.DataFrame({'First Name': first_name,
                       'Nationality': nationality,
                       'Airport Name': airport_name,
                       'Flight Status': flight_status,
                       'Flight Information': flight_information})

new_df.to_csv('Airline Data Information.csv', index=False)