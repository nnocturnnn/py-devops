


def raise_error(key, msg):
    keys = ['value','key','index','memory','name','eof']




if __name__ == '__main__':
    errors = ['value', 'key', 'index', 'memory', 'name', 'eof', 'wrong', '']
    for error in errors:
        message = f'This is a `{error}` error.'
        try:
            raise_error(error, message)
        except Exception as e:
            print(f'call with "{error}", "{message}":'
                  f'\n\tRaised error: {type(e)}'
                  f'\n\tMessage: {str(e)}\n')