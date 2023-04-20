def get_data(filename):
    with open(filename, 'r', encoding='utf8') as rf:
        lines = rf.read().split("\n")
        data = [d.split("\t") for d in lines if d != ""]
        header = data[0]
        data = data[1:]
    return header, data