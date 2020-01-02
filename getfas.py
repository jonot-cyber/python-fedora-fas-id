from fedora.client.fas2 import AccountSystem

fas = AccountSystem(username="testuserforgooglecodein2", password="HC3y9YEIdUc0CmLI")

emails = fas.people_by_key(key="email",search=input("What username would you like to find the email for? "),fields=['id'])

print("The email for this account is {}".format(next(iter(emails))))
