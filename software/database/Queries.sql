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
SELECT
    DATE_FORMAT(t.tijd, '%Y-%m') AS maand,
    SUM(t.gewicht) AS totaal_gewicht
FROM Users u
         JOIN Afval a   ON u.id = a.id
         JOIN AfvalType t ON a.id = t.id
GROUP BY maand
ORDER BY maand;
