#
# every section has to be written like this:
# (section_name):
#     - content
# End
#
# Before each section it should be a #
#
# The section_name has to be unique for each section.
#
# First, you have to load your file: e.g. content = load_file(file_name)
# Next, you get your section names: e.g. sec_list = get_section_list(content)
# Then, if you want to get section content: e.g. sec_cnt = get_section_content(content, section_name)

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

# adaug in lista liniile care nu sunt comentarii

# for i in range(lines.index('Sigma:')+1, len(lines)):
#     if lines[i] == 'End':
#         break
#     alphabet.append(lines[i])
# # scot alfabetul
#
# for i in range(lines.index('States:')+1, len(lines)):
#     if lines[i] == 'End':
#         break
#     states.append(lines[i])
# #scot statesurile
#
# for i in range(lines.index('Transitions:')+1, len(lines)):
#     if lines[i] == 'End':
#         break
#     transitions.append(lines[i])
# # scot tranzitiile
#
# print(alphabet, states, transitions)
#
# second = lines.index('End', lines.index())
