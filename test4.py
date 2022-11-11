# person = {name: , father: , mother: , husband:  land: , money: ,  6}

# plist = {'ram' : { father: , mother: , husband:  land: , money: } }
plist = {'ram' : {}}



from pprint import pprint


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

                        person['father'] = father
                        # TODO : create father's dict if not available 
        
                    else:
                        mother = l.split(' s/o ')[1].split(" has ")[0][4:]
                        print(name,mother)
                        person['mother'] = mother
                        # TODO : create mother's dict if not available 

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
    

