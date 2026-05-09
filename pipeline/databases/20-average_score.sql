-- Creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN users.id INT)
BEGIN
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = users.id;
  UPDATE users
  SET average_score = avg_score
  WHERE id = users.id ;
END //
DELIMITER ;
