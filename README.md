# cctransactionspammer
This script spams credit card transactions.

This script essentially does a credit card transaction request to cloudfare which costs a few cents per transaction.
So this will basically spam transactions and cost the spamming site money.

The commented out code is to make it threadable. I haven't been able to figure out how to bypass the transaction wait
time, so I've gone ahead and imported cloudscraper for now because I may be able to use that down the line
but haven't been able to solve that problem with this module.

The credit card info used is from ayden (https://docs.adyen.com/development-resources/test-cards/test-card-numbers)
Thank you!
