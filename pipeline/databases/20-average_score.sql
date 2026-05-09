-- Creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser //
CREATE PROCEDURE ComputeAverageScoreForUser (IN student_id INT)
BEGIN
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = student_id;
  UPDATE users
  SET average_score = avg_score
  WHERE id = student_id;
END //
DELIMITER ;
