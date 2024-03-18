def write_in_console(message):
    '''
    This function writes the message to the console.

    Parameters:
    message (str): The message to write to the console.
    '''
    print(message)

def write_in_file(file_path, message):
    '''
    This function writes the message to a file.

    Parameters:
    file_path (str): The path to the file.
    message (str): The message to write to the file.
    '''
    import os
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
        
    with open(file_path, 'w') as file:
        file.write(message)


"""
def write_in_file_pandas(file_path, message):
    '''
    This function writes the message to a file using pandas.

    Parameters:
    file_path (str): The path to the file.
    message (str): The message to write to the file.
    '''
    import os
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    import pandas as pd
    pd.DataFrame([message]).to_json(file_path)
"""