# MLCCI

## Machine Learning Crypto Currency Investor 

---
---

### Abstract

Taking info from Multiple sources we can apply Natural language processing 
techniques to score the data and reactions to each source. 

---

### Sources 

Data can and will be streamed from various sources to be included into the 
Natural languae model. Each one of the following sources has a different audience 
and a different draw. In the future it might stretch to inclclude other sources 
including other financial markets and news / economics outlets. Parsing is the time
intensive part. 

1. [Twitter](https://ww.twitter.com)
    * [Tweepy - Twitter API](https://github.com/tweepy/tweepy)
2. [Reddit]( https://www.reddit.com) 
    * [Streaming API - python pusher](https://github.com/pusher/pusher-http-python)
        - [Require registration of App]( https://app.pusher.com/)
	* [Json Page Info](https://www.reddit.com/r/bitcoin/new.json?sort=new)
		-  Json format for getting sub info and posts
4. [Google News](https://newsapi.org/google-news-api)
3. Others?

---

### Models

The models used for Natural Language processing fall into two categories: 
Symbolic used tokenized words to infer meaning, and Sub-Symbolic translates words 
(and after training) sentences into a vector that models real world intention. 
See [this article explaining the difference](https://medium.com/intuitionmachine/the-two-paths-from-natural-language-processing-to-artificial-intelligence-d5384ddbfc18 ).


1. Sub-Symbolic
	* [Gensim - Word to Vector](https://rare-technologies.com/word2vec-tutorial/)
2. Symbolic	
	* [NLTK - Natural Language Tool Kit](http://www.nltk.org/)
	* [IBM Watson - SA Plugin](https://www.twilio.com/blog/2016/07/sms-sentiment-analysis-in-python-with-flask-and-the-ibm-watson-twilio-add-on.html)

---

### Method

There are two methods by which I would like to train and test this project. 
First, Collecting data from the sources continuously and processing the 
text data to determine sentiment. Upon determining sentiment check the 
model for analysis scoring against the market performance. 

* Check day's sentiment again day performance 
* Check day's sentiment against hour performance
* Check hour sentiment against hour performance
* (Longterm) Check Week sentiment against week performance 

---

### Links 

* [Coinbase](https://www.coinbase.com)
	- [API](https://developers.coinbase.com/docs/wallet/guides/buy-sell)
	- [GDAX API](https://docs.gdax.com/?python#introduction)
	- [GDAX Exchange](https://www.gdax.com/trade/BTC-USD)
	- [Account](https://www.coinbase.com/signin)
* [Ethereum](https://www.ethereum.org/)
* [R/CryptoMarkets](https://www.reddit.com/r/CryptoMarkets/)
* [R/CryptoCurrencyLive](https://www.reddit.com/r/CryptoCurrencyLive/)
* [Books on BlockChain ](http://cryptoczars.com/top-5-books-blockchain-developers/)


---

### Running

Currently there are only test scripts implemented. 
To run the twitter stream getting the tweets pertaining to "bitcoin", "ethereum", and "btc-usd"

```
$ python twitter/test.py

```
