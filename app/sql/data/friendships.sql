INSERT INTO friendships
    (user_one_id, user_two_id)
VALUES 
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (6, 1);


INSERT INTO friendships_requests 
(user_one_id, user_two_id, status)
VALUES
(1, 2, 'ACCEPTED'),
(1, 3, 'ACCEPTED'),
(1, 4, 'ACCEPTED'),
(2, 3, 'ACCEPTED'),
(2, 4, 'ACCEPTED'),
(2, 5, 'ACCEPTED'),
(3, 4, 'ACCEPTED'),
(3, 5, 'ACCEPTED'),
(6, 1, 'ACCEPTED'),
(1, 5, 'REJECTED'),
(1, 6, 'REJECTED'),
(2, 1, 'REJECTED'),
(6, 3, 'REJECTED');