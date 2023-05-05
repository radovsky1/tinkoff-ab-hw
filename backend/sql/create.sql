CREATE TABLE IF NOT EXISTS users
(
    id         UUID PRIMARY KEY,
    name TEXT                     NOT NULL,
    email TEXT                     NOT NULL,
    bio TEXT                     NOT NULL,
    password   TEXT                     NOT NULL,
    created    TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS friends
(
    user_id UUID REFERENCES users (id) ON DELETE CASCADE NOT NULL,
    friend_id UUID REFERENCES users (id) ON DELETE CASCADE NOT NULL,
    created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (user_id, friend_id)
);