#
# every section has to be written like this:
# (section_name):
#     - content
# End
#
# The section_name has to be unique for each section.
#
# First, you have to load your file: e.g. content = load_file(file_name)
# Next, you get your section names: e.g. sec_list = get_section_list(content)
# Then, if you want to get section content: e.g. sec_cnt = get_section_content(content, section_name)


import ex1_parser as f
c = f.load_file("m3.txt") #aici incarc fisierul
s = f.get_section_list(c) #aici listez sectiunile
print(s)
for i in s:
    print(i+": ",f.get_section_content(c, i))

#elimin din states specificatorii de start si final si voi ramane cu un array ce va continte lista de statesuri
states=[]
for i in f.get_section_content(c, 'States'):
        states.append(i.split(',')[0])

final=[] #aici voi avea toate starile finale
start=[] # aici voi avea toate startile de start

def dfa_checker():
    

    
    #verific daca exista start state
    ok_start = 0
    for i in f.get_section_content(c, 'States'):
        if 'S' in i:
            if i.split(',')[0] in states:
                ok_start = 1;
                start.append(i.split(',')[0])
    if not(ok_start):
        print("nu avem start ok")
    
    #verific daca exista final state
    ok_end = 0
    for i in f.get_section_content(c, 'States'):
        if 'F' in i:
            if i.split(',')[0] in states:
                ok_end = 1;
                final.append(i.split(',')[0])
    if not(ok_end): 
        print("nu avem final_state ok")
    
    #urmeaza sa verific daca elementele din tranzitie sunt specificate in alfabet sau in stari
    ok_transition = 1
    
    for i in f.get_section_content(c, 'Transitions'):
        for x in i.replace(" ", "").split(','):
        
            if x not in f.get_section_content(c, 'Sigma') and x not in states:
                ok_transition = 0
        if len(i.split(',')) !=3:
            ok_transition = 0
                
    if not(ok_transition):
        print("tranzitiile nu sunt corecte")
    
    if ok_end and ok_start and ok_transition:
        print("DFA-ul este corect")

dfa_checker()

print(states)
print("Start: ",start)
print("Final: ",final)

limbaj = input("Introduceti string: ")

stare_curenta = start[0]
transitions = f.get_section_content(c, "Transitions")
delta = []
for l in limbaj:
    delta = []
    for i in transitions:
        if(stare_curenta == i.replace(" ", "").split(',')[0] and l == i.replace(" ", "").split(',')[1]):
            delta = i.replace(" ", "")
            break
    stare_curenta = delta.split(",")[2]

if stare_curenta in final:
    print("String acceptat")
else:
    print("String neacceptat")


