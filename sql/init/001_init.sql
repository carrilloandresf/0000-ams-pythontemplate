CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

DROP PROCEDURE IF EXISTS get_user_count;
DROP PROCEDURE IF EXISTS get_user_stats;

DELIMITER //
CREATE PROCEDURE get_user_count()
BEGIN
    SELECT COUNT(*) AS user_count FROM users;
END //

CREATE PROCEDURE get_user_stats(IN user_id_param INT)
BEGIN
    SELECT id, name, email FROM users WHERE id = user_id_param;
END //
DELIMITER ;
