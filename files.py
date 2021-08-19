def map_keys(file_name='keys.txt'):
    """
    ______________________________________________________________________

    file_name: <str>


    ---> <dict> --> {<str> : <str>, <str> : <str>, ... , <str> : <str>}
    ______________________________________________________________________

    Opens 'file_name' and creates a dictionary where every key is assigned
    to an action.
    """
    keys_dict = dict()

    with open(file_name) as f:

        for line in f:

            if line == '\n':
                continue

            keys, action = ''.join(line.split('=')).split()

            for key in keys.split(','):

                keys_dict[key] = action

    return keys_dict

def list_actions(keys_dict=map_keys()):
    """
    ______________________________________________________________________

    keys_dict: <dict> --> {<str> : <str>, <str> : <str>, ... , <str> : <str>}


    ---> <list> --> [<str>, <str>, ... , <str>]
    ______________________________________________________________________

    Returns a list of all the actions in the keys file, without repetitions.
    """
    actions_list = list()

    for action in keys_dict.values():

        if not action in actions_list:

            actions_list.append(action)

    return actions_list

def list_repeated_keys(value, keys_dict=map_keys()):
    """
    ______________________________________________________________________

    value: <str>

    keys_dict: <dict> --> {<str> : <str>, <str> : <str>, ... , <str> : <str>}


    ---> <list> --> [<str>, <str>, ... , <str>]
    ______________________________________________________________________

    Given a value to search for and a dictionary (by default the one that 'map_keys' returns),
    it returns a list of all the keys that have such value.
    """
    return [key for (key, val) in keys_dict.items() if val == value]

def map_level(game_level):
    """
    ______________________________________________________________________

    game_level: <int>


    ---> <dict> --> {<str> : <int>, <str> : <list>*, <str> : <list>, ... , <str> : <list>}

        *<list> --> [<dict>, <dict>, ... , <dict>]
    ______________________________________________________________________

    Defines a dictionary with all the variables a level should have.
    """
    level_dict = dict()
    current_time = -1

    with open(f"levels/level_{game_level}.txt") as f:

        for line in f:

            if line == '\n' or not line.split():

                continue
            
            if line.lstrip()[:2] == '#t':

                _, time = line.split()
                level_dict['total_time'] = int(time)

            elif line.lstrip()[:2] == '#l':

                _, current_time = line.split()
                level_dict[current_time] = list()

            elif line.lstrip()[:2] == '#s':

                ship_dict = dict()
                attributes = line.split('#s')[1].split()

                for attribute in attributes:

                    atr, val = attribute.split('-')
                    ship_dict[atr] = (None if val == '/' else (val if not val.isnumeric() else int(val)))
                
                level_dict[current_time].append(ship_dict)

    return level_dict

def print_keys(keys_dict, file_name='keys.txt'):
    """
    ______________________________________________________________________

    keys_dict: <dict> --> {<str> : <str>, <str> : <str>, ... , <str> : <str>}

    file_name: <str>


    ---> None
    ______________________________________________________________________

    Opens 'file_name' and, if existent, edits within the information of the dictionary
    of the keys. If not, it creates one instead.
    """
    with open(file_name, mode='w') as f:

        dict_values = list_actions(keys_dict)

        for value in dict_values:

            if not value == dict_values[0]:

                f.write("\n\n")

            repeated_keys = ','.join(list_repeated_keys(value, keys_dict))

            f.write(f"{repeated_keys} = {value}")



def ext_constants(file_name='ext_cons.txt'):
    """
    ______________________________________________________________________

    file_name: <str>


    ---> <dict> --> {<str> : <int>, <str> : <bool>, ... , <str> : <str>}
    ______________________________________________________________________

    Maps the external constants that are in a designated file ('ext_cons.txt' by default),
    and creates a dictionary with the information within.
    """
    cons_dict = dict()

    with open(file_name) as f:

        for line in f:

            if line == '\n' or line.split()[0] == '#':

                continue

            fragmented_line = ''.join(line.split('=')).split()

            if fragmented_line[0] in ("ENEMY_TYPES", "BULLET_TYPES"):

                cons_dict[fragmented_line[0]] = fragmented_line[1:]
                continue

            constant, value = fragmented_line

            if value.isnumeric():

                value = int(value)

            elif value == 'True' or value == 'true':

                value = True

            elif value == 'False' or value == 'false':

                value = False

            cons_dict[constant] = value

    return cons_dict

EXT_CONST = ext_constants()