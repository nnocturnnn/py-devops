

def witch_hunt(suspect_sets, innocent_sets):
    alls = set()
    if suspect_sets:
        alls = suspect_sets[0].intersection(*suspect_sets)
    alls = alls.difference(*innocent_sets)
    return alls
