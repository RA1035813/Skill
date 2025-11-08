use SKILL;
DROP TABLE if exists SKILL.Afval;
DROP TABLE if exists SKILL.Users;
DROP TABLE if exists SKILL.AfvalType;

CREATE TABLE SKILL.AfvalType(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  type VARCHAR(255) NOT NULL,
  gewicht INT NOT NULL,
  tijd DATETIME NOT NULL
);
CREATE TABLE SKILL.Users(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(255) NOT NULL UNIQUE,
    score BIGINT NULL,
    administrator BOOLEAN NOT NULL
);


CREATE TABLE SKILL.Afval(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  type_id INT UNSIGNED NOT NULL,
  user_id INT UNSIGNED NOT NULL,
  FOREIGN KEY (type_id) REFERENCES AfvalType(id),
  FOREIGN KEY (user_id) REFERENCES Users(id)
);

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
