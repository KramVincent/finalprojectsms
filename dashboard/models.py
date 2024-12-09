from django.db import models
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if self.score <= 59:
            account_sid = 'ACd6012d98b54c7b44efee8434398de7a0'
            auth_token = 'c3717eec0a3a06b656bf8171ac531be7'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Hello {self.name}, you didn't secure a slot. Your score: {self.score}",
                from_='+17755998986',
                to='+639463105285',
            )
        elif 60 <= self.score < 90:
            account_sid = 'ACd6012d98b54c7b44efee8434398de7a0'
            auth_token = 'c3717eec0a3a06b656bf8171ac531be7'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Hello {self.name}, Congratulations! You secured a slot with a score of {self.score}",
                from_='+17755998986',
                to='+639463105285',
            )
        else:
            account_sid = 'ACd6012d98b54c7b44efee8434398de7a0'
            auth_token = 'c3717eec0a3a06b656bf8171ac531be7'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name}, you secured a slot and received money! Your score: {self.score}",
                from_='+17755998986',
                to='+639463105285',
            )
         

        print(message.body)

        return super().save(*args, **kwargs)
