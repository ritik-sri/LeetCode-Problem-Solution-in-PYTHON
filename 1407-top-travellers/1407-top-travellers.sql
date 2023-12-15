# Write your MySQL query statement below

Select Users.name as name , COALESCE(SUM(Rides.distance), 0) as travelled_distance from Users left join Rides on Users.id=Rides.user_id group by Rides.user_id order by travelled_distance desc,name;

