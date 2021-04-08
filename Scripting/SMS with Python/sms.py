#VER TWILIO, nos otorga el código incluso...

#Código del curso: (Igualmente extraído de Twilio)

from twilio.rest import Client

account_sid = 'AQUI VA EL CÓDIGO IDENTIFICADOR QUE NOS OTORGA'
auth_token = 'Otro código más del dashboard'
client = Client(account_sid, auth_token)

message = client.messages.create(
						from_ = 'Nro virtual de la página',
						body = 'Cuerpo del mensaje',
						to = 'Nro destinatario'
						)

print(message.sid) 

#TODO este código es otorgado por la misma página, esto fue un ejemplo de como 
#trabajar con cosas nuevas. Siempre googlear!