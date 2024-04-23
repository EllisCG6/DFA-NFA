def load_file(filename):
    lines = []
    with open(filename, "r") as f:
        for i in f.readlines():
            if i[0] != '#':
                lines.append(i.strip())
    return lines

def get_section_list(L):
    k = 0
    s = [L[0].replace(':','')]
    actual =0
    for i in L:
        if i == 'End':
            k+=1

    for i in range(0, k-1):
        actual = L.index('End', actual+1)
        s.append(L[actual+1].replace(':',''))


    return s

def get_section_content(L, section_name):
    k = L.index(section_name + ':')
    s = []
    for i in range(k+1, len(L)):
        if L[i] == 'End':
            break
        s.append(L[i])
    return s