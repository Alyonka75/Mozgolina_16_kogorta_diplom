select c.login,
       count(o.id) as quantity_orders
from "Couriers" as c
left join  "Orders" as o on c.id=o."courierId" and o."inDelivery"=true
group by c.login;




select track,
       case
         when finished=true then '2'
         when cancelled=true then '-1'
         when "inDelivery"=true then '1'
         else '0'
       end
from "Orders";