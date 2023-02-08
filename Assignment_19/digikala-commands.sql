--  Insert
INSERT INTO Costomers(id, name, city, country)
VALUES(1, 'Ali', 'Mashhad', 'Iran')

INSERT INTO Products(id, name, price, count)
VALUES(1, 'Laptop', 21500000, 5)

--  Select 
SELECT * FROM Products
WHERE count != 0

--  Delete
DELETE FROM Costomers
WHERE country != 'Iran'

--  Update
UPDATE Products
SET price = price * 0.80
