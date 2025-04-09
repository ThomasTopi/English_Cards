"""python file na handlovani a generovani slov z database"""

import pandas as pd
import random

def load_data_from_excel():
    file_path = "database//words.xlsx"
    data = pd.read_excel(file_path)
    return data

def get_random_number():
    size = len(load_data_from_excel())
    return random.randint(0, size - 1)

def get_english_word(ID):
    data = load_data_from_excel()
    eng_word = data.loc[data['ID'] == ID, "ENGLISH"]
    return ''.join(eng_word.to_list())
    
def get_czech_word(ID):
    data = load_data_from_excel()
    czech_word = data.loc[data['ID'] == ID, "CZECH"]
    return ''.join(czech_word.to_list())

