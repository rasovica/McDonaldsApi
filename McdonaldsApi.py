import json


class McDonald:
    def __init__(self):
        import requests
        # Defines data that is sent with the requests
        attr = json.loads('{\"AppVer\":\"1.0.5\",\"OSVer\":\"Android 6.0.1\",\"OSType\":1}')
        self.base_data = json.loads('{"ARB_INTERNET_ACCESS": "1", "cantCheckIn": "0", "appVersion": "1.0.5 (15)", "ARB_ORIENTATION": "portrait", "isLoggedIn": "0"}')
        self.base_data['attr'] = attr
        self.current_data = self.base_data
        # Creates a session
        self.session = requests.session()
        self.session.headers.update({'Client-ID': '077d6ddb4924e3f212415uuIxWfmEGSeS3FhlezRLaN.izTeM9s16', 'User-Agent': 'okhttp/  3.81'})

        # The app does this for some reason even thought we don't have a user #BADPROGRAMING
        self.session.post('https://www.mcdonalds.si/auth/LoginUser', json.dumps(self.current_data))
        self.session.post('https://www.mcdonalds.si/auth/GetUserData', json.dumps(self.current_data))

    # Returns json with all restaurants in Slovenia
    def get_restaurants(self):
        return json.dumps(self.session.get('https://www.mcdonalds.si/exports/restaurants.js').content.decode('utf-8'))

    # Returns all food and drink items you can buy
    def get_foods(self):
        return json.dumps(self.session.get('https://www.mcdonalds.si/exports/offers.js').content.decode('utf-8'))

    # Returns random data the app uses
    def get_content(self):
        return json.dumps(self.session.get('https://www.mcdonalds.si/exports/content.js').content.decode('utf-8'))

    # Registers a new user
    def register(self, first_name, last_name, email, password, agree_to_terms='1', agree_to_spam='0'):
        # No idea why they send data two different ways
        self.current_data['FName'] = first_name
        self.current_data['LName'] = last_name
        self.current_data['Email'] = email
        self.current_data['UPass'] = password
        self.current_data['AgreeYears'] = agree_to_terms
        self.current_data['AgreeData'] = agree_to_spam

        self.current_data['firstName'] = first_name
        self.current_data['lastName'] = last_name
        self.current_data['email'] = email
        self.current_data['password'] = password
        self.current_data['registrationCheck'] = agree_to_terms
        self.current_data['registrationCheckOptional'] = agree_to_spam

        self.current_data['policyLink'] = 'https:\/\/www.mcdonalds.si\/splosni-pogoji-mobilna-aplikacija\/'

        r = json.loads(self.session.post('https://www.mcdonalds.si/auth/RegisterNewUser', data=json.dumps(self.current_data)).content.decode('utf-8'))
        self.current_data = self.base_data
        return r

    # Login user
    def login(self, email, password):
        # Again most data is duplicated
        self.current_data['password'] = password
        self.current_data['username'] = email

        self.current_data['UName'] = email
        self.current_data['UPass'] = password

        data = json.loads(self.session.post('https://www.mcdonalds.si/auth/LoginUser', data=json.dumps(self.current_data)).content.decode('utf-8'))

        # Add token and id to session
        self.base_data['UserID'] = data['Data']['UserID']
        self.base_data['AccessToken'] = data['Data']['AccessToken']
        self.base_data['isLoggedIn'] = '1'
        self.current_data = self.base_data

        return data

    # Requires login, gets user info
    def get_user_info(self):
        return json.loads(self.session.post('https://www.mcdonalds.si/auth/GetUserInfo', data=json.dumps(self.current_data)).content.decode('utf-8'))

    # Requires login, gets users cupons
    def get_coupons(self):
        return json.loads(self.session.post('https://www.mcdonalds.si/auth/GetCoupons', data=json.dumps(self.current_data)).content.decode('utf-8'))

    # Requires login, tries to get joker coupon, I have not seen this succeed
    def play_joker(self):
        return json.loads(self.session.post('https://www.mcdonalds.si/auth/PlayJoker', data=json.dumps(self.current_data)).content.decode('utf-8'))

    # Requires login, takes the qr code from the bill and tries to check in with it, 4 check ins result in a reward
    def record_checkin(self, qr_code):
        self.current_data['ARBO_QR'] = {'value': qr_code, 'isRead': 1}
        self.current_data['QRCode'] = qr_code

        data = json.loads(self.session.post('https://www.mcdonalds.si/auth/RecordCheckIn', data=json.dumps(self.current_data)).content.decode('utf-8'))

        self.current_data = self.base_data

        return data
