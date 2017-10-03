import logging
import queue

log = logging.getLogger(__name__)


class Action(object):
    def __init__(self, func=None, args=[], kwargs={}):
        super(Action, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, *self.kwargs)


class ActionQueue(object):
    ID = 0

    def __init__(self):
        super(ActionQueue, self).__init__()
        self.queue = queue.Queue()
        self.id = ActionQueue.ID
        ActionQueue.ID += 1

    def add(self, action, args):
        pass

    def execute(self):
        pass
