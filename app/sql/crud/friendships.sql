-- All friendships

SELECT DISTINCT 
    F.user_one_id, 
    F.user_two_id, 
    U1.email AS email_1, 
    U2.email AS email_2
FROM
    friendships AS F
INNER JOIN
    users AS U1
ON
    F.user_one_id=U1.id
INNER JOIN
    users AS U2
ON
    F.user_two_id=U2.id;

--  Single
SELECT DISTINCT 
    F.user_one_id, 
    F.user_two_id, 
    U1.email AS email_1, 
    U2.email AS email_2,
    P.first_name
FROM
    friendships AS F
INNER JOIN
    users AS U1
ON
    F.user_one_id=U1.id
INNER JOIN
    users AS U2
ON
    F.user_two_id=U2.id
INNER JOIN
    profiles AS P
ON
    P.user_id=U2.id
WHERE F.user_one_id=1;    

