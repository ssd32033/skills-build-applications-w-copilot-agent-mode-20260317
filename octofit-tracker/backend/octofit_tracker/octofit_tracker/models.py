from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    distance = models.FloatField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.CharField(max_length=50)

    def __str__(self):
        return self.name
