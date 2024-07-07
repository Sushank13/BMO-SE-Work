DELIMITER //
CREATE PROCEDURE insertDecryptedFileContent(IN file_name VARCHAR(255), IN file_content VARCHAR(255))
BEGIN
INSERT INTO decrypted_file_content (file_name, content) VALUES (file_name, file_content);
END //
DELIMITER ; 