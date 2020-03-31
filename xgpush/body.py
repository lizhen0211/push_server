class AndroidMessageBody():

    @classmethod
    def get_multupy_push_body_dict(cls, token_list):
        return {'audience_type': 'token_list', 'token_list': token_list, 'message_type': 'notify', 'message': {
            'title': '消息标题',
            'content': '消息内容',
            'android': {
                'action': {
                    "ring": 1,
                    "ring_raw": "ring",
                    "vibrate": 1,
                    "lights": 1,
                    'action_type': 3,  # // 动作类型，1，打开activity或app本身；2，打开浏览器；3，打开Intent
                    'intent': 'xgscheme://com.xg.xgpush/notify_detail'
                }
            }
        }}

    @classmethod
    def get_get_multupy_push_body_str(cls, token_list):
        return str(cls.get_multupy_push_body_dict(token_list))

    @classmethod
    def get_single_push_body_dict(cls, token_list):
        return {'audience_type': 'token', 'token_list': token_list, 'message_type': 'notify', 'message': {
            'title': '消息标题',
            'content': '消息内容',
            'android': {
                'action': {
                    "ring": 1,
                    "ring_raw": "ring",
                    "vibrate": 1,
                    "lights": 1,
                    'action_type': 3,  # // 动作类型，1，打开activity或app本身；2，打开浏览器；3，打开Intent
                    'intent': 'xgscheme://com.xg.xgpush/notify_detail'
                }
            }
        }}

    @classmethod
    def get_single_push_body_str(cls, token_list):
        return str(cls.get_single_push_body_dict(token_list))
