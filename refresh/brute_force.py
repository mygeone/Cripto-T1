import requests

URL = 'https://www.refreshstore.cl/auth/api/validate'
PARAMS = {
    '_token': 'qqJP2a2QIvbK6rzCUXzwjaHmDDnoCH60QTM27Ud8',
    'email': 'miguel.contreras1@mail.udp.cl',
    'password': 'abc123',
    'g-recaptcha-response': '03AGdBq26R_oX8_xw9LLfHjbPdntX0wJ-fyWuiiH30Liw-QUbTSEihxepu7aG5300sflLycSW6up_Li2vXP6iCZ0_rvUim-c730k_TZxT3Uf52rnEGbz8XYGig4dcQFbQMulJc0ph2t3auhE8bNy7TjliYoxmIKGWMKPDudIbKxiZT87dVoMfm7kGyy_xkUadbUVZd0FQqtbHpht5IKK2Z6r3tmfuKQoigxQb-OLYXtUXI_-l5BSeSLOuHKNilJetox-TeMOMkB4-h8kvp1E0ul8cxuBPkOfI7FdwUos6-G4cNdS7rdw3bpMa7nb3oCa2qZf9GDOX11XfrQvL6RzTaJwXMPXs_gxXGZ1Ris5xcwyJzGO2CMrM-JEG3cUCaUfGecSTfNxJh1N_BWV3OOUlN-41ZO3-,mEo2D4kAnxjtBnpJAfXr6gxSCQDwGygFpAN1M9BXeOCdj7D2q',
    'token': '03AGdBq24TOileUuE2lxobRFR0oEJZtnKrb_fVfdU7UKHbK2u4bMwga0plnXE6E5Dua6x-fSabo8Y6S1-J-Ywq8udQSbMXkT3tQ92Fr_CKPY6gwsxZj-APPzuaQ0mfhrxLt3r56Ho9GQ-xXb7G2vXGgK88yh7utdC-mGjsmt9vuf0BqbRwcRjtXWgnvVdR3TL8jdZvV_0gHR8BkinpIbzJ6Nll7FbkqqOQffrukgi3mP1ATusOI3p2BTJ7_Oo9ffaUVpiLMAWnvLn0KFHKQOGi1d9TAUVOFt4l35lQp3Y8jfFVw48Yer7trzoDnlhISCeB83hCPI7CeTDDptZbV7i3XHjvwWBxJz73Rq42rrmunlsUCWCu5peY2YE1yGQyXn6mZtOBriVudDpueWuf3vf6BivYwD_4YisDn1yKLiD9cFuF_wZa3gJQ63bbQr45_q2TIbAYpl7If1ma',
    'action': 'login'
    }

r = requests.post(url = URL, params = PARAMS)


print(r)