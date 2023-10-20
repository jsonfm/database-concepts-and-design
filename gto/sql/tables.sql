CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    active BOOLEAN DEFAULT true,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS profiles (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    sex CHAR(1),
    birthday DATETIME,
    current_city VARCHAR(255),
    hometown VARCHAR(255),
    user_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS friendships (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_one_id INT NOT NULL,
    user_two_id INT NOT NULL,
    request_user_one_status VARCHAR(30) DEFAULT 'PENDING',
    request_user_one_updated_at TIMESTAMP,
    request_user_two_status VARCHAR(30) DEFAULT 'PENDING',
    request_user_two_updated_at TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_one_id) REFERENCES users(id),
    FOREIGN KEY (user_two_id) REFERENCES users(id),
    UNIQUE KEY unique_friendship_one_to_two (user_one_id, user_two_id),
    UNIQUE KEY unique_friendship_tow_to_one (user_two_id, user_one_id)
);