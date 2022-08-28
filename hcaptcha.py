import os
from twocaptcha import TwoCaptcha


def solvehCaptcha(sitekey, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', '**********APIKEY**********')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey=sitekey,
            url=url,
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result