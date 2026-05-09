-- Creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student.
CREATE PROCEDURE ComputeAverageScoreForUser (IN users_id INT)
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = users_id;
  UPDATE users
  SET average_score = avg_score
  WHERE id = users_id ;
