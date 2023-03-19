-- groups
SELECT score, COUNT(*) as number
FROM second_table
GROUP by score
ORDER by number DESC;
