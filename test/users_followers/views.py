import json
import os
import random
from collections import defaultdict

from django.http import JsonResponse
from django.db.models import Count

JSON_FOLDER = os.path.join('static', 'data')

def _create_followers_dict():
    users_followers = defaultdict(list)

    json_files = [f for f in os.listdir(JSON_FOLDER) if f.endswith('.json')]
    for filename in json_files:
        file_path = os.path.join(JSON_FOLDER, filename)
        with open(file_path) as json_file:
            user_data = json.load(json_file)
            user_id = user_data["user_id"]
            following = user_data.get("users_following", [])

            for followed_user_id in following:
                users_followers[user_id]
                users_followers[followed_user_id].append(user_id)

    return users_followers

def get_all_users_followers(request):
    users_followers = _create_followers_dict().items()
    sorted_followers = {int(k): v for k, v in sorted(users_followers, key=lambda item: int(item[0]))}
    response_data = [{'user_id': user_id, 'followers': following} for user_id, following in sorted_followers.items()]

    return JsonResponse(response_data, safe=False)

def user_with_fewest_followers(request):
    users_followers = _create_followers_dict()
    min_followers_count = min(len(users_followers[user]) for user in users_followers)
    users_with_min_followers = [user for user in users_followers if len(users_followers[user]) == min_followers_count]

    user_with_least_followers = random.choice(users_with_min_followers)
    response_data = {'user_id': user_with_least_followers, 'amount_of_followers': min_followers_count}

    return JsonResponse(response_data, safe=False)