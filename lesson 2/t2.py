import json


def write_order_to_json(**kwargs):
    with open("orders.json") as f:
        orders = json.load(f)

    orders.append(kwargs)

    assert ("item" in kwargs)
    assert ("quantity" in kwargs)
    assert ("price" in kwargs)
    assert ("buyer" in kwargs)
    assert ("date" in kwargs)

    assert (len(kwargs.keys()) == 5)

    with open("orders.json", "w") as f:
        f.write(json.dumps(orders, sort_keys=True, indent=4))


write_order_to_json(item="test", quantity=12, price=1.444, buyer="Buyer 1", date="12.04.04")
write_order_to_json(
    **{
        "item": "test 2",
        "quantity": 44,
        "price": 9.444,
        "buyer": "Buyer 2",
        "date": "22.09.05"
    }
)
