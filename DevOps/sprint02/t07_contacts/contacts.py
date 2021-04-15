import re

def contacts(container, info, operation):
    print(info)
    operations = ['add', 'update', 'delete']
    reg_name = r'^[a-zA-Z0-9-_]*$'
    reg = r'[^@]*@[^@]*\.[^@]*'
    if operation in operations:
        if "email" in info and "name" in info:
            if re.match(reg, info['email']) is not None:
                if re.match(reg_name, info['name']) is not None:
                    key = info.pop("email")
                    if operation == 'add':
                        container.update({key : info})
                        return True
                    elif operation == 'update':
                        if key in container:
                            container.update({key : {**container.get(key),**info}})
                            return True
                        else:
                            return False
                    else:
                        if key in container:
                            container.pop(key, "none")
                            return True
                        else:
                            return False
            else:
                return False
        else:
            return False
    return True
