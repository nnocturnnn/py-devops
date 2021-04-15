from random import choice, randint, seed, shuffle, sample
from string import printable, ascii_letters, digits
import json
import copy
from contacts import contacts


def optional_print(to_print, out=True):
    if out:
        print(to_print)


def rand_str(n=3, opt=printable):
    return ''.join((choice(opt) for _ in range(n)))


def name():
    return rand_str(n=5, opt=ascii_letters + digits + ' _')


def email():
    opt = printable.translate({ord('@'): None})
    return f'{rand_str(opt=opt)}@{rand_str(opt=opt)}.{rand_str(opt=opt)}'


def get_info(case='valid'):
    items = [('name', name()), ('email', email()), ('age', randint(0, 100)),
             ('height', randint(140, 200)), ('website', name() + '.com'),
             (rand_str(opt=ascii_letters), rand_str(opt=ascii_letters))]
    if case == 'random':
        items += (('name', rand_str()), ('email', rand_str()))
    info = {}
    if case != 'missing':
        info[items[0][0]], info[items[1][0]] = items[0][1], items[1][1]
    shuffle(items)
    for i in range(randint(1, 4)):
        info[items[i][0]] = items[i][1]
    return info


def test_add(cont, out=True):
    optional_print(f'{"add test":_^30}', out)
    infos = [get_info() for _ in range(5)]
    emails = [i.get('email') for i in infos]
    to_duplicate, to_overwrite = dict(choice(infos)), get_info()
    to_overwrite['email'] = choice(emails)
    # add several valid items
    res = [contacts(cont, dict(info), 'add') for info in infos]
    # add duplicate
    res.append(contacts(cont, to_duplicate, 'add'))
    # add item with existing email but different
    res.append(contacts(cont, to_overwrite, 'add'))
    optional_print(json.dumps(cont, indent=3), out)
    assert len(cont) == len(infos)
    assert all(res)
    assert all([not value.get('email') for value in cont.values()])
    assert all([e in cont for e in emails])


def test_update(cont, out=True):
    optional_print(f'{"update test":_^30}', out)
    res, old_len, info = [], len(cont), get_info()
    # update non existing contact
    while info['email'] in cont:
        info = get_info()
    res.append(contacts(cont, info, 'update'))
    # update existing, identical
    it = choice(list(cont.items()))
    res.append(contacts(cont, dict(it[1], email=it[0]), 'update'))
    # update existing, different
    for _ in range(5):
        email = choice(list(cont))
        info = dict(get_info(), email=email)
        res.append(contacts(cont, info, 'update'))
    optional_print(json.dumps(cont, indent=3), out)
    assert old_len == len(cont)
    assert all(res[1:]) and not res[0]


def test_delete(cont, out=True):
    optional_print(f'{"delete test":_^30}', out)
    res, emails, old_len = [], sample(list(cont), 2), len(cont)
    # delete not existing
    info = get_info()
    while info['email'] in cont:
        info = get_info()
    res.append(contacts(cont, info, 'delete'))
    # delete existing, identical
    info = dict(cont[emails[0]], email=emails[0])
    emails.append(info.get('email'))
    res.append(contacts(cont, info, 'delete'))
    # delete existing, different
    info = dict(get_info(), email=emails[1])
    emails.append(info.get('email'))
    res.append(contacts(cont, info, 'delete'))
    assert len(cont) == old_len - 2
    assert all(res[1:]) and not res[0]
    assert all([email not in cont for email in emails])


def test_validation(cont, out=True):
    optional_print(f'{"validation test":_^30}', out)
    infos, ops, cont_cpy = [], ['add', 'update', 'delete'], copy.deepcopy(cont)
    # 'name' or 'email' missing
    while len(infos) < 5:
        info = get_info('missing')
        if not ('name' in info and 'email' in info):
            infos.append(info)
    res = [contacts(cont, dict(i), choice(ops)) for i in infos]
    # operation invalid
    res.append(contacts(cont, get_info(), rand_str()))
    assert not any(res)
    assert cont_cpy == cont
    # random info, can happen to be valid or invalid
    for i in [get_info('random') for _ in range(15)]:
        op = choice(ops)
        if len(cont) and randint(0, 20) % 2:
            i['email'] = choice(list(cont))
        res.append(contacts(cont, dict(i), op))
    optional_print(res, out)
    optional_print(json.dumps(cont, indent=3), out)


def run_test(n_seed=0, out=True, cont=None):
    if cont is None:
        cont = dict()
    seed(n_seed)
    test_add(cont, out)
    test_update(cont, out)
    test_delete(cont, out)
    test_validation(cont, out)


if __name__ == '__main__':
    # run with different n_seed to test your output
    # you will see the printed output for this case
    run_test(n_seed=3)
    for s in range(20):
        # these test runs wont print anything unless an assertion has failed
        run_test(n_seed=s, out=False)
