# Write your MySQL query statement below

select visits.customer_id,count(*) as count_no_trans from Visits where visit_id not in(Select distinct(Visits.visit_id) from Visits join Transactions where Visits.visit_id = Transactions.visit_id) group by visits.customer_id;