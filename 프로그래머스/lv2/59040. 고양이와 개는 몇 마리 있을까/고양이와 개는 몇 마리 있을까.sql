/* Solved date
- 230918
*/
SELECT
    ANIMAL_TYPE
    , COUNT(*) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;