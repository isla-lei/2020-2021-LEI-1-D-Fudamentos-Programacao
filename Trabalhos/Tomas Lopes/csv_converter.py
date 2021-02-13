''' csv_converter.py '''

import json
import csv


def make_json(csv_file_path, json_file_path):
    data = []

    with open(csv_file_path, 'r') as csvReader:
        print('A abrir ficheiro CSV ...')
        for line in csv.DictReader(csvReader):
            data.append(line)

    i = 0
    last = 2010

    final_data = []

    while True:
        same_year = []
        while(data[i]['year'] == last and i < 771):
            same_year.append({
                'id': data[i]['id'],
                'home': data[i]['home'],
                'away': data[i]['away'],
                'h_score': data[i]['h_score'],
                'a_score': data[i]['a_score'],
                'date': data[i]['date'],
                'stadium': data[i]['stadium'],
                'attendance': data[i]['attendance'],
                'date': data[i]['date'],
                'phase': data[i]['phase']
            })
            i += 1

        final_data.append(
            {
                'name': data[i-1]['world_cup'],
                'year': last,
                'host': data[i-1]['host'],
                'games': same_year
            }
        )

        last = data[i]['year']

        if(i == 771):
            same_year.append({
                'id': data[i]['id'],
                'home': data[i]['home'],
                'away': data[i]['away'],
                'h_score': data[i]['h_score'],
                'a_score': data[i]['a_score'],
                'date': data[i]['date'],
                'stadium': data[i]['stadium'],
                'attendance': data[i]['attendance'],
                'date': data[i]['date'],
                'phase': data[i]['phase']
            })

            final_data.append(
                {
                    'name': data[i-1]['world_cup'],
                    'year': last,
                    'host': data[i-1]['host'],
                    'games': same_year
                }
            )
            final_data.pop(0)  # Correction from loop
            final_data.pop(-2)  # Correction from last append
            break

    print('Convertido para JSON com sucesso.')

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(final_data, indent=4))
        print('Ficheiro JSON criado!')
