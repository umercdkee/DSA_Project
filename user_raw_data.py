from avl_tree import*

users_data = [
    ['admin','admin'],
    ['umercdkee','umer123'],
    ['chris789', 'D6qN1u$yR*p'],
    ['mike2024', 'P5gF@8wNl'],
    ['john2025', 'X7@bR2dF!o'],
    ['emily2022', 'T1kW3z@fV*p'],
    ['alex2023', 'L2jM5q#vN'],
    ['olivia2026', 'C4zE%9tG!o'],
    ['emma2026', 'B@zH6x9LqS'],
    ['david789', 'H1kY7p@tVl'],
    ['john123', 'N8#mP2qD'],
    ['sophia789', 'S4yN5kE!gA'],
    ['isabella2024', 'M3#dE5xGkY'],
    ['emma2025', 'Z5jK@3hGqL'],
    ['mike2026', 'V@kN7p5Hw'],
    ['olivia2023', 'R3mC7@xG!l'],
    ['sophia2023', 'H7bY8fK@lG'],
    ['emily2023', 'G7dK#6wTzE'],
    ['david456', 'F6uP#7z@qA'],
    ['alex2022', 'W@oE4j8mHs'],
    ['isabella789', 'P1vY7nD&zB']
]

users_database=None
for i in users_data:
    users_database=insert(users_database,i[0],{"Username":i[0], "Password":i[1], "Books Borrowed":[],"Fines Due":0})