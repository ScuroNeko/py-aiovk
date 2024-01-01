import json
from enum import Enum
from json import JSONEncoder


class EnumEncoder(JSONEncoder):
    def default(self, obj):
        return obj.value


class VkKeyboardColor(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    NEGATIVE = 'negative'
    POSITIVE = 'positive'


class VkKeyboard:
    def __init__(self, one_time=False, inline=False):
        self.inline = inline
        self.lines = [[]]

        self.keyboard = {
            'inline': self.inline,
            'buttons': self.lines
        }
        if not inline:
            self.keyboard['one_time'] = one_time

    def __load_payload(self, payload) -> str:
        if isinstance(payload, str):
            return payload
        elif isinstance(payload, dict):
            return json.dumps(payload)
        elif isinstance(payload, Payload):
            return json.dumps(payload.get())

    def add_text_button(self, text, payload=None, color=VkKeyboardColor.PRIMARY):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'text',
            'label': text
        }
        if payload:
            action.update({'payload': self.__load_payload(payload)})
        button = {
            'color': color,
            'action': action
        }
        current_line.append(button)

    def add_link_button(self, text, link, payload=None):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'open_link',
            'link': link,
            'label': text
        }
        if payload:
            action.update({'payload': self.__load_payload(payload)})
        button = {
            'action': action
        }
        current_line.append(button)

    def add_location_button(self, payload=None):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'location'
        }

        if payload:
            action.update({'payload': self.__load_payload(payload)})

        button = {
            'action': action
        }
        current_line.append(button)

    def add_vk_pay_button(self, hash):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'vkpay',
            'hash': hash
        }
        button = {
            'action': action
        }
        current_line.append(button)

    def add_vk_apps_button(self, label, app_id, owner_id=None, hash=None, payload=None):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'open_app',
            'label': label,
            'app_id': app_id
        }
        if owner_id:
            action.update({'owner_id': owner_id})
        if hash:
            action.update({'hash': hash})
        if payload:
            action.update({'payload': self.__load_payload(payload)})

        button = {
            'action': action
        }
        current_line.append(button)

    def add_callback_button(self, label, payload=None, color=VkKeyboardColor.PRIMARY):
        current_line = self.lines[-1]
        if len(current_line) == 5:
            raise TypeError('max elements in line: 5')

        action = {
            'type': 'callback',
            'label': label
        }

        if payload:
            action.update({'payload': self.__load_payload(payload)})

        button = {
            'action': action,
            'color': color
        }
        current_line.append(button)

    def add_line(self):
        if len(self.lines) == 10:
            if self.inline:
                raise TypeError('max lines: 6')
            else:
                raise TypeError('max lines: 10')
        self.lines.append([])

    def get_current_line(self):
        return self.lines[-1]

    def get_keyboard(self):
        keyboard = self.keyboard.copy()
        if 'buttons' not in keyboard:
            keyboard.update({'buttons': self.lines})
        return json.dumps(keyboard, cls=EnumEncoder)

    @classmethod
    def get_empty_keyboard(cls):
        keyboard = cls(True)
        keyboard.keyboard['buttons'] = []
        return keyboard.get_keyboard()

    @classmethod
    def get_empty_inline(cls):
        keyboard = cls(False, True)
        keyboard.keyboard['buttons'] = []
        return keyboard.get_keyboard()


class Payload:
    def __init__(self, cmd, **kwargs):
        self.cmd = cmd
        self.args: dict = kwargs
        self.value = {'command': cmd}

    def get(self):
        if self.args:
            return {'command': self.cmd, 'args': self.args}
        else:
            return {'command': self.cmd}
