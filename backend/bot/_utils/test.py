sheet_data = [{
    "timestamp": "09-04-2019",
    "value": "10.0",
    "company_name": "Xbox",
    "product": "Buy"
}, {
    "timestamp": "09-03-2019",
    "value": "2.0",
    "company_name": "something",
    "product": "Sell"
}]

headers = [key for key, val in sheet_data[0].items()]

print(headers)