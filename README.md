# Finding-pi-to-n-Decimal-Places
A Python implementation of the Chudnovsky algorithm to find pi to the nth decimal place with O(n(log(n)**3) time complexity

The initial idea that had crossed my mind when first faced with this problem was to simply take the constant `pi` from the `math` package and return the first `n` digits. However, since this value is understandably only accurate to the 15th decimal place (understandably so, since much more precision would be unnecessary for the  majority of calculations), this would not suffice and I would have to research methods to compute pi to the nth digit. The best solution I was able to find for this project was using the Chudnovsky algorithm (https://en.wikipedia.org/wiki/Chudnovsky_algorithm) for computing pi.

This code is valid for positive integer values of `n`
