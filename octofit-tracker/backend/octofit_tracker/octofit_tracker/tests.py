from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='desc')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='all')
        self.activity = Activity.objects.create(user=self.user, type='run', distance=5, duration=30)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')

    def test_activity_str(self):
        self.assertIn('Test User', str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn('Test Team', str(self.leaderboard))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')
