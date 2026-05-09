-- Creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(5,2);

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    IF avg_score IS NULL THEN
        SELECT 'No scores found for this user.' AS message;
    END IF;

    UPDATE users
    SET average_score = avg_score,
    WHERE id = p_user_id
END$$

DELIMITER ;
