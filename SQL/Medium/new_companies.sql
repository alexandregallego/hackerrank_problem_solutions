/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT t1.company_code, t1.founder, count(distinct(t2.lead_manager_code)), count(distinct(t3.senior_manager_code)), count(distinct(t4.manager_code)), count(distinct(t5.employee_code))
FROM company t1
LEFT JOIN lead_manager t2 ON t1.company_code = t2.company_code
left join senior_manager t3 ON t1.company_code = t3.company_code
left join manager t4 ON t1.company_code = t4.company_code
left join employee t5 ON t1.company_code = t5.company_code
group by t1.company_code, t1.founder
order by company_code ASC;
