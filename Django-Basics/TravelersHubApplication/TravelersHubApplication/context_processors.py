from TravelersHubApplication.utils import get_user_obj


def user_profile_context(request):
    return {
        'user_profile': get_user_obj()
    }
