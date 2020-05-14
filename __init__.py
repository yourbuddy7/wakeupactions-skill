from mycroft import MycroftSkill, intent_file_handler


class Wakeupactions(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wakeupactions.intent')
    def handle_wakeupactions(self, message):
        self.speak_dialog('wakeupactions')


def create_skill():
    return Wakeupactions()

