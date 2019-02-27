
"""
There are four collection data types in the Python programming language:

List    []       is a collection which is ordered and changeable. Allows duplicate members.
Tuple   ()       is a collection which is ordered and unchangeable. Allows duplicate members.
Set     {}       is a collection which is unordered and unindexed. No duplicate members.
Dictionary   {}  is a collection which is unordered, changeable and indexed. No duplicate members.



"""

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
        "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
        "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
        "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
        "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
        "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}           
         }

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]


ratings1 = {
            "Arkadiusz": (2,1,2,3,2,3),
            "Agness": (4,2,1,3,4)           
           }    
ratings2 = [
        {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
    ]

ratings3 = {
        "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        "Agness:": {'ratings': (4,2,1,3,4), 'behaviour': 2}
    }



"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]
for name, age, sex in ppllist2:
    print(name)

"""
