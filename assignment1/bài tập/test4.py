price_of_a_book=24.95
discount=0.4
the_first_shipping_cost=3
shipping_cost=0.75
copies=60

total_before_discount=price_of_a_book*copies

total_after_discount=total_before_discount*(1-discount)

total_shipping_cost=the_first_shipping_cost+shipping_cost*(copies-1)

total_wholesale=total_after_discount+total_shipping_cost

print("The total wholesale:  ", round(total_wholesale,2))