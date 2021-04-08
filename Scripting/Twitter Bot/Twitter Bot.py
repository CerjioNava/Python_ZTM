#Twitter Bot

#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. 
#Run this on your own machine, not in this Repl. 
import tweepy
import time						#Para el time.sleep()

#REVISAR DOCUMENTACIÓN DE TWEEPY

consumer_key = ''				#API KEY
consumer_secret = ''			#API SECRET KEY 	
access_token = ''				#ACCESS TOKEN
access_token_secret = ''		#ACCESS TOKEN SECRET

#Todas desde el usuario API que creemos

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)		#Verificadores de twitter de la cuenta
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)			#Autenticador

'''
#Ejemplo imprimiendo los tweets que aparezcan en el inicio de nuestro twitter.

public_tweets = api.home_timeline()
fow tweet in public_tweets:
	print(tweet.text)
'''

user = api.me()						#Devuelve información de nuestro usuario
print (user.name) 					#Imprime nombre de usuario
print (user.screen_name)			#Imprime el identificador de usuario
print (user.followers_count)		#Imprime la cantidad de seguidores

search = "zerotomastery"
numberOfTweets = 2

#limit_handle para limitar la cantidad de veces que se contacta el API (para evitar colapsos)
def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:		#Si se supera el RateLimit, se detiene la función por 1 segundo.
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):		#Cursor es un generador
  if follower.name == 'Usernamehere':									#Si se consigue al usuario 						
    print(follower.name)					#Se imprime el nombre 
    follower.follow()						#Follow al usuario


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()				#También puedes retweetear cosas con .retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
