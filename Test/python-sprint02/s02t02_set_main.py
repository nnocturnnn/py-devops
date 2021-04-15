from witch_hunt import witch_hunt


def run_test(suspect_sets, innocent_sets):
    witches = witch_hunt(suspect_sets, innocent_sets)
    assert isinstance(witches, set)
    print(f'Witches found: {sorted(list(witches))}')


if __name__ == '__main__':
    can_read = {'Keeva', 'Daegal', 'Adam', 'Bellatrix', 'Ulrich', 'Keene',
                'Evanora', 'Earthan', 'Paxton', 'Alice', 'Candice', 'Cedonia',
                'Zelig', 'Lydia', 'Mortimer'}
    talk_to_self = {'Candice', 'Lydia', 'Chilton', 'Alice', 'Cedonia',
                    'Minerva', 'Adam', 'Daegal', 'Camilla', 'Keene',
                    'Chalmers', 'Keeva', 'Paxton'}
    healers = {'Bellatrix', 'Cullen', 'Adam', 'Alice', 'Lydia', 'Ulrich',
               'Zelig', 'Cedonia', 'Paris', 'Chalmers', 'Chilton',
               'Minerva', 'Paxton', 'Mortimer', 'Earthan', 'Daegal'}
    wealthy = {'Chalmers', 'Keeva', 'Alice', 'Cullen', 'Minerva'}
    men = {'Keene', 'Zelig', 'Mortimer', 'Adam', 'Ulrich', 'Chalmers',
           'Paxton', 'Cullen', 'Chilton', 'Earthan', 'Daegal'}

    run_test([can_read, talk_to_self, healers], [wealthy, men])
    run_test([], [wealthy, men])
    run_test([can_read, talk_to_self, healers], [])
