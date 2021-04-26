from summary import summary

if __name__ == '__main__':
    print(summary('s03t05_load_json_test.json', 'visibility'))
    print(summary('s03t05_load_json_test.json', 'purpose'))
    print(summary('s03t05_load_json_test.json', 'no items with this key'))
    print(summary('s03t05_load_json_invalid.json', 'purpose'))
