DROP DATABASE IF EXISTS composeapp;
CREATE DATABASE composeapp;
CREATE TABLE composeapp.applications(
    id VARCHAR(6) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    owner VARCHAR(6) NOT NULL,
    created_at DATETIME NOT NULL,
    deleted_at DATETIME DEFAULT NULL,
    last_build DATETIME DEFAULT NULL
);
CREATE TABLE composeapp.application_settings(
    app_id VARCHAR(6) NOT NULL,
    repo_provider VARCHAR(255),
    repo_user VARCHAR(255),
    repo_name VARCHAR(255),
    repo_is_public INT DEFAULT 0
);
CREATE TABLE composeapp.users(
    id VARCHAR(6) PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    github_token VARCHAR(255),
    created_at DATETIME,
    deleted_at DATETIME DEFAULT NULL,
    last_access DATETIME DEFAULT NULL
);