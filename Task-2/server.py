from weasyprint import HTML
import datetime

# 1. Dynamic invoice data
data = {
    "invoice_no": "00126",
    "date": datetime.date.today().strftime("%B %d, %Y"),
    "customer_name": "Alice Tan",
    "items": [
        {"description": "Website Design", "qty": 1, "price": 500},
        {"description": "Hosting (1 year)", "qty": 1, "price": 100},
        {"description": "Domain Name (1 year)", "qty": 1, "price": 15},
        {"description": "SEO Optimization", "qty": 1, "price": 250},
        {"description": "Email Setup", "qty": 3, "price": 20},
    ],
    "tax_rate": 0.06
}

# 2. Build table HTML dynamically
items_html = ""
subtotal = 0
for item in data["items"]:
    total = item["qty"] * item["price"]
    subtotal += total
    items_html += f"""
        <tr>
            <td>{item['description']}</td>
            <td>{item['qty']}</td>
            <td>RM{item['price']:.2f}</td>
            <td>RM{total:.2f}</td>
        </tr>
    """

tax = subtotal * data["tax_rate"]
total_due = subtotal + tax

# 3. Final HTML with professional styles
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            color: #333;
            background-color: #fff;
        }}
        .header {{
            text-align: center;
            color: #005BAC;
            margin-bottom: 30px;
        }}
        .header h1 {{
            margin-bottom: 5px;
            font-size: 28px;
        }}
        .header p {{
            font-size: 14px;
            color: #666;
        }}
        .info {{
            margin-bottom: 30px;
        }}
        .info p {{
            margin: 5px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        th {{
            background-color: #005BAC;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        td {{
            border: 1px solid #ddd;
            padding: 10px;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .totals {{
            text-align: right;
            margin-top: 20px;
        }}
        .totals h2 {{
            margin: 5px 0;
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>INVOICE</h1>
        <p>Professional Billing - Malaysia</p>
    </div>

    <div class="info">
        <p><strong>Invoice No:</strong> {data['invoice_no']}</p>
        <p><strong>Date:</strong> {data['date']}</p>
        <p><strong>Customer:</strong> {data['customer_name']}</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>Description</th>
                <th>Qty</th>
                <th>Unit Price (RM)</th>
                <th>Total (RM)</th>
            </tr>
        </thead>
        <tbody>
            {items_html}
        </tbody>
    </table>

    <div class="totals">
        <h2>Subtotal: RM{subtotal:.2f}</h2>
        <h2>Tax (6%): RM{tax:.2f}</h2>
        <h2><strong>Total Due: RM{total_due:.2f}</strong></h2>
    </div>
</body>
</html>
"""

# 4. Generate PDF
filename = f"invoice_{data['invoice_no']}.pdf"
HTML(string=html_content).write_pdf(filename)

print(f"✅ Professional invoice PDF generated as '{filename}'")
