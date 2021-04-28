

def extractor(extractable, value_type):
    return dict(filter(lambda e: isinstance(e[1], value_type), extractable.items()))
    