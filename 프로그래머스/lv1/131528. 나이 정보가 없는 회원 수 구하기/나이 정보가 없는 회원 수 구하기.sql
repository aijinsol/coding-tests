/* Solved date
- 230816
*/
SELECT
    COUNT(USER_ID) AS 'USERS'
FROM USER_INFO
WHERE
    AGE IS NULL;