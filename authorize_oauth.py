import urlparse
import oauth2 as oauth
import requests

# First of all fill in your consumer key and secret you get when
# you create your application at Redu

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'

request_token_url = 'http://localhost:3000/oauth/request_token'
access_token_url = 'http://localhost:3000/oauth/access_token'
authorize_url = 'http://localhost:3000/oauth/authorize'

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# Step 1: Get a request token. This is a temporary token that is used for 
# having the user authorize an access token and to sign the request to obtain 
# said access token.

resp, content = client.request(request_token_url, "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))

print "Request Token:"
print "oauth_token        = %s" % request_token['oauth_token']
print "oauth_token_secret = %s" % request_token['oauth_token_secret']
print 

# Step 2: Redirect to Redu. Since this is a CLI script we do not redirect.
# In a web application you would redirect the user to the URL below.
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print 

# After the user has granted access to you, the consumer, the Redu server
# will show him an alphanumeric code to enter in our application
accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

# You use this token to make a new request and ask for the access token. You
# should store this access token somewhere safe, like a database, for future use.
token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")

access_token = dict(urlparse.parse_qsl(content))

print "Access Token:"
print "oauth_token        = %s" % access_token['oauth_token']
print "oauth_token_secret = %s" % access_token['oauth_token_secret']

# You may now access protected resources using the access tokens above.