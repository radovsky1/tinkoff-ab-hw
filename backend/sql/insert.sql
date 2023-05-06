INSERT INTO users (id, name, email, bio, password)
VALUES ('123e4567-e89b-12d3-a456-426614174000', 'admin', 'admin@example.com', 'admin@example.com', 'admin');

INSERT INTO users (id, name, email, bio, password)
VALUES ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'user', 'user@example.com', 'user@example.com', 'user');

INSERT INTO friends (user_id, friend_id)
VALUES ('3fa85f64-5717-4562-b3fc-2c963f66afa6', '123e4567-e89b-12d3-a456-426614174000');

INSERT INTO friends (user_id, friend_id)
SELECT 'a748e658-575b-405a-8d4e-1d8192b40e23', id
FROM users
WHERE id <> 'a748e658-575b-405a-8d4e-1d8192b40e23';