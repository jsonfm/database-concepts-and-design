CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id),
    INDEX (email)
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
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TYPE friendship_request_status AS ENUM ('ACCEPTED', 'REJECTED');


CREATE TABLE IF NOT EXISTS friendships_requests (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_one_id INT NOT NULL,
    user_two_id INT NOT NULL,
    status VARCHAR(10),
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id),
    FOREIGN KEY (user_one_id) REFERENCES users(id),
    FOREIGN KEY (user_two_id) REFERENCES users(id),
    UNIQUE KEY unique_friendship_request_one_to_two (user_one_id, user_two_id),
    UNIQUE KEY unique_friendship_request_two_to_one (user_two_id, user_one_id)
);


CREATE TABLE IF NOT EXISTS friendships (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_one_id INT NOT NULL,
    user_two_id INT NOT NULL,
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id),
    FOREIGN KEY (user_one_id) REFERENCES users(id),
    FOREIGN KEY (user_two_id) REFERENCES users(id),
    UNIQUE KEY unique_friendship_one_to_two (user_one_id, user_two_id),
    UNIQUE KEY unique_friendship_two_to_one (user_two_id, user_one_id)
);


CREATE TABLE IF NOT EXISTS schools (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(255),
    country VARCHAR(45),
    type VARCHAR(10),
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS educations (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    title VARCHAR(255),
    start_year INT CHECK (start_year > 1900),
    end_year INT CHECK (end_year > 1900),
    user_id INT,
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS employers (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(255),
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS professional_positions (
    id INT AUTO_INCREMENT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    employer_id INT NOT NULL,
    user_id INT NOT NULL,
    job_title VARCHAR(255),
    deleted BOOLEAN DEFAULT false,
    active BOOLEAN DEFAULT false,
    PRIMARY KEY(id),
    FOREIGN KEY (employer_id) REFERENCES employers(id)
);