import logging
import sys
import os
import time
import everysk

everysk.api_sid = '<YOUR_ACCOUNT_SID>'
everysk.api_token = '<YOUR_AUTH_TOKEN>'
everysk.verify_ssl_certs = False # Set to True to verify if the server certificate is valid


def test_risk_attribution():
    args = {
        'projection': ['IND:SPX', 'IND:SX5E'],
        'base_currency': 'USD',
        'date': '20181112',
        'securities': [
            {'id': 'id0', 'symbol': 'AAPL', 'quantity': 1.0}
        ]
    }
    r = everysk.Calculation.riskAttribution(**args)

    print(everysk.utils.dumps_json(r))

    return

def test_stress_test():
    args = {
        'shock': 'IND:SPX',
        'magnitude': 0.1,
        'horizon': None,
        'projection': ['IND:SPX', 'IND:SX5E'],
        'base_currency': 'USD',
        'date': '20181112',
        'securities': [
            {'id': 'id0', 'symbol': 'AAPL', 'quantity': 1.0}
        ]
    }
    r = everysk.Calculation.stressTest(**args)

    print(everysk.utils.dumps_json(r))

    return    


def main():

    # test_risk_attribution()
    test_stress_test()

    return

if __name__ == '__main__':
    main()
