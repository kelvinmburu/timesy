import urllib.request,json

# Getting the quote base url
quote_url = 'https://zenquotes.io/api/random/quotes'

def get_quote():
  '''
  Function that gets a random quote - gets a jason response to our url request
  '''

  with urllib.request.urlopen(quote_url) as url:
    get_quote_data = url.read()
    quote = json.loads(get_quote_data)

  return quote