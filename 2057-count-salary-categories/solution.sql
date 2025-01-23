# Write your MySQL query statement below
WITH category_list AS (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
)
SELECT cl.category, 
       COALESCE(COUNT(a.account_id), 0) AS accounts_count
FROM category_list cl
LEFT JOIN (
    SELECT 
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        account_id
    FROM accounts
) a ON cl.category = a.category
GROUP BY cl.category;
