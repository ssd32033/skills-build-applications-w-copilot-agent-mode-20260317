from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Collections
        users = db['users']
        teams = db['teams']
        activities = db['activities']
        leaderboard = db['leaderboard']
        workouts = db['workouts']

        # Clear existing data
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Sample teams
        marvel_team = {'name': 'Marvel', 'description': 'Marvel Superheroes'}
        dc_team = {'name': 'DC', 'description': 'DC Superheroes'}
        marvel_team_id = teams.insert_one(marvel_team).inserted_id
        dc_team_id = teams.insert_one(dc_team).inserted_id

        # Sample users
        user_data = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_team_id},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': marvel_team_id},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team_id': marvel_team_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_team_id},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team_id': dc_team_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_team_id},
        ]
        user_ids = users.insert_many(user_data).inserted_ids

        # Sample activities
        activity_data = [
            {'user_id': user_ids[0], 'type': 'run', 'distance': 5, 'duration': 30},
            {'user_id': user_ids[1], 'type': 'cycle', 'distance': 20, 'duration': 60},
            {'user_id': user_ids[2], 'type': 'swim', 'distance': 1, 'duration': 40},
            {'user_id': user_ids[3], 'type': 'run', 'distance': 10, 'duration': 50},
            {'user_id': user_ids[4], 'type': 'cycle', 'distance': 15, 'duration': 45},
            {'user_id': user_ids[5], 'type': 'swim', 'distance': 2, 'duration': 55},
        ]
        activities.insert_many(activity_data)

        # Sample leaderboard
        leaderboard_data = [
            {'team_id': marvel_team_id, 'points': 300},
            {'team_id': dc_team_id, 'points': 280},
        ]
        leaderboard.insert_many(leaderboard_data)

        # Sample workouts
        workouts_data = [
            {'name': 'Morning Run', 'description': '5km easy run', 'suggested_for': 'all'},
            {'name': 'HIIT', 'description': 'High intensity interval training', 'suggested_for': 'advanced'},
        ]
        workouts.insert_many(workouts_data)

        self.stdout.write(self.style.SUCCESS('테스트 데이터가 octofit_db에 성공적으로 적재되었습니다.'))
