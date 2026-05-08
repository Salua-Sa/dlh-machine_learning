-- Displays the average temperature by city ordered by temperature descending.
SELECT city, AVG(temperature) AS avg_temp FROM temperature
GROUP BY city WHERE avg_temp DESC
