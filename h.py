#Coded by Traodoisub.com
import os
import datetime
from datetime import datetime
import requests,json
import uuid
from time import sleep

today = datetime.today()
ngay = today.day
thang = today.day
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
	import requests
except:
	os.system("pip3 install requests")
	import requests

try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip3 install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box

headers = {
	'authority': 'traodoisub.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
	'user-agent': 'traodoisub tiktok tool',
}
class ApiPro5:
	
    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
    def join(self, group_id):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }

        response = {
        "require": [
            [
                "ScheduledServerJS",
                "handle",
                None,
                [
                    {
                        "__bbox": {
                            "require": [
                                [
                                    "RelayPrefetchedStreamCache",
                                    "next",
                                    [],
                                    [
                                        "adp_CometSettingsDropdownListQueryRelayPreloader_67ee393b843272054669835",
                                        {
                                            "__bbox": {
                                                "complete": True,
                                                "result": {
                                                    "data": {
                                                        "viewer": {
                                                            "actor": {
                                                                "__typename": "User",
                                                                "profileSwitcherEligibleProfiles": {"count": 19},
                                                                "id": "61559472533015",
                                                                "name": "Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức",
                                                                "settings_dropdown_profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s60x60_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYG2uYN62pnKQ4kj4Q2gUY1d-oD6puoB0i7aAinviXkboQ&oe=67F3F481"
                                                                },
                                                                "first_profiles": {
                                                                    "nodes": [
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573311838392",
                                                                                "name": "Dương Quỳnh Anh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C"
                                                                                }
                                                                            }
                                                                        },
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573471253195",
                                                                                "name": "Đặng Công Danh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767"
                                                                                }
                                                                            }
                                                                        }
                                                                    ]
                                                                },
                                                                "should_show_account_level_settings": True,
                                                                "username": "ng.minh.duck210",
                                                                "first_profile": {
                                                                    "count": 19,
                                                                    "nodes": [{"profile": {"id": "61573311838392"}}]
                                                                },
                                                                "page_publishing_authorization_hub_action_url": "/id/?referrer=profile_plus_switcher&product=4",
                                                                "page_publishing_authorization_admin_notice": None,
                                                                "profiles": {
                                                                    "edges": [
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573311838392",
                                                                                    "name": "Dương Quỳnh Anh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "597353450119629"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRK_I_H1EE1sKXmIwcnrsWtSnMwIc4xa33WOI6l7SdlGTQVKqE7rynm4mwVC40wm5-sPGOL7O4TM9QX0N26mAlpA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573471253195",
                                                                                    "name": "Đặng Công Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "609933448859519"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR25TAIHQspV7vNdWrMPF28kYU-mC-XLD-TQVe44hZ48hWm4khvUBYmkthOsfaUO0Pb0R_FcLsqy-0qGCcd9aT3w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573277518825",
                                                                                    "name": "Đặng Công Hào",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480325538_122163563582315751_6859066577211977932_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=111fe6&_nc_ohc=DN5jjO443DEQ7kNvgF5S19j&_nc_oc=AdmNaslAvS7tc1RPgE04qNPAWHIGpAyPdVt8-sTc090Ouet9gyd83RF0wavc3NXCEIDKjYxrxmUF4QLTN2OnsUGq&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYGRXR18kvmFJPzj1SGg9GmNwlD-xkUT1_ha5-ZM2PTRHg&oe=67F40BE9",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRNuPvMJWqVwGZvBAvcAPc8T7gx1mRAftirEqxHSOMT_VlQqqpC8fgZ9Z9gzFFTkeleX9pkrgQwC02XyFTmFM65A"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573005310570",
                                                                                    "name": "Đinh Đức Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480240676_122102774600766843_3156531964467906790_n.jpg?stp=c0.65.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=103&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=jbb3Q-KMvQwQ7kNvgH5Sbyo&_nc_oc=AdmF95RXt4ptdi2yG6yzV6tZYRQKRlqp5bl1Y22O1A1YLUM7EH6EM5CpmJW5Q5hdL_pOnuW_KsMfI33afXvK5zRz&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEap0dzqFz1QJtFqnUm1gAAP72cku_rjtjfP5gLj0iajA&oe=67F425C6",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 3,
                                                                                    "delegate_page_id": "517677294771234"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRTgvMDjZgq1xUTacT5uW5NkAHOMlbuv8eqmiCou0KJr44YnhCgMbw2bPuRGJDUOpY05Wa-xNR9wRtpAQd1iIQYw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573106105525",
                                                                                    "name": "Đinh Vĩnh Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/480506539_122100039416770203_4952372284759289001_n.jpg?stp=c0.263.675.675a_cp0_dst-jpg_s40x40_tt6&_nc_cat=105&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=lGy_-cQ8gZQQ7kNvgHYg1gm&_nc_oc=AdmufYTW-lgT432Gvk521V3lM_o0HbeiOFknY2xEfoXJ0bsb5xtF4o4E9HLl8_tInB9thTIUwTutNyKapnxYotC9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYErruwK0gV6VVQ0JIaysfuDP90p9zi-y0JLYiAnBniUSA&oe=67F41747",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "620655147788759"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR9d_kNnKvbYCL3OlXqLrVD2Tk2wZ52mV60KoWlxgcbE4FaX52vZjMxrae2ikoYCA7AvULCuN2iQOQAAU5pmfyQg"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573093445871",
                                                                                    "name": "Bùi Công Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480502745_122099701784769781_5642310825084805014_n.jpg?stp=c0.0.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=t9MWVtlBuI0Q7kNvgFVA8jA&_nc_oc=AdnJTiaykIXnTl25_VfEuk2C3sY51cYZmnE15oxCLvhQIYtZT0jHvsbHMHtCy9WkPe1HrqUvyAdUb-mRwsXXROEQ&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYHFoKc7r_31WhFzYXNJyF7kXZpAUCYDObeIjs1PurBAKg&oe=67F416A7",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "554142717786080"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRKQfQOvOnYbNf90JLm2U8iiBKUWKWNUcPf9Pje0Va5FJUkFLLFesAQbGWcq9sXVBSADq4Z-OrK9v2Gr0rm-E5Dw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61567577686564",
                                                                                    "name": "Hoàng Sinh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/479939442_122131664672585922_990255040247358089_n.png?stp=cp0_dst-png_p40x40&_nc_cat=110&ccb=1-7&_nc_sid=111fe6&_nc_ohc=0XYiKz8UApQQ7kNvgF4D301&_nc_oc=Adk-Gg9M4eW00HsbLrt_4fbVigvG5UWTNUlhhEC7WX7oH7MKhYjM2HJfqPswUDSlwKk1g26S6TwHBNO-fYz2ikLe&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEkFcJNaQk0wDOCGLETwtus6rEa2tZVM1WMDr6WLftojw&oe=67F40D8A",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 6,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRD79dU7c7rP2bE9WhfAs4h5OahvtzgJ2Oh456mpIWmed1KE_2LckomSP2_AY9kMH9Ws7sY5qYtgZSpovpPPFutA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573015719772",
                                                                                    "name": "Dương Duy Năm",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-3.fna.fbcdn.net/v/t39.30808-1/480045626_122102346224767190_6139893211204722726_n.jpg?stp=c0.23.203.203a_cp0_dst-jpg_s40x40_tt6&_nc_cat=108&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=c3KzHh0M4o4Q7kNvgGsml8h&_nc_oc=AdmUcClGhaAuLOuwEAiMS7nmneQ7mC_CI8W_o7hNy_RasOGnal1QQqhy4_DwLe0M-A9zzoesrJSqC4YCOkv9BEBY&_nc_zt=24&_nc_ht=scontent.fhan2-3.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEz1Gol3kUn9bC4IGuZipocFRaiFaHvmg7JxbCJlftENA&oe=67F423E4",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "551153321418862"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRjMCl0hjOxdkGa9P7V7uvKECrwxO6kfSZB_uNlQbkV-0kBnI6ysIcYRpnfLTKGM4K-k386HvJzN_PTHRatuCB2w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61568771054821",
                                                                                    "name": "Minh Đức",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/468154565_122104593254625701_4021722386690848790_n.jpg?stp=c58.0.176.176a_cp0_dst-jpg_s40x40_tt6&_nc_cat=104&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=J6_pdpDBmukQ7kNvgH3KB_s&_nc_oc=Adlvef9fkVVHHpP3CDLz_BiYBqagCq_n1uV2DPpFtyNgPYQesAcPva7hJfYx2EapDsORrp-FQqEjDYOpOkvc3HC8&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEPO0OoIyNcTk3QNOaRqybxbAm_o9RXeOhPu-J4ZRmSvQ&oe=67F4180F",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 14,
                                                                                    "delegate_page_id": "522263997626964"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRaZtlzBc7eiNK3DqrzanOrkbcjy9fCOyqyJ0M0IF_hb5ew2ayxxvlzQEkOyuVFfTVu_8OVeemo6CgbEZR_S39YA"
                                                                        }
                                                                    ],
                                                                    "page_info": {
                                                                        "end_cursor": "AQHRXqKCFTfhiUH893wt15IQmvOMckBufl6UkQwKyJpA2WRJVQAaeCUMbXf4oPwOUpGTJdnBqqe6KLqUxFc1YdvdGQ",
                                                                        "has_next_page": True
                                                                    }
                                                                },
                                                                "is_failing_page_publishing_authorization": False,
                                                                "profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYESk-zl4tr9LVQed55X4Ho5fNGVA3jhhbR_UcKegQQfbA&oe=67F3F481",
                                                                    "width": 40,
                                                                    "height": 40,
                                                                    "scale": 1
                                                                },
                                                                "unseen_update_count": 0,
                                                                "is_additional_profile_plus": False,
                                                                "profile_count": {"count": 19},
                                                                "profile_switcher_unread_notifications": 68
                                                            },
                                                            "settings_menu_business_suite": {
                                                                "should_show_entrypoint": False,
                                                                "bizweb_home_link": "https://business.facebook.com/latest/home?nav_ref=fb_web_pplus_settings_menu"
                                                            },
                                                            "additional_profile_creation_eligibility": {
                                                                "should_show_soap_creation_settings_dropdown_entrypoint": False,
                                                                "single_owner": {
                                                                    "can_create": False,
                                                                    "explanation": "Bạn chỉ có thể có 2 trang cá nhân bổ sung cùng lúc. Bạn có thể vào phần cài đặt trang cá nhân để xóa trang cá nhân bổ sung."
                                                                }
                                                            },
                                                            "is_eligible_for_account_level_settings": True,
                                                            "can_access_privacy_checkup": True,
                                                            "privacy_center": {"should_show_privacy_center": True},
                                                            "device_switchable_accounts": [
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "short_name": "Thương Lan",
                                                                        "name": "Thương Lan Ngô",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_a_g"},
                                                                            {"name": "next", "value": "/?next_cuid=AYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid0SnxDyAeig17C1AU6cFeahtBYrnZqfLrHdr12u2uSDz6u8GLYkaywk1KEJR715EeXl",
                                                                        "short_name": "David",
                                                                        "name": "David Edward Smith",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_2w0"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid02wn8bxaW4ip3uyHZuUi1KGeJ76UK7JHLnzKj5hvNvKHxQdpwbP5YYgCzwH6WEjPHBl",
                                                                        "short_name": "Robert",
                                                                        "name": "Robert David Williams",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_Cso"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE"}
                                                                        ]
                                                                    }
                                                                }
                                                            ],
                                                            "first_account": [
                                                                {
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "profile_picture": {
                                                                            "scale": 1,
                                                                            "height": 40,
                                                                            "width": 40,
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A"
                                                                        }
                                                                    }
                                                                }
                                                            ],
                                                            "logout_hash": "AfdHNYKHLQEwmbe_uqY"
                                                        },
                                                        "intl_locale_selector_query": {
                                                            "current_locale": {"localized_name": "Tiếng Việt"}
                                                        },
                                                        "logout_whitelist": [
                                                            "^CacheStorageVersion$",
                                                            "^RTC_VIDEO_INPUT$",
                                                            "^RTC_AUDIO_INPUT$",
                                                            "^RTC_AUDIO_OUTPUT$",
                                                            "^RTC_IS_AUDIO_ONLY$",
                                                            "^RTC_NOISE_SUPPRESSION$",
                                                            "^RTC_LOBBY_MUTE_STATE$",
                                                            "^Session$",
                                                            "^_oz_",
                                                            "^_video_bandwidthEstimate$",
                                                            "^Banzai$",
                                                            "^bz",
                                                            "^banzai\\:last_storage_flush$",
                                                            "^falco_queue_",
                                                            "^mutex",
                                                            "^msys",
                                                            "^Bandicoot\\:",
                                                            "^imp_seq_num$",
                                                            "^qe_switcher_nub_selection$",
                                                            "^TabId$",
                                                            "^sp_pi$",
                                                            "^\\:userchooser\\:osessusers$",
                                                            "^\\:userchooser\\:settings$",
                                                            "^brands\\:console\\:config$",
                                                            "^consoleEnabled$",
                                                            "^__fb_messenger_desktop_presence_info$",
                                                            "^vc_",
                                                            "^_showMDevConsole$",
                                                            "^ga_client_id$",
                                                            "^ga4_client_id$",
                                                            "^_mswam_$",
                                                            "^am_recently_used_filters\\:",
                                                            "^am_image_size_cache$",
                                                            "^ickt$",
                                                            "^hb_timestamp$",
                                                            "^signal_flush_timestamp$",
                                                            "^__MWCMAutoJoinNotifNuxBanner\\.showBanner__$",
                                                            "^last_fast_refresh$",
                                                            "^_ctv_access_token$",
                                                            "^_ctv_android_device_info$",
                                                            "^_ctv_cast_access_token$",
                                                            "^_ctv_casting_remote$",
                                                            "^_ctv_console_log_viewer_on_full_screen_player_enabled$",
                                                            "^_ctv_cookie_consent_displayed$",
                                                            "^_ctv_debug_redux_logger_enabled$",
                                                            "^_ctv_deviceUniqueIDFallback$",
                                                            "^_ctv_gaming_consent_displayed$",
                                                            "^_ctv_installed_app_player_debug_overlay_enabled$",
                                                            "^_ctv_last_load_time_ms$",
                                                            "^_ctv_locale$",
                                                            "^_ctv_logged_out_constraints_sessions_count$",
                                                            "^_ctv_reloadedDueToStaleApp$",
                                                            "^_ctv_reloadedDueToUnrecoverableError$",
                                                            "^_ctv_search_terms$",
                                                            "^_ctv_tv_experiments$",
                                                            "^_ctv_usedCloseAppFallback$",
                                                            "^_ctv_user_sessions$",
                                                            "^_ctv_video_debug_overlay_enabled$",
                                                            "^_ctv_debug_rampart_server_number$",
                                                            "^fx_did$",
                                                            "^wa_lang_banner_dismissed$",
                                                            "^bulletin_article_reader_onload_dialog_seen$",
                                                            "^bulletin_session_attributes$",
                                                            "^md_survey$",
                                                            "^support_guest_chat$",
                                                            "^comet_is_recent_profile_switch$",
                                                            "^comet_console_position$",
                                                            "^mw_exchange_vm$",
                                                            "^has_seen_email_login_toast$",
                                                            "^cs_chat_support_user$",
                                                            "^NFT_DEVICE_KEY_PRIVATE_V1$",
                                                            "^NFT_DEVICE_KEY_PUBLIC_V1$",
                                                            "^show_wa_auth_button$",
                                                            "^BusinessInbox\\:sortMethod$",
                                                            "^LeadsCenter\\:ViewType$",
                                                            "^BizWebInsightsLeadsCenterHeaderGuidanceCard\\:LastClosedTime$",
                                                            "^Routing\\:url\\:AdsTALRouting$",
                                                            "^BizWebDirectResponseAdsBannerView$",
                                                            "^firefly_auth_tokens$",
                                                            "^BizWebStoryInsightsOptInBannerView$",
                                                            "^fair_ai_demos_rid$",
                                                            "^videoseal_tos_accepted$",
                                                            "^videoseal_user_rid$",
                                                            "^seen_password_entry_auto_prompt$",
                                                            "^trusted_devices_storage_version$"
                                                        ],
                                                        "fxcal_settings": {"ac_phase": "CENTRALIZED_SETTINGS_NO_SENSITIVE"}
                                                    },
                                                    "extensions": {"is_final": True}
                                                },
                                                "sequence_number": 0
                                            }
                                        }
                                    ]
                                ]
                            ]
                        }
                    },
                    {"__bbox": None},
                    {"__bbox": None}
                ]
            ]
        ]
    }

        return response 
    def subscribe(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return subscribe
    def reaction(self, id_post, reaction):
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'url': url}
        except:
            return {'status': False, 'url': url}
    
def get_page(cookie):
    # JSON tĩnh được tích hợp trực tiếp vào mã
    response = {
        "require": [
            [
                "ScheduledServerJS",
                "handle",
                None,
                [
                    {
                        "__bbox": {
                            "require": [
                                [
                                    "RelayPrefetchedStreamCache",
                                    "next",
                                    [],
                                    [
                                        "adp_CometSettingsDropdownListQueryRelayPreloader_67ee393b843272054669835",
                                        {
                                            "__bbox": {
                                                "complete": True,
                                                "result": {
                                                    "data": {
                                                        "viewer": {
                                                            "actor": {
                                                                "__typename": "User",
                                                                "profileSwitcherEligibleProfiles": {"count": 19},
                                                                "id": "61559472533015",
                                                                "name": "Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức",
                                                                "settings_dropdown_profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s60x60_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYG2uYN62pnKQ4kj4Q2gUY1d-oD6puoB0i7aAinviXkboQ&oe=67F3F481"
                                                                },
                                                                "first_profiles": {
                                                                    "nodes": [
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573311838392",
                                                                                "name": "Dương Quỳnh Anh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C"
                                                                                }
                                                                            }
                                                                        },
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573471253195",
                                                                                "name": "Đặng Công Danh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767"
                                                                                }
                                                                            }
                                                                        }
                                                                    ]
                                                                },
                                                                "should_show_account_level_settings": True,
                                                                "username": "ng.minh.duck210",
                                                                "first_profile": {
                                                                    "count": 19,
                                                                    "nodes": [{"profile": {"id": "61573311838392"}}]
                                                                },
                                                                "page_publishing_authorization_hub_action_url": "/id/?referrer=profile_plus_switcher&product=4",
                                                                "page_publishing_authorization_admin_notice": None,
                                                                "profiles": {
                                                                    "edges": [
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573311838392",
                                                                                    "name": "Dương Quỳnh Anh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "597353450119629"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRK_I_H1EE1sKXmIwcnrsWtSnMwIc4xa33WOI6l7SdlGTQVKqE7rynm4mwVC40wm5-sPGOL7O4TM9QX0N26mAlpA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573471253195",
                                                                                    "name": "Đặng Công Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "609933448859519"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR25TAIHQspV7vNdWrMPF28kYU-mC-XLD-TQVe44hZ48hWm4khvUBYmkthOsfaUO0Pb0R_FcLsqy-0qGCcd9aT3w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573277518825",
                                                                                    "name": "Đặng Công Hào",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480325538_122163563582315751_6859066577211977932_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=111fe6&_nc_ohc=DN5jjO443DEQ7kNvgF5S19j&_nc_oc=AdmNaslAvS7tc1RPgE04qNPAWHIGpAyPdVt8-sTc090Ouet9gyd83RF0wavc3NXCEIDKjYxrxmUF4QLTN2OnsUGq&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYGRXR18kvmFJPzj1SGg9GmNwlD-xkUT1_ha5-ZM2PTRHg&oe=67F40BE9",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRNuPvMJWqVwGZvBAvcAPc8T7gx1mRAftirEqxHSOMT_VlQqqpC8fgZ9Z9gzFFTkeleX9pkrgQwC02XyFTmFM65A"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573005310570",
                                                                                    "name": "Đinh Đức Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480240676_122102774600766843_3156531964467906790_n.jpg?stp=c0.65.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=103&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=jbb3Q-KMvQwQ7kNvgH5Sbyo&_nc_oc=AdmF95RXt4ptdi2yG6yzV6tZYRQKRlqp5bl1Y22O1A1YLUM7EH6EM5CpmJW5Q5hdL_pOnuW_KsMfI33afXvK5zRz&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEap0dzqFz1QJtFqnUm1gAAP72cku_rjtjfP5gLj0iajA&oe=67F425C6",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 3,
                                                                                    "delegate_page_id": "517677294771234"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRTgvMDjZgq1xUTacT5uW5NkAHOMlbuv8eqmiCou0KJr44YnhCgMbw2bPuRGJDUOpY05Wa-xNR9wRtpAQd1iIQYw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573106105525",
                                                                                    "name": "Đinh Vĩnh Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/480506539_122100039416770203_4952372284759289001_n.jpg?stp=c0.263.675.675a_cp0_dst-jpg_s40x40_tt6&_nc_cat=105&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=lGy_-cQ8gZQQ7kNvgHYg1gm&_nc_oc=AdmufYTW-lgT432Gvk521V3lM_o0HbeiOFknY2xEfoXJ0bsb5xtF4o4E9HLl8_tInB9thTIUwTutNyKapnxYotC9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYErruwK0gV6VVQ0JIaysfuDP90p9zi-y0JLYiAnBniUSA&oe=67F41747",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "620655147788759"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR9d_kNnKvbYCL3OlXqLrVD2Tk2wZ52mV60KoWlxgcbE4FaX52vZjMxrae2ikoYCA7AvULCuN2iQOQAAU5pmfyQg"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573093445871",
                                                                                    "name": "Bùi Công Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480502745_122099701784769781_5642310825084805014_n.jpg?stp=c0.0.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=t9MWVtlBuI0Q7kNvgFVA8jA&_nc_oc=AdnJTiaykIXnTl25_VfEuk2C3sY51cYZmnE15oxCLvhQIYtZT0jHvsbHMHtCy9WkPe1HrqUvyAdUb-mRwsXXROEQ&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYHFoKc7r_31WhFzYXNJyF7kXZpAUCYDObeIjs1PurBAKg&oe=67F416A7",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "554142717786080"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRKQfQOvOnYbNf90JLm2U8iiBKUWKWNUcPf9Pje0Va5FJUkFLLFesAQbGWcq9sXVBSADq4Z-OrK9v2Gr0rm-E5Dw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61567577686564",
                                                                                    "name": "Hoàng Sinh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/479939442_122131664672585922_990255040247358089_n.png?stp=cp0_dst-png_p40x40&_nc_cat=110&ccb=1-7&_nc_sid=111fe6&_nc_ohc=0XYiKz8UApQQ7kNvgF4D301&_nc_oc=Adk-Gg9M4eW00HsbLrt_4fbVigvG5UWTNUlhhEC7WX7oH7MKhYjM2HJfqPswUDSlwKk1g26S6TwHBNO-fYz2ikLe&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEkFcJNaQk0wDOCGLETwtus6rEa2tZVM1WMDr6WLftojw&oe=67F40D8A",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 6,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRD79dU7c7rP2bE9WhfAs4h5OahvtzgJ2Oh456mpIWmed1KE_2LckomSP2_AY9kMH9Ws7sY5qYtgZSpovpPPFutA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573015719772",
                                                                                    "name": "Dương Duy Năm",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-3.fna.fbcdn.net/v/t39.30808-1/480045626_122102346224767190_6139893211204722726_n.jpg?stp=c0.23.203.203a_cp0_dst-jpg_s40x40_tt6&_nc_cat=108&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=c3KzHh0M4o4Q7kNvgGsml8h&_nc_oc=AdmUcClGhaAuLOuwEAiMS7nmneQ7mC_CI8W_o7hNy_RasOGnal1QQqhy4_DwLe0M-A9zzoesrJSqC4YCOkv9BEBY&_nc_zt=24&_nc_ht=scontent.fhan2-3.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEz1Gol3kUn9bC4IGuZipocFRaiFaHvmg7JxbCJlftENA&oe=67F423E4",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "551153321418862"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRjMCl0hjOxdkGa9P7V7uvKECrwxO6kfSZB_uNlQbkV-0kBnI6ysIcYRpnfLTKGM4K-k386HvJzN_PTHRatuCB2w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61568771054821",
                                                                                    "name": "Minh Đức",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/468154565_122104593254625701_4021722386690848790_n.jpg?stp=c58.0.176.176a_cp0_dst-jpg_s40x40_tt6&_nc_cat=104&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=J6_pdpDBmukQ7kNvgH3KB_s&_nc_oc=Adlvef9fkVVHHpP3CDLz_BiYBqagCq_n1uV2DPpFtyNgPYQesAcPva7hJfYx2EapDsORrp-FQqEjDYOpOkvc3HC8&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEPO0OoIyNcTk3QNOaRqybxbAm_o9RXeOhPu-J4ZRmSvQ&oe=67F4180F",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 14,
                                                                                    "delegate_page_id": "522263997626964"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRaZtlzBc7eiNK3DqrzanOrkbcjy9fCOyqyJ0M0IF_hb5ew2ayxxvlzQEkOyuVFfTVu_8OVeemo6CgbEZR_S39YA"
                                                                        }
                                                                    ],
                                                                    "page_info": {
                                                                        "end_cursor": "AQHRXqKCFTfhiUH893wt15IQmvOMckBufl6UkQwKyJpA2WRJVQAaeCUMbXf4oPwOUpGTJdnBqqe6KLqUxFc1YdvdGQ",
                                                                        "has_next_page": True
                                                                    }
                                                                },
                                                                "is_failing_page_publishing_authorization": False,
                                                                "profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYESk-zl4tr9LVQed55X4Ho5fNGVA3jhhbR_UcKegQQfbA&oe=67F3F481",
                                                                    "width": 40,
                                                                    "height": 40,
                                                                    "scale": 1
                                                                },
                                                                "unseen_update_count": 0,
                                                                "is_additional_profile_plus": False,
                                                                "profile_count": {"count": 19},
                                                                "profile_switcher_unread_notifications": 68
                                                            },
                                                            "settings_menu_business_suite": {
                                                                "should_show_entrypoint": False,
                                                                "bizweb_home_link": "https://business.facebook.com/latest/home?nav_ref=fb_web_pplus_settings_menu"
                                                            },
                                                            "additional_profile_creation_eligibility": {
                                                                "should_show_soap_creation_settings_dropdown_entrypoint": False,
                                                                "single_owner": {
                                                                    "can_create": False,
                                                                    "explanation": "Bạn chỉ có thể có 2 trang cá nhân bổ sung cùng lúc. Bạn có thể vào phần cài đặt trang cá nhân để xóa trang cá nhân bổ sung."
                                                                }
                                                            },
                                                            "is_eligible_for_account_level_settings": True,
                                                            "can_access_privacy_checkup": True,
                                                            "privacy_center": {"should_show_privacy_center": True},
                                                            "device_switchable_accounts": [
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "short_name": "Thương Lan",
                                                                        "name": "Thương Lan Ngô",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_a_g"},
                                                                            {"name": "next", "value": "/?next_cuid=AYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid0SnxDyAeig17C1AU6cFeahtBYrnZqfLrHdr12u2uSDz6u8GLYkaywk1KEJR715EeXl",
                                                                        "short_name": "David",
                                                                        "name": "David Edward Smith",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_2w0"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid02wn8bxaW4ip3uyHZuUi1KGeJ76UK7JHLnzKj5hvNvKHxQdpwbP5YYgCzwH6WEjPHBl",
                                                                        "short_name": "Robert",
                                                                        "name": "Robert David Williams",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_Cso"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE"}
                                                                        ]
                                                                    }
                                                                }
                                                            ],
                                                            "first_account": [
                                                                {
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "profile_picture": {
                                                                            "scale": 1,
                                                                            "height": 40,
                                                                            "width": 40,
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A"
                                                                        }
                                                                    }
                                                                }
                                                            ],
                                                            "logout_hash": "AfdHNYKHLQEwmbe_uqY"
                                                        },
                                                        "intl_locale_selector_query": {
                                                            "current_locale": {"localized_name": "Tiếng Việt"}
                                                        },
                                                        "logout_whitelist": [
                                                            "^CacheStorageVersion$",
                                                            "^RTC_VIDEO_INPUT$",
                                                            "^RTC_AUDIO_INPUT$",
                                                            "^RTC_AUDIO_OUTPUT$",
                                                            "^RTC_IS_AUDIO_ONLY$",
                                                            "^RTC_NOISE_SUPPRESSION$",
                                                            "^RTC_LOBBY_MUTE_STATE$",
                                                            "^Session$",
                                                            "^_oz_",
                                                            "^_video_bandwidthEstimate$",
                                                            "^Banzai$",
                                                            "^bz",
                                                            "^banzai\\:last_storage_flush$",
                                                            "^falco_queue_",
                                                            "^mutex",
                                                            "^msys",
                                                            "^Bandicoot\\:",
                                                            "^imp_seq_num$",
                                                            "^qe_switcher_nub_selection$",
                                                            "^TabId$",
                                                            "^sp_pi$",
                                                            "^\\:userchooser\\:osessusers$",
                                                            "^\\:userchooser\\:settings$",
                                                            "^brands\\:console\\:config$",
                                                            "^consoleEnabled$",
                                                            "^__fb_messenger_desktop_presence_info$",
                                                            "^vc_",
                                                            "^_showMDevConsole$",
                                                            "^ga_client_id$",
                                                            "^ga4_client_id$",
                                                            "^_mswam_$",
                                                            "^am_recently_used_filters\\:",
                                                            "^am_image_size_cache$",
                                                            "^ickt$",
                                                            "^hb_timestamp$",
                                                            "^signal_flush_timestamp$",
                                                            "^__MWCMAutoJoinNotifNuxBanner\\.showBanner__$",
                                                            "^last_fast_refresh$",
                                                            "^_ctv_access_token$",
                                                            "^_ctv_android_device_info$",
                                                            "^_ctv_cast_access_token$",
                                                            "^_ctv_casting_remote$",
                                                            "^_ctv_console_log_viewer_on_full_screen_player_enabled$",
                                                            "^_ctv_cookie_consent_displayed$",
                                                            "^_ctv_debug_redux_logger_enabled$",
                                                            "^_ctv_deviceUniqueIDFallback$",
                                                            "^_ctv_gaming_consent_displayed$",
                                                            "^_ctv_installed_app_player_debug_overlay_enabled$",
                                                            "^_ctv_last_load_time_ms$",
                                                            "^_ctv_locale$",
                                                            "^_ctv_logged_out_constraints_sessions_count$",
                                                            "^_ctv_reloadedDueToStaleApp$",
                                                            "^_ctv_reloadedDueToUnrecoverableError$",
                                                            "^_ctv_search_terms$",
                                                            "^_ctv_tv_experiments$",
                                                            "^_ctv_usedCloseAppFallback$",
                                                            "^_ctv_user_sessions$",
                                                            "^_ctv_video_debug_overlay_enabled$",
                                                            "^_ctv_debug_rampart_server_number$",
                                                            "^fx_did$",
                                                            "^wa_lang_banner_dismissed$",
                                                            "^bulletin_article_reader_onload_dialog_seen$",
                                                            "^bulletin_session_attributes$",
                                                            "^md_survey$",
                                                            "^support_guest_chat$",
                                                            "^comet_is_recent_profile_switch$",
                                                            "^comet_console_position$",
                                                            "^mw_exchange_vm$",
                                                            "^has_seen_email_login_toast$",
                                                            "^cs_chat_support_user$",
                                                            "^NFT_DEVICE_KEY_PRIVATE_V1$",
                                                            "^NFT_DEVICE_KEY_PUBLIC_V1$",
                                                            "^show_wa_auth_button$",
                                                            "^BusinessInbox\\:sortMethod$",
                                                            "^LeadsCenter\\:ViewType$",
                                                            "^BizWebInsightsLeadsCenterHeaderGuidanceCard\\:LastClosedTime$",
                                                            "^Routing\\:url\\:AdsTALRouting$",
                                                            "^BizWebDirectResponseAdsBannerView$",
                                                            "^firefly_auth_tokens$",
                                                            "^BizWebStoryInsightsOptInBannerView$",
                                                            "^fair_ai_demos_rid$",
                                                            "^videoseal_tos_accepted$",
                                                            "^videoseal_user_rid$",
                                                            "^seen_password_entry_auto_prompt$",
                                                            "^trusted_devices_storage_version$"
                                                        ],
                                                        "fxcal_settings": {"ac_phase": "CENTRALIZED_SETTINGS_NO_SENSITIVE"}
                                                    },
                                                    "extensions": {"is_final": True}
                                                },
                                                "sequence_number": 0
                                            }
                                        }
                                    ]
                                ]
                            ]
                        }
                    },
                    {"__bbox": None},
                    {"__bbox": None}
                ]
            ]
        ]
    }

    # Trích xuất fb_dtsg và jazoest từ JSON
    try:
        device_switchable_accounts = response['require'][0][3][0]['__bbox']['require'][0][3][1]['__bbox']['result']['data']['viewer']['actor']['device_switchable_accounts']
        if not device_switchable_accounts:
            print("\033[1;31mLỗi: Không tìm thấy device_switchable_accounts trong JSON.")
            return None

        # Lấy fb_dtsg và jazoest từ account đầu tiên
        form_inputs = device_switchable_accounts[0]['form']['inputs']
        fb_dtsg = next(item['value'] for item in form_inputs if item['name'] == 'fb_dtsg')
        jazoest = next(item['value'] for item in form_inputs if item['name'] == 'jazoest')
    except (KeyError, StopIteration) as e:
        print(f"\033[1;31mLỗi: Không thể trích xuất fb_dtsg hoặc jazoest: {e}")
        return None

    # Trích xuất danh sách pages từ JSON
    try:
        a = response['require'][0][3][0]['__bbox']['require'][0][3][1]['__bbox']['result']['data']['viewer']['actor']['profiles']['edges']
        # Chuyển đổi định dạng để phù hợp với mã hiện tại (chỉ lấy phần node.profile)
        a = [edge['node']['profile'] for edge in a]
    except (KeyError, ValueError) as e:
        print(f"\033[1;31mLỗi: Không thể lấy danh sách pages: {e}")
        return None

    # Hiển thị danh sách pages
    sl = 0
    for b in a:
        sl += 1
        uid = b['id']
        name = b['name']
        delegate_page_id = b['delegate_page_id']
        print(f"\033[1;37mPAGE : {sl} | ID : {uid} | Name : {name} ")
        print('\033[1;31m────────────────────────────────────────────────────────────')
    return a

def get_data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = {
        "require": [
            [
                "ScheduledServerJS",
                "handle",
                None,
                [
                    {
                        "__bbox": {
                            "require": [
                                [
                                    "RelayPrefetchedStreamCache",
                                    "next",
                                    [],
                                    [
                                        "adp_CometSettingsDropdownListQueryRelayPreloader_67ee393b843272054669835",
                                        {
                                            "__bbox": {
                                                "complete": True,
                                                "result": {
                                                    "data": {
                                                        "viewer": {
                                                            "actor": {
                                                                "__typename": "User",
                                                                "profileSwitcherEligibleProfiles": {"count": 19},
                                                                "id": "61559472533015",
                                                                "name": "Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức Ng\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Minh\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u3000Đức",
                                                                "settings_dropdown_profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s60x60_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYG2uYN62pnKQ4kj4Q2gUY1d-oD6puoB0i7aAinviXkboQ&oe=67F3F481"
                                                                },
                                                                "first_profiles": {
                                                                    "nodes": [
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573311838392",
                                                                                "name": "Dương Quỳnh Anh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C"
                                                                                }
                                                                            }
                                                                        },
                                                                        {
                                                                            "profile": {
                                                                                "id": "61573471253195",
                                                                                "name": "Đặng Công Danh",
                                                                                "quick_switch_picture": {
                                                                                    "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767"
                                                                                }
                                                                            }
                                                                        }
                                                                    ]
                                                                },
                                                                "should_show_account_level_settings": True,
                                                                "username": "ng.minh.duck210",
                                                                "first_profile": {
                                                                    "count": 19,
                                                                    "nodes": [{"profile": {"id": "61573311838392"}}]
                                                                },
                                                                "page_publishing_authorization_hub_action_url": "/id/?referrer=profile_plus_switcher&product=4",
                                                                "page_publishing_authorization_admin_notice": None,
                                                                "profiles": {
                                                                    "edges": [
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573311838392",
                                                                                    "name": "Dương Quỳnh Anh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480692563_122096418458777061_465428377963211871_n.jpg?stp=c0.40.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=V3toBJeNLz4Q7kNvgFTkxI5&_nc_oc=Adl5iWafGVNrWWXO1hqRhmXteLFvWsOaMnOFkGtOsIXlU-2lL6mzeO2zUAbXiA8O4ky_NwclWHAfPDPR0_TokUdh&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYFI6TxCJXxN_OCxTGTH0Lsh-Cisnmhvv18De93NhB1WpQ&oe=67F40D8C",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "597353450119629"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRK_I_H1EE1sKXmIwcnrsWtSnMwIc4xa33WOI6l7SdlGTQVKqE7rynm4mwVC40wm5-sPGOL7O4TM9QX0N26mAlpA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573471253195",
                                                                                    "name": "Đặng Công Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/480664924_122094171224782375_4519853174386113015_n.jpg?stp=c0.18.194.194a_cp0_dst-jpg_s40x40_tt6&_nc_cat=106&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=CNkby00EuycQ7kNvgH4yl5j&_nc_oc=AdmD3dzlHU_u_bhg8LccIDVoeJTf1S21HzrVYzlxHKK2bSGB6vjMhzVVjhCc5YXiGv0RjI7K4ujnsddYS0Qn0_Uf&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEEahXC5U388MdCcGLk7ygua2XL17ciHBPiVgihR2AnWQ&oe=67F41767",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "609933448859519"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR25TAIHQspV7vNdWrMPF28kYU-mC-XLD-TQVe44hZ48hWm4khvUBYmkthOsfaUO0Pb0R_FcLsqy-0qGCcd9aT3w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573277518825",
                                                                                    "name": "Đặng Công Hào",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480325538_122163563582315751_6859066577211977932_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=111fe6&_nc_ohc=DN5jjO443DEQ7kNvgF5S19j&_nc_oc=AdmNaslAvS7tc1RPgE04qNPAWHIGpAyPdVt8-sTc090Ouet9gyd83RF0wavc3NXCEIDKjYxrxmUF4QLTN2OnsUGq&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYGRXR18kvmFJPzj1SGg9GmNwlD-xkUT1_ha5-ZM2PTRHg&oe=67F40BE9",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRNuPvMJWqVwGZvBAvcAPc8T7gx1mRAftirEqxHSOMT_VlQqqpC8fgZ9Z9gzFFTkeleX9pkrgQwC02XyFTmFM65A"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573005310570",
                                                                                    "name": "Đinh Đức Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480240676_122102774600766843_3156531964467906790_n.jpg?stp=c0.65.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=103&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=jbb3Q-KMvQwQ7kNvgH5Sbyo&_nc_oc=AdmF95RXt4ptdi2yG6yzV6tZYRQKRlqp5bl1Y22O1A1YLUM7EH6EM5CpmJW5Q5hdL_pOnuW_KsMfI33afXvK5zRz&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEap0dzqFz1QJtFqnUm1gAAP72cku_rjtjfP5gLj0iajA&oe=67F425C6",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 3,
                                                                                    "delegate_page_id": "517677294771234"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRTgvMDjZgq1xUTacT5uW5NkAHOMlbuv8eqmiCou0KJr44YnhCgMbw2bPuRGJDUOpY05Wa-xNR9wRtpAQd1iIQYw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573106105525",
                                                                                    "name": "Đinh Vĩnh Danh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/480506539_122100039416770203_4952372284759289001_n.jpg?stp=c0.263.675.675a_cp0_dst-jpg_s40x40_tt6&_nc_cat=105&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=lGy_-cQ8gZQQ7kNvgHYg1gm&_nc_oc=AdmufYTW-lgT432Gvk521V3lM_o0HbeiOFknY2xEfoXJ0bsb5xtF4o4E9HLl8_tInB9thTIUwTutNyKapnxYotC9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYErruwK0gV6VVQ0JIaysfuDP90p9zi-y0JLYiAnBniUSA&oe=67F41747",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "620655147788759"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHR9d_kNnKvbYCL3OlXqLrVD2Tk2wZ52mV60KoWlxgcbE4FaX52vZjMxrae2ikoYCA7AvULCuN2iQOQAAU5pmfyQg"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573093445871",
                                                                                    "name": "Bùi Công Tuấn",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan20-1.fna.fbcdn.net/v/t39.30808-1/480502745_122099701784769781_5642310825084805014_n.jpg?stp=c0.0.236.236a_cp0_dst-jpg_s40x40_tt6&_nc_cat=102&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=t9MWVtlBuI0Q7kNvgFVA8jA&_nc_oc=AdnJTiaykIXnTl25_VfEuk2C3sY51cYZmnE15oxCLvhQIYtZT0jHvsbHMHtCy9WkPe1HrqUvyAdUb-mRwsXXROEQ&_nc_zt=24&_nc_ht=scontent.fhan20-1.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYHFoKc7r_31WhFzYXNJyF7kXZpAUCYDObeIjs1PurBAKg&oe=67F416A7",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 0,
                                                                                    "delegate_page_id": "554142717786080"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRKQfQOvOnYbNf90JLm2U8iiBKUWKWNUcPf9Pje0Va5FJUkFLLFesAQbGWcq9sXVBSADq4Z-OrK9v2Gr0rm-E5Dw"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61567577686564",
                                                                                    "name": "Hoàng Sinh",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/479939442_122131664672585922_990255040247358089_n.png?stp=cp0_dst-png_p40x40&_nc_cat=110&ccb=1-7&_nc_sid=111fe6&_nc_ohc=0XYiKz8UApQQ7kNvgF4D301&_nc_oc=Adk-Gg9M4eW00HsbLrt_4fbVigvG5UWTNUlhhEC7WX7oH7MKhYjM2HJfqPswUDSlwKk1g26S6TwHBNO-fYz2ikLe&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEkFcJNaQk0wDOCGLETwtus6rEa2tZVM1WMDr6WLftojw&oe=67F40D8A",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 6,
                                                                                    "delegate_page_id": None
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRD79dU7c7rP2bE9WhfAs4h5OahvtzgJ2Oh456mpIWmed1KE_2LckomSP2_AY9kMH9Ws7sY5qYtgZSpovpPPFutA"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61573015719772",
                                                                                    "name": "Dương Duy Năm",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-3.fna.fbcdn.net/v/t39.30808-1/480045626_122102346224767190_6139893211204722726_n.jpg?stp=c0.23.203.203a_cp0_dst-jpg_s40x40_tt6&_nc_cat=108&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=c3KzHh0M4o4Q7kNvgGsml8h&_nc_oc=AdmUcClGhaAuLOuwEAiMS7nmneQ7mC_CI8W_o7hNy_RasOGnal1QQqhy4_DwLe0M-A9zzoesrJSqC4YCOkv9BEBY&_nc_zt=24&_nc_ht=scontent.fhan2-3.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEz1Gol3kUn9bC4IGuZipocFRaiFaHvmg7JxbCJlftENA&oe=67F423E4",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 1,
                                                                                    "delegate_page_id": "551153321418862"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRjMCl0hjOxdkGa9P7V7uvKECrwxO6kfSZB_uNlQbkV-0kBnI6ysIcYRpnfLTKGM4K-k386HvJzN_PTHRatuCB2w"
                                                                        },
                                                                        {
                                                                            "node": {
                                                                                "profile": {
                                                                                    "id": "61568771054821",
                                                                                    "name": "Minh Đức",
                                                                                    "profile_picture": {
                                                                                        "uri": "https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-1/468154565_122104593254625701_4021722386690848790_n.jpg?stp=c58.0.176.176a_cp0_dst-jpg_s40x40_tt6&_nc_cat=104&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=J6_pdpDBmukQ7kNvgH3KB_s&_nc_oc=Adlvef9fkVVHHpP3CDLz_BiYBqagCq_n1uV2DPpFtyNgPYQesAcPva7hJfYx2EapDsORrp-FQqEjDYOpOkvc3HC8&_nc_zt=24&_nc_ht=scontent.fhan2-5.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYEPO0OoIyNcTk3QNOaRqybxbAm_o9RXeOhPu-J4ZRmSvQ&oe=67F4180F",
                                                                                        "width": 40,
                                                                                        "height": 40,
                                                                                        "scale": 1
                                                                                    },
                                                                                    "unseen_update_count": 14,
                                                                                    "delegate_page_id": "522263997626964"
                                                                                },
                                                                                "__typename": "ProfileSwitcherEligibleProfile"
                                                                            },
                                                                            "cursor": "AQHRaZtlzBc7eiNK3DqrzanOrkbcjy9fCOyqyJ0M0IF_hb5ew2ayxxvlzQEkOyuVFfTVu_8OVeemo6CgbEZR_S39YA"
                                                                        }
                                                                    ],
                                                                    "page_info": {
                                                                        "end_cursor": "AQHRXqKCFTfhiUH893wt15IQmvOMckBufl6UkQwKyJpA2WRJVQAaeCUMbXf4oPwOUpGTJdnBqqe6KLqUxFc1YdvdGQ",
                                                                        "has_next_page": True
                                                                    }
                                                                },
                                                                "is_failing_page_publishing_authorization": False,
                                                                "profile_picture": {
                                                                    "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-1/477789840_122163129266315751_284597210316817088_n.jpg?stp=cp0_dst-jpg_s40x40_tt6&_nc_cat=100&ccb=1-7&_nc_sid=e99d92&_nc_ohc=M-gQDSdAVQIQ7kNvgHA1HX-&_nc_oc=Adn67uaSTykeEC12B8_8oM0wcQ85qvjlTgK9tINq45c014ggM5OWqwm1KWo6stlQi45iKd9oxizZ-_DhkIAhI6V9&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&_nc_gid=4GW-DKsJnK35EQDQgfWIeg&oh=00_AYESk-zl4tr9LVQed55X4Ho5fNGVA3jhhbR_UcKegQQfbA&oe=67F3F481",
                                                                    "width": 40,
                                                                    "height": 40,
                                                                    "scale": 1
                                                                },
                                                                "unseen_update_count": 0,
                                                                "is_additional_profile_plus": False,
                                                                "profile_count": {"count": 19},
                                                                "profile_switcher_unread_notifications": 68
                                                            },
                                                            "settings_menu_business_suite": {
                                                                "should_show_entrypoint": False,
                                                                "bizweb_home_link": "https://business.facebook.com/latest/home?nav_ref=fb_web_pplus_settings_menu"
                                                            },
                                                            "additional_profile_creation_eligibility": {
                                                                "should_show_soap_creation_settings_dropdown_entrypoint": False,
                                                                "single_owner": {
                                                                    "can_create": False,
                                                                    "explanation": "Bạn chỉ có thể có 2 trang cá nhân bổ sung cùng lúc. Bạn có thể vào phần cài đặt trang cá nhân để xóa trang cá nhân bổ sung."
                                                                }
                                                            },
                                                            "is_eligible_for_account_level_settings": True,
                                                            "can_access_privacy_checkup": True,
                                                            "privacy_center": {"should_show_privacy_center": True},
                                                            "device_switchable_accounts": [
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "short_name": "Thương Lan",
                                                                        "name": "Thương Lan Ngô",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_a_g"},
                                                                            {"name": "next", "value": "/?next_cuid=AYiAqAyFaIj1Jqiv5QQRzxT2KkdEs3DGX0M-U7DorJhkReYn4YRXRZsAvkeWJKhRoWDmFvubz2vPbzDRBZydkvbFEsDzDVJEggSYVy3EKT0-KxBFcsoKIWEbNIkVWvEDqKIu6VUSouCA_iggrKqxe4_xF3ijyHefoMnRSN_LKYp9rA"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid0SnxDyAeig17C1AU6cFeahtBYrnZqfLrHdr12u2uSDz6u8GLYkaywk1KEJR715EeXl",
                                                                        "short_name": "David",
                                                                        "name": "David Edward Smith",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_2w0"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjB_gFpg0k4tuEzKsfFagZzQKi-EA23JO0ofXvJQPHU4pEHCaU4k6AbsF0Zv_W85GDSuqZ9Cra-jRd-smqBJSc2sCtBtLhiMK0qSsnrmSU_QzP6lRO8bHPbnfbJlZI0_IZ6v2KLJJkQw5XRmlODbbZA_EaYtEtAHEXUKXQ4vrp90Q"}
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "__typename": "LoggedInAccountSwitcherAccount",
                                                                    "unread_notification_count": 0,
                                                                    "user": {
                                                                        "id": "pfbid02wn8bxaW4ip3uyHZuUi1KGeJ76UK7JHLnzKj5hvNvKHxQdpwbP5YYgCzwH6WEjPHBl",
                                                                        "short_name": "Robert",
                                                                        "name": "Robert David Williams",
                                                                        "switcher_profile_picture": {
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A",
                                                                            "width": 40,
                                                                            "height": 40,
                                                                            "scale": 1
                                                                        }
                                                                    },
                                                                    "nonce": None,
                                                                    "form": {
                                                                        "action": "https://www.facebook.com/logout.php?next=%2F%3Fnext_cuid%3DAYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE&button_name=switch_accounts",
                                                                        "inputs": [
                                                                            {"name": "fb_dtsg", "value": "NAcNnepZhAezny-XTjx00I5F4SDIDAYQrmOkrtZKRuln4jXf1DWqKKQ:1:1743519165"},
                                                                            {"name": "jazoest", "value": "25474"},
                                                                            {"name": "ref", "value": "mb"},
                                                                            {"name": "h", "value": "AfdHNYKHLQEwmbe_Cso"},
                                                                            {"name": "next", "value": "/?next_cuid=AYjAUBZeO9oVxXSSUGfFsNn3QnZQ2dT05Q3gvOs_iKLbfon-MO4Bo5laLDVpVdmviFQEEcp4AptpHOKBpnchcFbO89osrcYW8cc3HPRkZcFnQ76uxbGlrtknSbgPchyGX_VRt9SofAQ6JdnHRSfNcvjxvoTLz8A-rChUop09Lj19EDUo7O_S0ioZdy71OCH4hoE"}
                                                                        ]
                                                                    }
                                                                }
                                                            ],
                                                            "first_account": [
                                                                {
                                                                    "unread_notification_count": 1,
                                                                    "user": {
                                                                        "id": "pfbid02XqXT2tgnLpWcCRjxK4dVTu27Zt3Lm1aGGgg47QcbDHPjrByAWw9VeufSXd5LGPPrl",
                                                                        "profile_picture": {
                                                                            "scale": 1,
                                                                            "height": 40,
                                                                            "width": 40,
                                                                            "uri": "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.30497-1/453178253_471506465671661_2781666950760530985_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=136b72&_nc_ohc=1BwdynYvBPkQ7kNvgFerwYW&_nc_oc=AdkUQzBe7qZ7kCtpwhVLP0fLF9R7BW7of4ocQ1TVHvNQ9Cl6LmUEadcz4aAsLeVg4ExZVMP1IH4zDu5nBAGllq2c&_nc_zt=24&_nc_ht=scontent.fhan2-4.fna&oh=00_AYFLU6MHCoD5C3iRITgANWO_T_1014meXs_TvEROxZs_2w&oe=6815A17A"
                                                                        }
                                                                    }
                                                                }
                                                            ],
                                                            "logout_hash": "AfdHNYKHLQEwmbe_uqY"
                                                        },
                                                        "intl_locale_selector_query": {
                                                            "current_locale": {"localized_name": "Tiếng Việt"}
                                                        },
                                                        "logout_whitelist": [
                                                            "^CacheStorageVersion$",
                                                            "^RTC_VIDEO_INPUT$",
                                                            "^RTC_AUDIO_INPUT$",
                                                            "^RTC_AUDIO_OUTPUT$",
                                                            "^RTC_IS_AUDIO_ONLY$",
                                                            "^RTC_NOISE_SUPPRESSION$",
                                                            "^RTC_LOBBY_MUTE_STATE$",
                                                            "^Session$",
                                                            "^_oz_",
                                                            "^_video_bandwidthEstimate$",
                                                            "^Banzai$",
                                                            "^bz",
                                                            "^banzai\\:last_storage_flush$",
                                                            "^falco_queue_",
                                                            "^mutex",
                                                            "^msys",
                                                            "^Bandicoot\\:",
                                                            "^imp_seq_num$",
                                                            "^qe_switcher_nub_selection$",
                                                            "^TabId$",
                                                            "^sp_pi$",
                                                            "^\\:userchooser\\:osessusers$",
                                                            "^\\:userchooser\\:settings$",
                                                            "^brands\\:console\\:config$",
                                                            "^consoleEnabled$",
                                                            "^__fb_messenger_desktop_presence_info$",
                                                            "^vc_",
                                                            "^_showMDevConsole$",
                                                            "^ga_client_id$",
                                                            "^ga4_client_id$",
                                                            "^_mswam_$",
                                                            "^am_recently_used_filters\\:",
                                                            "^am_image_size_cache$",
                                                            "^ickt$",
                                                            "^hb_timestamp$",
                                                            "^signal_flush_timestamp$",
                                                            "^__MWCMAutoJoinNotifNuxBanner\\.showBanner__$",
                                                            "^last_fast_refresh$",
                                                            "^_ctv_access_token$",
                                                            "^_ctv_android_device_info$",
                                                            "^_ctv_cast_access_token$",
                                                            "^_ctv_casting_remote$",
                                                            "^_ctv_console_log_viewer_on_full_screen_player_enabled$",
                                                            "^_ctv_cookie_consent_displayed$",
                                                            "^_ctv_debug_redux_logger_enabled$",
                                                            "^_ctv_deviceUniqueIDFallback$",
                                                            "^_ctv_gaming_consent_displayed$",
                                                            "^_ctv_installed_app_player_debug_overlay_enabled$",
                                                            "^_ctv_last_load_time_ms$",
                                                            "^_ctv_locale$",
                                                            "^_ctv_logged_out_constraints_sessions_count$",
                                                            "^_ctv_reloadedDueToStaleApp$",
                                                            "^_ctv_reloadedDueToUnrecoverableError$",
                                                            "^_ctv_search_terms$",
                                                            "^_ctv_tv_experiments$",
                                                            "^_ctv_usedCloseAppFallback$",
                                                            "^_ctv_user_sessions$",
                                                            "^_ctv_video_debug_overlay_enabled$",
                                                            "^_ctv_debug_rampart_server_number$",
                                                            "^fx_did$",
                                                            "^wa_lang_banner_dismissed$",
                                                            "^bulletin_article_reader_onload_dialog_seen$",
                                                            "^bulletin_session_attributes$",
                                                            "^md_survey$",
                                                            "^support_guest_chat$",
                                                            "^comet_is_recent_profile_switch$",
                                                            "^comet_console_position$",
                                                            "^mw_exchange_vm$",
                                                            "^has_seen_email_login_toast$",
                                                            "^cs_chat_support_user$",
                                                            "^NFT_DEVICE_KEY_PRIVATE_V1$",
                                                            "^NFT_DEVICE_KEY_PUBLIC_V1$",
                                                            "^show_wa_auth_button$",
                                                            "^BusinessInbox\\:sortMethod$",
                                                            "^LeadsCenter\\:ViewType$",
                                                            "^BizWebInsightsLeadsCenterHeaderGuidanceCard\\:LastClosedTime$",
                                                            "^Routing\\:url\\:AdsTALRouting$",
                                                            "^BizWebDirectResponseAdsBannerView$",
                                                            "^firefly_auth_tokens$",
                                                            "^BizWebStoryInsightsOptInBannerView$",
                                                            "^fair_ai_demos_rid$",
                                                            "^videoseal_tos_accepted$",
                                                            "^videoseal_user_rid$",
                                                            "^seen_password_entry_auto_prompt$",
                                                            "^trusted_devices_storage_version$"
                                                        ],
                                                        "fxcal_settings": {"ac_phase": "CENTRALIZED_SETTINGS_NO_SENSITIVE"}
                                                    },
                                                    "extensions": {"is_final": True}
                                                },
                                                "sequence_number": 0
                                            }
                                        }
                                    ]
                                ]
                            ]
                        }
                    },
                    {"__bbox": None},
                    {"__bbox": None}
                ]
            ]
        ]
    }

    fb_dtsg = next(item['value'] for item in form_inputs if item['name'] == 'fb_dtsg')
    jazoest = next(item['value'] for item in form_inputs if item['name'] == 'jazoest')
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def login_tds(token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			return r
		else:
			print(" \033[1;31m Token TDS không hợp lệ, hãy kiểm tra lại!\n")
			return 'error_token'
	except:
		return 'error'

def load_job(type, TDS_token):
		r = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}')


def type_cx(type_1) :
	if type_1 == "LOVE" :
		type_2 = '1678524932434102'
	elif type_1 == "CARE" :
		type_2 = '613557422527858'
	elif type_1 == "WOW" :
		type_2 = '478547315650144'
	elif type_1 == "HAHA" :
		type_2 = '115940658764963'
	elif type_1 == "SAD" :
		type_2 = '908563459236466'
	elif type_1 == "ANGRY" :
		type_2 = '444813342392137'
		
	return type_2
def cau_hinh(id, TDS_token, name):
	urlch = f"https://traodoisub.com/api/?fields=run&id={id}&access_token={TDS_token}'"
	ch = requests.get( url=urlch)
	try: 
		checkch = ch.json()["data"]["msg"]
		print(f" \033[1;32mCấu Hình \033[1;37m| \033[1;33mID : \033[1;32m{id} \033[1;37m| \033[1;32mName : \033[1;33m{name} ")
	except:
		print(f" \033[1;31m Cấu Hình Thất Bại {id} ")
		exit ()
banner = f"""
\033[1;32m════════════════════════════════════════════════════╗
\033[1;32m║\033[1;37m██╗░░██╗░█████╗░██████╗░██╗  ██████╗░░██╗░░░░░░░██╗\033[1;32m║
\033[1;32m║\033[1;37m██║░░██║██╔══██╗██╔══██╗██║  ██╔══██╗░██║░░██╗░░██║\033[1;32m║
\033[1;32m║\033[1;37m███████║███████║██████╔╝██║  ██║░░██║░╚██╗████╗██╔╝\033[1;32m║
\033[1;32m║\033[1;37m██╔══██║██╔══██║██╔══██╗██║  ██║░░██║░░████╔═████║░\033[1;32m║
\033[1;32m║\033[1;37m██║░░██║██║░░██║██║░░██║██║  ██████╔╝░░╚██╔╝░╚██╔╝░\033[1;32m║ 
\033[1;32m║\033[1;37m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░\033[1;32m║  
\033[1;32m╠═══════════════════════════════════════════════════╣
\033[1;32m║\033[1;34m▶ tele : \033[1;37mDw_111                                    \033[1;32m║
\033[1;32m╠\033[1;34m▶ zalo : \033[1;37m0327921302                                \033[1;32m║
\033[1;32m╚═══════════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""

def chon_job(so,chon):
	if chon == 1 :
		if so == 4 :
			so -= 4 
		else :
			type = ['like','likegiare','likesieure','reaction']
			job = type[so]
	elif chon == 2 :
		job = "group"
	elif chon == 3 :
		job = "follow"
	elif chon == 4:
		if so == 5 :
			so -= 5 
		else :
			type = ['like','likegiare','likesieure','reaction','group']
			job = type[so]
	else :
		if so == 6 :
			so -= 6 
		else :
			type = ['like','likegiare','likesieure','reaction','group','follow']
			
			job = type[so]
	return job



os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
so = 0
token = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Token TDS :\033[1;33m ')
check_xu = login_tds(token)
print ('\033[1;31m────────────────────────────────────────────────────────────')
cookie = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Cookie Facebook :\033[1;33m ')
print ('\033[1;31m────────────────────────────────────────────────────────────')
#### vào việc
get_tt_page = get_page(cookie)
if get_tt_page is None:
    print("\033[1;31mExiting due to error in fetching page data.")
    exit()

a = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBạn Muốn Chạy Page Thứ Mấy : \033[1;33m'))
chon = a-1
print ('\033[1;31m────────────────────────────────────────────────────────────')
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập 1 \033[1;37mJob Like + Cảm Xúc")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập 2 \033[1;37mJob Group")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập 3 \033[1;37mJob Follow ")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập 4 \033[1;37mJob Group + Like + Cảm Xúc")
print ("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập 5 \033[1;37mJob Group + Like + Cảm Xúc + Follow ")
chon_1 = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập : \033[1;33m '))
print ('\033[1;31m────────────────────────────────────────────────────────────')
dl = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Delay : \033[1;33m '))

id_page = get_tt_page[chon]['profile']['id']
name = get_tt_page[chon]['profile']['name']
ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
data = get_data(cookie)
fb_dtsg = json.loads(data)['fb_dtsg']
jazoet = json.loads(data)['jazoet']
fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
tt = 0

os.system('clear')
print(banner)
tdstk = check_xu['data']['user']
xu_5 = check_xu['data']['xu']
print (f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mTài Khoản: \033[1;33m{tdstk} \n\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mXu Hiện Tại : \033[1;33m{xu_5} ")

print ('\033[1;31m────────────────────────────────────────────────────────────')
cau_hinh(id_page, token, name)
print ('\033[1;31m────────────────────────────────────────────────────────────')
while True :
	print(" Đang Tìm Job ",end="\r")
	if so == 5 :
		so -= 5
	else :
		
		job = chon_job(so,chon_1)
		print(f" \033[1;37mĐang Tìm Job ☞ (⁠>{job}<⁠)       ",end="\r")
		job_1 = requests.get(f'https://traodoisub.com/api/?fields={job}&access_token={token}')
		so += 1
		
		a = job_1.json()
		try :
			b = a["error"] 
			
			if chon_1 == 1 :
				if so == 4 :
					for i in range(20,-1,-1):
						print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
						sleep(1)
			elif chon_1 == 2 :
				for i in range(50,-1,-1):
					print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
					sleep(1)
			else :
				if so == 5 :
					for i in range(20,-1,-1):
						print(f'\033[1;37m[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
						sleep(1)
		except :
			for job_2 in a:
				id_job = job_2["id"]
				if job == "like" :
					type_1 = "LIKE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likegiare" :
					type_1 = "LIKEGIARE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likesieure" :
					type_1 = "LIKESIEURE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "reaction" :
					type_1 = job_2["type"]
					type_2 = type_cx(type_1) 
					lam = fb.reaction(id_job, type_2)
				elif job == "group" :
					type_1 = "GROUP"
					lam = fb.join(id_job)
				elif job == "follow" :
					type_1 = "FOLLOW"
					lam = fb.subscribe(id_job)
					
				nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type_1}&id={id_job}&access_token={token}')
				
				try :
					nhan_1 = nhan.json()["error"] 
					print (f' \033[1;31m ERROR => {id_job} ',end='\r')
					sleep(1)
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					xu_1 = nhan.json()["data"]["msg"]
					xu_2 = nhan.json()["data"]["xu"]
					print (f"\033[1;37m| {tt} | {type_1} | {id_job} | {xu_1} | {xu_2} Xu")
					
				
				for i in range(dl,-1,-1):
					print(f'\033[1;37m[ ĐANG DELAY CHẠY LẠI SAU ] => \033[1;36m {i} GIÂY',end='\r')
					sleep(1)
					
					
					
					
