-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
DELIMITER //
BEGIN
    DECLARE avg_weighted_score
    SELECT SUM(score * weight) / SUM(weight)
    FROM corrections
    WHERE corrections.user_id = p_user_id;
    UPDATE users
    SET  average_score = avg_weighted_score
    WHERE id = p_user_id;
END //
DEÃLIMITER //
