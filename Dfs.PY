graph = {'Akshayawat': {'des': {'Subham', 'Sinesh'}},
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

st = []
st.append(list(graph['Sinesh'][].keys())[0])
visited = []

while st != []:
    node = st.pop()
    print(node)
    visited.append(node)
    for adjnode in graph[node]:
        if adjnode not in visited:
            st.append(adjnode)

