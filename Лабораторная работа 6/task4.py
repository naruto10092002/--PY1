import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file: str, delimiter=',', new_line='\n') -> list[dict]:
    with open(file, 'r', encoding='utf-8') as f:
        headers = ((f.readline()).strip(new_line)).split(delimiter)
        data = []
        for line in f:
            data.append((line.strip(new_line)).split(delimiter))
    result = []
    for row in data:
        dict_ = {headers[i]: row[i] for i in range(len(headers))}
        result.append(dict_)

    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
