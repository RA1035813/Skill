# de inserts en Queries zijn geschreven door AI


-- Query: Toon per user welke afvaltypes en totalen
SELECT
    u.userName,
    t.type AS afvaltype,
    t.gewicht,
    DATE_FORMAT(t.tijd, '%Y-%m') AS maand
FROM Users u
         JOIN Afval a ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
ORDER BY u.userName, maand;

-- Query: Totaalgewicht per maand (op basis van je schema)
SELECT
    DATE_FORMAT(t.tijd, '%Y-%m') AS maand,
    SUM(t.gewicht) AS totaal_gewicht
FROM Users u
         JOIN Afval a ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
GROUP BY maand
ORDER BY maand;

-- overzicht van user, afvaltype en gewicht
SELECT
    u.userName,
    t.type,
    t.gewicht,
    DATE_FORMAT(t.tijd, '%Y-%m') AS maand
FROM Users u
         JOIN Afval a   ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
ORDER BY u.userName, maand;

-- totaalgewicht per maand over alle users
# SELECT
#     DATE_FORMAT(t.tijd, '%Y-%m') AS maand,
#     SUM(t.gewicht) AS totaal_gewicht
# FROM Users u
#          JOIN Afval a   ON u.id = a.id
#          JOIN AfvalType t ON a.id = t.id
# GROUP BY maand
# ORDER BY maand;

-- Userdata
SELECT
    u.userName,
    t.type AS afvaltype,
    t.gewicht,
    t.tijd
FROM Users u
         JOIN Afval a ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
WHERE u.userName = 'TestUser'                --  specifieke gebruiker
  AND DATE_FORMAT(t.tijd, '%Y-%m') = '2025-11'  --  specifieke maand (YYYY-MM)
ORDER BY t.tijd;


# -- Userdata
# SELECT
#     u.userName,
#     t.type AS afvaltype,
#     t.gewicht,
#     t.tijd
# FROM Users u
#          JOIN Afval a ON u.id = a.id
#          JOIN AfvalType t ON a.id = t.id
# WHERE u.userName = 'Alice'                --  specifieke gebruiker
#   AND DATE_FORMAT(t.tijd, '%Y-%m') = '2025-11'  --  specifieke maand (YYYY-MM)
# ORDER BY t.tijd;


SELECT u.userName, t.type, t.gewicht, DATE_FORMAT(t.tijd, '%Y-%m') AS maand
FROM Users u
    JOIN Afval a   ON u.id = a.id
    JOIN AfvalType t ON a.id = t.id ORDER BY u.userName, maand;

-- inserts
