-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
select city, AVG(value) AS avg_temp from temperatures GROUP BY city ORDER BY avg_temp desc;
