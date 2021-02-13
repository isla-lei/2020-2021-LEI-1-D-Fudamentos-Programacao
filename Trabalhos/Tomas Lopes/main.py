import csv
import json
import sys

from csv_converter import make_json
from game import play

csv_file_path = 'data.csv'
json_file_path = 'data.json'


def try_to_create_file():
    try:
        open(json_file_path)
        return True
    except FileNotFoundError:
        try:
            make_json(csv_file_path, json_file_path)
            return False
        except FileNotFoundError:
            print('Ficheiro de dados (CSV) não encontrado.')
            input('\nPressione a tecla ENTER para voltar ao menu...')

            return False


def print_menu():
    import os

    os.system('cls' if os.name == 'nt' else 'clear')

    print('1. Jogar')
    print('2. Gerar o ficheiro a partir do CSV')
    print('3. Consultar os dados de assistência')
    print('4. Alterar dados de assistência')
    print('5. Eliminar dados de assistência')
    print('6. Consultar todos os dados')
    print('7. Pesquisar')
    print('8. Total de espetadores')
    print('9. Informações de uma seleção')
    print('10. Eliminar ficheiro JSON')
    print('11. Sair\n')


def option_switch(option):
    if(option == 1):
        play(json_file_path)
        input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 2):
        if(try_to_create_file()):
            print('O ficheiro já existe')
            input('\nPressione a tecla ENTER para voltar ao menu...')
            return
        else:
            input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 3):
        print_attendance_info()
        input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 4):
        edit_attendance_info()
        input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 5):
        delete_file(json_file_path)
        try_to_create_file()

        print('Dados de assistência resetados...')
        input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 6):
        try:
            opt = int(input('Deseja abrir o ficheiro JSON ou CSV? (1/2): '))

            if(opt == 1):
                print_json_file(json_file_path)
            elif(opt == 2):
                print_csv_file(csv_file_path)
            else:
                print('Deve inserir um número entre 1 e 2')

            input('\nPressione a tecla ENTER para voltar ao menu...')
        except ValueError:
            print('Deve inserir um valor numérico')
            input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 7):
        search_in_file(json_file_path)
        input('\nPressione a tecla ENTER para voltar ao menu...')
    elif(option == 8):
        spectators = total_attendance()

        for info in spectators:
            print(
                str(info['year']) + ': ' + str(info['spectators']))
        print('\nNota: Nem todos os jogos têm informação atualizada quanto ao número de espetadores.')

        input('\nPressione a tecla ENTER para voltar ao menu...')
    elif(option == 9):
        teams = get_all_teams(json_file_path)
        for team in teams:
            print(str(team['index']) + '. ' + team['team'])

        try:
            opt = int(input('Introduza uma opção: '))

            if (opt < 1 or opt > 81):
                print('Introduza uma opção válida.')
                input('\nPressione a tecla ENTER para voltar ao menu...')
                return

            team_info = get_team_info(teams, opt)

            pretty_obj = pretiffy_json(team_info)

            print(pretty_obj)

            input('\nPressione a tecla ENTER para voltar ao menu...')
        except ValueError:
            print('Deve introduzir um valor numérico')
            input('\nPressione a tecla ENTER para voltar ao menu...')

    elif(option == 10):
        delete_file(json_file_path)

        input('\nPressione a tecla ENTER para voltar ao menu...')
    elif(option == 11):
        sys.exit()
    else:
        print('Opção Inválida.')
        input('\nPressione a tecla ENTER para voltar ao menu...')


def pretiffy_json(data):
    return json.dumps(data, indent=4)


def print_json_file(file_path):
    json_obj = open_file(file_path)

    if(json_obj == False):
        return

    pretty_obj = pretiffy_json(json_obj)

    print(pretty_obj)


def print_csv_file(file_path):
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print('CSV file not found.')


def get_all_teams(file_path):
    json_obj = open_file(file_path)

    if(json_obj == False):
        return

    teams = []

    for competition in json_obj:
        for game in competition['games']:
            if(not (game['home'] in teams)):
                teams.append(game['home'])

            if(not(game['away'] in teams)):
                teams.append(game['away'])

    teams.sort()

    data = []
    i = 1

    for team in teams:
        data.append({'index': i, 'team': team})
        i += 1

    return data


def total_attendance():
    json_obj = open_file(json_file_path)

    if(json_obj == False):
        return

    data = []

    for competition in json_obj:
        spectators = 0

        for game in competition['games']:
            if(game['attendance']):
                spectators += int(game['attendance'])

        data.append({'year': competition['year'], 'spectators': spectators})

    return data


def search_in_file(path):
    json_obj = open_file(path)

    if(json_obj == False):
        return

    years = []

    for competition in json_obj:
        years.append(competition['year'])

    years.sort()

    try:
        needle = int(
            input('Introduza um ano para ver as informações sobre a competição do mesmo: '))

        (result_index, time, n_of_iterations) = sequencial_search(years, str(needle))

        if(result_index == -1):
            print(f'\nOops... O elemento não existe na lista.')

        print('\n--------------------------------Pesquisa Sequencial--------------------------------')
        print(
            f'Tempo passado: {time}.\nNº de iterações: {n_of_iterations}')

        (result_index, time, n_of_iterations) = binary_search(years, needle)
        print('\n--------------------------------Pesquisa Binária--------------------------------')
        print(f'Tempo passado: {time}\nNº de iterações: {n_of_iterations}')

        if(result_index != -1):
            try:
                answer = input('Deseja ver o resultado da pesquisa? (S/N): ')

                if(answer.lower() == 's'):
                    # As the array is reversed in the sorting process the real index is the inverse of the index found
                    result = pretiffy_json(json_obj[-(result_index + 1)])
                    print(result)
            except ValueError:
                print('Deve inserir um valor numérico.')

    except ValueError:
        print('Deve inserir um valor numérico.')
        return


def sequencial_search(array, needle):
    import time

    start_time = time.time()
    i = 0

    for i in range(len(array)):
        if(array[i] == needle):
            i += 1
            return (i, time.time() - start_time, i)

    return (-1, time.time() - start_time, i)


def binary_search(array, needle):
    import time

    start_time = time.time()

    min = 0
    max = len(array) - 1
    mid = 0

    i = 0

    while min <= max:
        i += 1
        mid = (max + min) // 2

        if int(array[mid]) < needle:
            min = mid + 1

        elif int(array[mid]) > needle:
            max = mid - 1

        else:
            return (mid, time.time() - start_time, i)

    return (-1, time.time() - start_time, i)


def open_file(path):
    try:
        with open(path, 'r') as file:
            json_obj = json.load(file)

        return json_obj
    except FileNotFoundError:
        print('Ficheiro não encontrado.')
        return False


def get_team_info(teams, index):
    team = teams[index - 1]['team']

    json_obj = open_file(json_file_path)

    if(json_obj == False):
        return

    team_data = []

    for competition in json_obj:
        for game in competition['games']:
            if(game['home'] == team or game['away'] == team):
                team_data.append(game)

    return team_data


def delete_file(path):
    import os

    try:
        os.remove(path)

        print('Ficheiro eliminado.')
    except OSError:
        print('Alguma coisa correu mal.')


def print_attendance_info():
    json_obj = open_file(json_file_path)

    if(json_obj == False):
        return

    for competition in json_obj:
        print(str(competition['name']))
        for game in competition['games']:
            print('    ' + str(game['home']) +
                  ' x ' + str(game['away']) + ': ' + str(game['attendance']))


def edit_attendance_info():
    json_obj = open_file(json_file_path)

    if(json_obj == False):
        return

    i = 0
    for competition in json_obj:
        print(str(i + 1) + '. ' + str(competition['name']))
        i += 1

    try:
        option = int(input(
            '\nIntroduza o número da competição que pretende editar: '))

        if(option < 1 or option > 19):
            print('Introduza uma opção válida.')
            return

        edit_competition_attendance_info(json_obj, option)
    except ValueError:
        print('Deve inserir um valor numérico.')


def edit_competition_attendance_info(competitions, competition_index):
    competition = competitions[competition_index]

    print('\n\nA editar a informação de ' + str(competition['name']) + '\n')
    i = 0
    for game in competition['games']:
        print(str(i+1) + '. ' + str(game['home']) + ' x ' +
              str(game['away']) + ': ' + str(game['attendance']))
        i += 1

    try:
        option = int(
            input('\nEscolha um jogo para editar a informação de assistência: '))

        if(option < 1 or option > i + 1):
            print('Introduza uma opção válida.')

        try:
            new_value = int(input('Introduza o novo valor de assistência: '))
            edit_game_attendance_info(
                competition_index, option - 1, new_value)
        except ValueError:
            print('Deve inserir um valor numérico.')

    except ValueError:
        print('Deve inserir um valor numérico.')


def edit_game_attendance_info(competition_index, game_index, value):
    json_obj = open_file(json_file_path)

    if(json_obj == False):
        return

    json_obj[competition_index]['games'][game_index]['attendance'] = str(value)

    with open(json_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(json_obj, indent=4))


def start():
    try:
        while True:  # The loop will end with option 11 that calls sys.quit()
            print_menu()
            option = int(input('Escolha uma opção: '))
            option_switch(option)
    except ValueError:
        print('Deve introduzir um valor numérico.')


start()
