EXPLAIN ANALYZE SELECT id, name, last_login
FROM users JOIN friends ON friends.user_id = 'ce692cd0-5581-4584-bc95-88f68a996387'
WHERE users.id = friends.friend_id
ORDER BY last_login DESC;


-- INDEXES
CREATE INDEX users_id_name_last_login_desc_idx ON users (id, name, last_login desc);
CREATE INDEX idx_friends_friend_user ON friends (friend_id, user_id);
CREATE INDEX friends_friend_id ON friends(friend_id);
CREATE INDEX friends_user_id ON friends(user_id);


