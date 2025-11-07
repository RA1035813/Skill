# USE SKILL;
# # de inserts en Queries zijn geschreven door AI
# -- 1️⃣ eerst AfvalType
# INSERT INTO AfvalType (id, type, gewicht, tijd) VALUES
#     (1, 'Plastic', 5, '2025-11-03 10:30:00'),
#     (2, 'Papier',  3, '2025-11-04 14:10:00'),
#     (3, 'Glas',    8, '2025-11-06 09:45:00');
#
# -- 2️⃣ daarna Afval, met dezelfde id’s als AfvalType
# INSERT INTO Afval (id) VALUES
#        (1),
#        (2),
#        (3);
#
# -- 3️⃣ daarna Users, met dezelfde id’s als Afval
# INSERT INTO Users (id, userName, score, administrator) VALUES
#    (1, 'TestUser',   100, FALSE),
#    (2, 'dwaas',    80,  FALSE),
#    (3, 'Admin',   0,   TRUE);
#
# -- test
# SELECT
#     u.userName,
#     t.type AS afvaltype,
#     t.gewicht,
#     t.tijd
# FROM Users u
#          JOIN Afval a ON u.id = a.id
#          JOIN AfvalType t ON a.id = t.id
# ORDER BY u.userName;

-- Eerst Users invoegen
INSERT INTO Users (userName, score, administrator) VALUES
   ('Alice', 0, FALSE),
   ('Bob', 0, FALSE),
   ('Charlie', 0, FALSE);

-- Dan AfvalType invoegen
INSERT INTO AfvalType (type, gewicht, tijd) VALUES
    ('Plastic', 5, '2025-11-01 12:00:00'),
    ('Metaal', 10, '2025-11-02 15:00:00'),
    ('Papier', 2, '2025-11-03 09:30:00');

-- Nu Afval invoegen met verwijzing naar bestaande Users en AfvalType
INSERT INTO Afval (type_id, user_id) VALUES
     (1, 1),  -- Alice heeft Plastic
     (2, 1),  -- Alice heeft Metaal
     (3, 2),  -- Bob heeft Papier
     (1, 3);  -- Charlie heeft Plastic

INSERT INTO AfvalType (type, gewicht, tijd) VALUES
    ('Plastic', 5, '2025-11-01 12:00:00'),
    ('Metaal', 10, '2025-11-15 09:00:00');
-- test
SELECT
    u.userName,
    t.type AS afvaltype,
    t.gewicht,
    t.tijd
FROM Users u
         JOIN Afval a ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
ORDER BY u.userName;



