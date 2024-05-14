select c.login,
       count(o.id) as quantity_orders
from "Orders" as o
inner join "Couriers" as c on o."courierId"=c.id
where o."inDelivery"=true
group by c.login;




select track,
       case
         when finished=true then '2'
         when cancelled=true then '-1'
         when "inDelivery"=true then '1'
         else '0'
       end
from "Orders";