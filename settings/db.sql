DROP TABLE IF EXISTS applications;
CREATE TABLE applications(
    id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    desc TEXT,
    repository VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    last_build DATETIME NOT NULL
);

DROP TABLE IF EXISTS build_histories;
CREATE TABLE build_histories(
    build_id VARCHAR(255),
    app_id VARCHAR(255),
    built_at DATETIME NOT NULL,
    code INT DEFAULT 0
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
    id VARCHAR(255) PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    role VARCHAR(255)
);
