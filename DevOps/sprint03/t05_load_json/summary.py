import json


def hashable(v):
    try:
        hash(v)
    except TypeError:
        return False
    return True

def in_dictionary(key, dict):
    return key in dict

def summary(filename,summarize_by):
    file = open(filename)
    f_dict = {}
    try:
        data = json.load(file)
        for i in data:
            if in_dictionary(summarize_by,i):
                if hashable(i[summarize_by]) == False:
                    if in_dictionary("unhashable",f_dict):
                        f_dict["unhashable"] += 1
                    else:
                        f_dict.update({"unhashable" : 1})
                elif i[summarize_by] in f_dict:
                    f_dict[i[summarize_by]] += 1
                else:
                    f_dict.update({i[summarize_by] : 1})
            else:
                if None in f_dict:
                    f_dict[None] += 1
                else:
                    f_dict[None] = 1
        return dict(sorted(f_dict.items(), key=lambda x: x[1],reverse=True))
    except:
        return 'Error in decoding JSON.'



print(summary('s03t05_load_json_test.json', 'visibility'))
print(summary('s03t05_load_json_test.json', 'purpose'))
print(summary('s03t05_load_json_test.json', 'no items with this key'))
print(summary('s03t05_load_json_invalid.json', 'purpose'))