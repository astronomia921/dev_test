import json
import requests
import base64


def get_block_transactions(block_number):
    base_url = "https://akash.mintscan.io/api"
    endpoint = f"/blocks/{block_number}"
    url = base_url + endpoint
    response = requests.get(url, verify=False, timeout=60)

    if response.status_code == 200:
        block_data = response.json()
        encoded_data = block_data.get('data', {}).get('txs', '')

        if encoded_data:
            decoded_data = base64.b64decode(encoded_data).decode('utf-8')
            transactions = json.loads(decoded_data)

            with open('transactions.txt', 'w') as file:
                file.write(json.dumps(transactions))

            return transactions

    return None


print(get_block_transactions(11260637))
