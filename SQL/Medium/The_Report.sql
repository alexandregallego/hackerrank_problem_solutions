SELECT CASE WHEN t2.grade >= 8 then t1.Name else 'NULL' end as Name, t2.grade, t1.marks
from students as t1
INNER JOIN grades as t2 On t1.marks >= t2.min_mark AND t1.marks <= t2.max_mark
order by grade desc, Name, marks;
