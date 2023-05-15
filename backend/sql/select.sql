SELECT id, name, email, bio, password
FROM users WHERE id = '123e4567-e89b-12d3-a456-426614174000';

SELECT *
FROM friends WHERE user_id = '123e4567-e89b-12d3-a456-426614174000';

SELECT *
FROM users;

-- hw4 Добавить запрос на выборку друзей пользователя, сортировка по дате последнего логина

SELECT id, name, last_login
FROM users JOIN friends ON users.id = friends.friend_id
WHERE friends.user_id = '123e4567-e89b-12d3-a456-426614174000'
ORDER BY last_login DESC;