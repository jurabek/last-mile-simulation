
Last mile delivery and Pick up (from Depot to destination) depending on different product categories in Python with `simpy` Library. So the task is a following requirement:

Input from User:
- Number of AMRS
- Population density (1-100%) 
- Number of Customers (in that Population)
- Amr capacity ()

There are customers spread out based on population density and each of them can place an Order. The customer order has different categories with priorities:

- `groceries: priority 1`
- `pharmaceutics: priority 1` 
- `flowers: priority 2`
- `electronic: priority 3` 
- `clothes: priority 4`
- `retour electronics: prio 3`
- `retour clothes: prio 4`
- `organic waste: prio 1`
- `residual waste: prio 2`
- `other waste: prio 3`

Depot is a class, in which all `AMRS` are located and it can accept random orders from random customers, and they are stored in the `Order Queue` but those with high priority go into front. Orders are distributed to different AMRS and filled randomly (e.g. delivery time in 5 mins) and then to be delivered to the customers (Generated randomly and have random distances to Depot).

Like different arrival times. Or an order to pick up something from a customer (retour or waste), so they leave the depot immediately and then take 10 minutes to load the stuff and bring it back to the depot. Or better to separate that the rubbish would be taken to another point and returned B depot. 
Or if there is an order for a pop and then you can pick it up and take it away at once, which would waste less time than sending a new AMR from the depot.

Also, distances / driving time to customers should be set randomly and amrs should be able to deliver Many customers at once whichever are closest to each other If there are orders with low priority and AMRs are not full then AMRs should wait for 1 hour before delivering in case other orders come in and then can deliver all at once.

If there are orders with low priority and amrs are not full then amrs should wait for 1 hour before delivering in case other orders come in and then can deliver all at once.

The goal is => safe as much time as possible/ make as many deliveries as possible.

Example of the output of the simulation:
```
Order #4 of type ‘groceries‘ has been placed by customer 1, at time 76 
(=01:16am) 
AMR #1 has loaded order #4 at time 81
AMR #1 has left depot at time 81
AMR #1 has arrived at customer #1 at time 145
Order #2 has been placed by customer #2 at time 146
AMR #2 has loaded order #2 at time 151
AMR #2 is waiting for another order
AMR dropped order #4 by costumer #1 at time 155
AMR #1 is back in depot at time 224
(After 60 minutes waiting and no new order)
AMR #2 has left depot at time X
```

For example: 
Customers makes an order to pickup or to be delivered. And there are different categories, e.g garbage is taken out not so often so that possibility 20% for this Order Type, and maybe clothes will order 60%, and also capacity of AMR and product volume, like AMR waits for products until it is not filled to 70% and only then will go if the products have low priority, and if high as for medicines, then immediately leaves. And it drives like by traveling salesman algorithm.
