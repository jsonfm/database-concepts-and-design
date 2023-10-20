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