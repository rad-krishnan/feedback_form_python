CREATE DATABASE feedback_db;

USE feedback_db;

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255),
    email_address VARCHAR(255),
    phone_number VARCHAR(15),
    product_name VARCHAR(255),
    purchase_date DATE,
    product_quality ENUM('excellent', 'good', 'average', 'poor', 'very_poor'),
    expectations_met ENUM('exceeded', 'met', 'somewhat_met', 'not_met'),
    ease_of_use ENUM('very_easy', 'somewhat_easy', 'neutral', 'somewhat_difficult', 'very_difficult'),
    recommendation ENUM('definitely', 'probably', 'unsure', 'probably_not', 'definitely_not'),
    likes TEXT,
    dislikes TEXT,
    comments TEXT,
    follow_up ENUM('yes', 'no')
);
