orders = [
    {
        'id': 101,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'Ravi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'Meera',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]

def analyse(orders):

    revenue = {}
    product_count = {}
    customer_status = {}

    for order in orders:

        customer = order['customer']
        status = order['status']

        if customer not in customer_status:
            customer_status[customer] = []

        customer_status[customer].append(status)

        if status != 'CANCELLED':

            for product, quantity, price in order['items']:

                amount = quantity * price

                if customer not in revenue:
                    revenue[customer] = 0

                revenue[customer] += amount

                if product not in product_count:
                    product_count[product] = 0

                product_count[product] += quantity

    top_products = sorted(
        product_count.items(),
        key=lambda x: (-x[1], x[0])
    )[:2]

    fully_delivered = sorted([
        customer
        for customer, statuses in customer_status.items()
        if all(status == 'DELIVERED' for status in statuses)
    ])

    result = {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }

    return result

result = analyse(orders)

print(result)