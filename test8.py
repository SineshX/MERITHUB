from pprint import pprint

# person = {name: , father: , mother: , husband:  land: , money: ,  6}

# plist = {'ram' : { father: , mother: , husband:  land: , money: , dec : {} } }
plist = {'ram' : {}}

with open('textdata.txt' , 'r' ) as f:
    lst = f.readlines()
    for line in lst:
        person = {}
        # TODO : fetch mother from same dict if p exist  :)
        # print(line.strip()[20:])
        l = line.strip()[20:]
        money = int(l.split(' in ')[1][:-7])
        land = int(l.split(' purchased ')[1].split()[0])

        # print(money)
        # print(land)

        # two ppl
        # print(l.find('and'))
        ppl = l.split(" and ")


        if(len(ppl) == 2):
            # two ppl 
            print("two ppl")
            # Mr. Sinesh s/o Mr. Akshayawat
            name1 = ppl[0].split(" s/o ")[0][4:]
            # Mr. Subham s/o Mr. Akshayawat has purchased 14 acre land in 28000000/- only
            name2 = ppl[1].split(" s/o ")[0][4:]

            father = ppl[0].split(" s/o ")[1][4:]
            print(name1,name2,father)


            if name1 in plist:
                # just add money and land ++
                plist[name1]['money'] += money/2
                plist[name1]['land'] += land/2
                
            else:
                # fresh
                # person['mother'] =  ''
                # person['husband'] = ''
                person['father'] = father
                person['land'] = land/2 
                person['money'] = money/2
                plist[name1] =  person

            if name2 in plist:
                # just add money and land ++
                plist[name2]['money'] += money/2
                plist[name2]['land'] += land/2
                pass
            else:
                # baki saari properties same rahegi 
                person['father'] = father
                person['land'] = land/2 
                person['money'] = money/2
                plist[name2] =  person

            if father in plist:
                # plist[father]['des'] = {name1 :'', name2:''}
                pass
            else: 
                # create father 
                plist[father] = {}
                plist[father]['des'] = [name1, name2]
                
        # end of 2 ppl 
        
        else:
            # single p
            print("single")

            if(l[:3] == 'Mr.'):
                # print("male")


                name = l.split(' s/o ')[0][4:]

                if name in plist:
                    # just add money and land ++
                    plist[name]['money'] += money
                    plist[name]['land'] += land 
                    
                else:
                    # fresh
                    #Mr. Akshayawat has purchased 10 acre land in 10000000/- only
                    if(l.split(' s/o ')[1][:3] == 'Mr.'):
                        father = l.split(' s/o ')[1].split(" has ")[0][4:]
                        print(name,father)

                        # TODO : create father's dict if not available ; created 
                        if father in plist:
                            # if name in plist[father]['des']: 
                            #     # agar beta ya beti hui 
                                
                            #     pass
                            # else:
                            #     
                            plist[father]['des'] = [name, ] 

                        else: 
                            person['father'] = father
                            

                    else:
                        mother = l.split(' s/o ')[1].split(" has ")[0][4:]
                        print(name,mother)
                        person['mother'] = mother
                        # TODO : create mother's dict if not available 
                        if mother in plist:
                            plist[mother]['des'] = plist[name]['father']['des']
                        else:
                            pass
                        
                        

                    person['husband'] = '' # male hai :)

                    person['land'] = land
                    person['money'] = money
                    plist[name] =  person

            else:
                # starts with female : small  assumption 

                print("female")
                # Ms. Jass w/o Mr. Sinesh has purchased 12 acre land in 36000000/- only
                name = l.split(' w/o ')[0][4:]
                husband = l.split(' w/o ')[1].split(" has ")[0][4:]

                print(name,husband)

                if name in plist:
                    # just add money and land ++
                    plist[name]['money'] += money
                    plist[name]['land'] += land 
                    
                else:
                    # fresh female rec 
                    # TODO : fetch father if not available 
                    # TODO : fetch mother if not available 
                    # TODO : uske paas uske husband ki v jamin hogi ? 
                    person['husband'] = husband
                    person['land'] = land
                    person['money'] = money
                    plist[name] =  person
        

    pprint(plist)

'''

{'Akshayawat': {'des': {'Subham', 'Sinesh'}},
 'Anmol': {'des': 'Anuj', 'husband': '', 'land': 30, 'money': 100000000},
 'Anuj': {'husband': '', 'land': 10, 'money': 50000000},
 'Jass': {'husband': 'Sinesh', 'land': 12, 'money': 36000000},
 'Sinesh': {'des': 'Anmol',
            'father': 'Akshayawat',
            'husband': '',
            'land': 17.0,
            'money': 24000000.0},
 'Subham': {'father': 'Akshayawat', 'land': 7.0, 'money': 14000000.0},
 'ram': {}}

 '''

# stored data :) 

# traversal : 



# print('des' in plist['Sinesh'])
print('des' in plist['Jass'])

def get_des(plist, name):
    visited = set()
    stack = [name]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if ('des' in plist[vertex]):
                stack.extend(set(plist[vertex]['des']) - visited)
    return list(visited)


# def get_des(visited, plist, name): 

#     if name not in visited:
#         # self append
#         visited.append(name)
#         # all neighbour
#         print(plist[name]['des'])
#         visited.append(plist[name]['des'])
#         for neighbour in plist[name]['des']:
#             get_des(visited, plist, name)


print("working on query")


def main():

    # q = input() 
    q = "select * from plist where name = 'Sinesh'"
    # q = "select * from plist where name = 'Sinesh'"
    q = "select sum(land) from plist where name = 'Sinesh'"
    q = "select sum(wealth) from plist where FT = 'Sinesh'"
    q = "select sum(land) from plist where name = 'Anuj'"
    q = "select sum(land) from plist where name = 'Jass'"
    q = "select sum(land) from plist where name = 'Sinesh'"
    q = q.split()
    name = q[7][1:-1]

    if q[0].lower() != 'select':
        print("wrong query")
        return

    if q[1] == '*':
        # all_des = get_des(dictname, name )
        dictname  = q[3]

        print(plist[name]['money'])
        print(plist[name]['land'])


    else: 
        query = q[1]
        if( q[5] == 'FT'): 
            if query == 'sum(land)':
                total = 0
                # visited = []
                visited = get_des( plist, name)
                print(visited)
                for person in visited:
                    total += plist[person]['land']

                print( "Total land : " , total)
            elif query == 'sum(wealth)':
                total = 0
                visited = []
                visited = get_des(plist, name)
                print(visited)
                for person in visited:
                    total += plist[person]['money']

                print( "Total welth : " ,total)
  
        elif(q[5] == 'name'):
            if query == 'sum(land)':
                print( "Total land : " , plist[name]['land'])
            elif query == 'sum(wealth)':
                print( "Total welth : " ,plist[name]['money'])
        else:
            print("wrong query")
        
    # print(name, dictname)


    pass


main()
