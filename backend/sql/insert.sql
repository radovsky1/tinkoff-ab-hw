INSERT INTO users (id, name, email, biography, password)
VALUES ('123e4567-e89b-12d3-a456-426614174000', 'admin', 'admin@example.com', 'admin@example.com', 'admin');

INSERT INTO users (id, name, email, biography, password)
VALUES ('3fa85f64-5717-4562-b3fc-2c963f66afa6', 'user', 'user@example.com', 'user@example.com', 'user');

INSERT INTO friends (user_id, friend_id)
VALUES ('3fa85f64-5717-4562-b3fc-2c963f66afa6', '123e4567-e89b-12d3-a456-426614174000');