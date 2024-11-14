CREATE DATABASE IF NOT EXISTS media_tracker_db;
USE media_tracker_db;

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Anime Table
CREATE TABLE IF NOT EXISTS anime (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    episodes INT,
    genre VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Manga Table
CREATE TABLE IF NOT EXISTS manga (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    chapters INT,
    genre VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Completed Table: Tracks completed items by each user
CREATE TABLE IF NOT EXISTS completed (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    anime_id INT,
    manga_id INT,
    completed_date DATE,
    UNIQUE (user_id, anime_id),
    UNIQUE (user_id, manga_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (anime_id) REFERENCES anime(id),
    FOREIGN KEY (manga_id) REFERENCES manga(id)
);

-- Plan to Watch/Read Table: Tracks items a user plans to watch/read
CREATE TABLE IF NOT EXISTS plan_to (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    anime_id INT,
    manga_id INT,
    planned_date DATE,
    UNIQUE (user_id, anime_id),
    UNIQUE (user_id, manga_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (anime_id) REFERENCES anime(id),
    FOREIGN KEY (manga_id) REFERENCES manga(id)
);

-- Currently Watching Table: Tracks items a user is currently watching/reading
CREATE TABLE IF NOT EXISTS currently_watching (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    anime_id INT,
    manga_id INT,
    started_date DATE,
    UNIQUE (user_id, anime_id),
    UNIQUE (user_id, manga_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (anime_id) REFERENCES anime(id),
    FOREIGN KEY (manga_id) REFERENCES manga(id)
);

-- Ensure exclusivity by setting a unique constraint on the combination of user_id, anime_id, and manga_id across lists
-- so that an item cannot appear in more than one list at a time for a user.

