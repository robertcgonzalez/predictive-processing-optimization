-- CTE for backlog trends + window function for rolling average
WITH daily_backlog AS (
    SELECT 
        submission_date,
        COUNT(*) as new_records,
        AVG(actual_days) OVER (ORDER BY submission_date ROWS BETWEEN 30 PRECEDING AND CURRENT ROW) as rolling_avg_days
    FROM synthetic_processing_data
    GROUP BY submission_date
)
SELECT 
    submission_date,
    new_records,
    rolling_avg_days,
    CASE WHEN rolling_avg_days > 30 THEN 'High Risk - Prioritize' ELSE 'On Track' END as alert
FROM daily_backlog
ORDER BY submission_date DESC;
