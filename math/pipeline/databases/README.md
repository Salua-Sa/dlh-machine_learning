This is directory containt 42 databases tasks:

 0-create_database_if_missing.sql creates the database db_0 in your MySQL server.

 1-first_table.sql creates a table called first_table in the current database in your MySQL server.

2-list_values.sql lists all rows of the table first_table in your MySQL server.

3-insert_value.sql inserts a new row in the table first_table in your MySQL server.

4-best_score.sql lists all records with a score >= 10 in the table second_table in your MySQL server.

5-average.sql computes the score average of all records in the table second_table in your MySQL server.

6-avg_temperatures.sql displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

7-max_state.sql displays the max temperature of each state (ordered by State name).

8-genre_id_by_show.sql lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

9-no_genre.sql lists all shows contained in hbtn_0d_tvshows without a genre linked.

10-count_shows_by_genre.sql lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

11-rating_shows.sql lists all shows from hbtn_0d_tvshows_rate by their rating.

12-rating_genres.sql lists all genres in the database hbtn_0d_tvshows_rate by their rating.

13-uniq_users.sql creates a table users.

14-country_users.sql creates a table users with enumeration of countries.

15-fans.sql ranks country origins of bands, ordered by the number of (non-unique) fans.

16-glam_rock.sql lists all bands with Glam rock as their main style, ranked by their longevity.

17-store.sql creates a trigger that decreases the quantity of an item after adding a new order.

18-valid_email.sql creates a trigger that resets the attribute valid_email only when the email has been changed.

19-bonus.sql creates a stored procedure AddBonus that adds a new correction for a student.

20-average_score.sql creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.

21-div.sql creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

22-list_databases lists all databases in MongoDB.

23-use_or_create_database creates or uses the database my_db.

24-insert inserts a document in the collection school.

25-all lists all documents in the collection school.

26-match lists all documents with name="Holberton school" in the collection school.

27-count displays the number of documents in the collection school.

28-update adds a new attribute to a document in the collection school.

29-delete deletes all documents with name="Holberton school" in the collection school.

30-all.py lists all documents in a collection.

31-insert_school.py inserts a new document in a collection based on kwargs.

32-update_topics.py changes all topics of a school document based on the name.

33-schools_by_topic.py returns the list of school having a specific topic.

34-log_stats.py provides some stats about Nginx logs stored in MongoDB.

100-index_my_names.sql creates an index idx_name_first on the table names and the first letter of name.

101-index_name_score.sql creates an index idx_name_first_score on the table names and the first letter of name and the score.

102-need_meeting.sql creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

103-average_weighted_score.sql creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

104-find lists all documents with name starting by Holberton in the collection school.

105-students.py returns all students sorted by average score.

106-log_stats.py Improve 34-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs.
