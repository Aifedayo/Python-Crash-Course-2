import random, time


team_mates = ['mushrah', 'noyad', 'salami', 'codedbashir', 'thesmathub', 'kaybee', 'zee', 'samad', 'salakoa','sulayman']
present_team_mates = ['mushrah', 'zee', 'noyad', 'codedbashir', 'thesmathub', 'samad', 'salakoA', 'sulayman', 'kaybee']

if len(present_team_mates) < len(team_mates):
    team_mate = random.sample(present_team_mates, k=(len(present_team_mates)))


else:
    team_mate = random.sample(team_mates, k=len(team_mates))

def python_class(*args):
    with open('question.txt', mode='r') as my_question:
        content = ''.join(my_question.readlines()).split('\n')
        questions = random.sample(content, len(team_mate))
    
    # index_list = ['[-4:15]', '[::2]', '[:10]', '[3:12]', '[:10]', '[::]', '[10:]']
    # index_list = random.sample(index_list, len(team_mate))
    
    print("Using the given index, what will each of the statement return?")
    names = [name for name in team_mate]
    
    quests = [question for question in questions]
    

    for item in zip(names, quests):
        print(item)


#python_class(team_mate)
