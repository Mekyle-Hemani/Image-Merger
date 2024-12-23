import pickle

def save(variable, filename='save.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(variable, file)

def load(filename='save.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None