def input_from_console():
    '''
    This function returns the input from the console.
    
    Returns:
    str: The input from the console.
    '''
    return input()

def input_from_file(file_path):
    '''
    This function returns the input from a file.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The input from the file.
    '''
    return open(file_path, 'r').read()

def input_from_file_pandas(file_path):
    '''
    This function returns the input from a file using pandas.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The input from the file.
    '''
    import pandas as pd
    return pd.read_json(file_path)