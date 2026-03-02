-- Last updated: 02/03/2026, 14:02:05
SELECT name 
FROM Customer
WHERE COALESCE(referee_id, 0) != 2;