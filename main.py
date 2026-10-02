def create_receipt(event):

    total = 0
    receipt_text = "<h3>Order Receipt</h3>"

    # Big Mac
    if document.querySelector("#bigmac").checked:
        qty = int(document.querySelector("#bigmac_qty").value)
        price = 189
        total = total + (price * qty)
        receipt_text += f"Big Mac x{qty} = ₱{price * qty}<br>"

    # Chicken
    if document.querySelector("#chicken").checked:
        qty = int(document.querySelector("#chicken_qty").value)
        price = 115
        total = total + (price * qty)
        receipt_text += f"Chicken McDo x{qty} = ₱{price * qty}<br>"

    # Cheeseburger
    if document.querySelector("#cheeseburger").checked:
        qty = int(document.querySelector("#cheeseburger_qty").value)
        price = 89
        total = total + (price * qty)
        receipt_text += f"Cheeseburger x{qty} = ₱{price * qty}<br>"

    # Fries
    if document.querySelector("#fries").checked:
        qty = int(document.querySelector("#fries_qty").value)
        price = 75
        total = total + (price * qty)
        receipt_text += f"Fries x{qty} = ₱{price * qty}<br>"

    # McFlurry
    if document.querySelector("#mcflurry").checked:
        qty = int(document.querySelector("#mcflurry_qty").value)
        price = 69
        total = total + (price * qty)
        receipt_text += f"McFlurry x{qty} = ₱{price * qty}<br>"

    # Iced Coffee
    if document.querySelector("#coffee").checked:
        qty = int(document.querySelector("#coffee_qty").value)
        price = 65
        total = total + (price * qty)
        receipt_text += f"Iced Coffee x{qty} = ₱{price * qty}<br>"

    # Coca-Cola
    if document.querySelector("#coke").checked:
        qty = int(document.querySelector("#coke_qty").value)
        price = 55
        total = total + (price * qty)
        receipt_text += f"Coca-Cola x{qty} = ₱{price * qty}<br>"

    receipt_text += f"<hr><b>Total: ₱{total}</b>"

    receipt = document.querySelector("#receipt")

    receipt.innerHTML = receipt_text
    receipt.style.display = "block"


def generate_sku(event):

    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    stock = document.querySelector("#stock").value

    if product == "" or stock == "":
        document.querySelector("#sku_result").innerHTML = "Please complete all fields."
        return

    # Get first 3 letters of product name
    product_code = product.upper().replace(" ", "")[:3]

    # Create a random number
    number = random.randint(100, 999)

    # Create the SKU
    sku = f"{category}-{product_code}-{stock}-{number}"

    document.querySelector("#sku_result").innerHTML = (
        f"<b>Generated SKU:</b><br><br>"
        f"<span style='font-size:25px; color:#d92316;'>{sku}</span>"
    )