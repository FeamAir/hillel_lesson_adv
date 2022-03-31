/*
 Serch customers
 */
SELECT FirstName, LastName 
FROM customers
WHERE FirstName in ("Mark","Frank") or LastName  in ("Taylor","Harris");
