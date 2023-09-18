/* Solved date
- 230918
*/
SELECT
    CASE
        WHEN CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) < 10 THEN RIGHT(DATE_FORMAT(DATETIME, '%H'), 1)
        ELSE DATE_FORMAT(DATETIME, '%H')
    END AS 'HOUR'
    , COUNT(*) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) >= 9
    AND CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) < 20
GROUP BY DATE_FORMAT(DATETIME, '%H')
ORDER BY CAST(HOUR AS SIGNED);
