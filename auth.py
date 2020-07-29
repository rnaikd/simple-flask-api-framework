# Google firebase-admin login to pull data from server and perform operations

import google
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession


class Authme:

    def get(self, param):
        if len(param) < 1:
            return {
                'code': 400,
                'message': 'Wrong number of params'
            }

        # Define the required scopes
        scopes = [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/firebase.database"
        ]

        # Authenticate a credential with the service account
        credentials = service_account.Credentials.from_service_account_file(
            "key/service_key.json", scopes=scopes)

        # Use the credentials object to authenticate a Requests session.
        authed_session = AuthorizedSession(credentials)
        response = authed_session.get(
           "https://<DATABASE_NAME>.firebaseio.com/users/ada/name.json")

        # Or, use the token directly, as described in the "Authenticate with an
        # access token" section below. (not recommended)
        request = google.auth.transport.requests.Request()
        credentials.refresh(request)
        if param[0] == 'token':
             data = credentials.token
        else:
             data = response
        
        return {
            'code': 200,
            'data': data
        }

    def post(self, param):
        pass

    def put(self, param):
        pass

    def delete(self, param):
        pass