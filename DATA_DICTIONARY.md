# Data Dictionary - synthetic_processing_data.csv

| Column                | Description                          | Type    |
|-----------------------|--------------------------------------|---------|
| record_id             | Unique record identifier             | int     |
| submission_date       | Date record entered                  | date    |
| case_type             | Type of case                         | string  |
| priority              | Priority level                       | string  |
| old_predicted_days    | Original estimated processing time   | int     |
| optimized_predicted_days | Model-predicted time after optimization | int  |
| actual_days           | Real processing time                 | int     |
| compliance_flag       | Regulatory compliance check          | int     |
| bias_risk_score       | Bias mitigation score (0-1)          | float   |
