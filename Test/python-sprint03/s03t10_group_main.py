import json
from group import group

if __name__ == '__main__':
    test_case_data = [
        {
            'name': 'Alex',
            'gender': 'male',
            'species': 'human',
            'job': 'bicycle repair man',
        },
        {
            'name': 'Monika',
            'gender': 'female',
            'species': 'human',
            'job': 'stockbroker'
        },
        {
            'name': 'Bob',
            'gender': 'male',
            'species': 'human',
            'job': 'quantity surveyor'
        },
        {
            'name': 'Veronika',
            'gender': 'female',
            'species': 'human',
            'job': 'church warden'
        },
        {
            'name': 'George',
            'gender': 'male',
            'species': 'human',
            'job': 'bicycle repair man'
        },
    ]
    test_case_data_group_fields_1 = ['gender']
    test_case_data_group_fields_2 = ['species', 'gender', 'job']

    res_1 = group(test_case_data, test_case_data_group_fields_1)
    res_2 = group(test_case_data, test_case_data_group_fields_2)

    print(json.dumps(res_1, indent=2))
    print()
    print(json.dumps(res_2, indent=2))
