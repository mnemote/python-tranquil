class BaseContext(object):
    """All contexts derive from this class"""
    
    def __init__(self, request):
        self.request = request
        
    
class DummyContext(BaseContext):
    
    def serialize(self):
        return None
    
    
class ProcessableContext(BaseContext):
    """Defines the methods which navigate the Tranquil request."""
    
    def process_action_list(self, action_list):
    
        new = self
        for action in action_list:
            if type(action) is dict:
                new = new.process_action_group(action)
            elif type(action) is list:
                new = new.action(*action)
            else:
                new = new.action(action)
    
        if isinstance(new, BaseContext):
            return new.serialize()
        else:
            return new
    
    
    def process_action_group(self, action_group):
    
        return dict([
            (label, self.process_request(action))
            for label, action in action_group.items()
        ])
    
    
    def process_request(self, actions):
    
        if type(actions) is dict:
            return self.process_action_group(actions)
    
        elif type(actions) is list:
            return self.process_action_list(actions)
    
        elif type(actions) in (str, unicode):
            return self.process_action_list([[actions]])
    
        else:
            raise NotImplementedError()

    
class ActionContext(ProcessableContext):
    
    def action(self, name, *params):
        """Despatches actions off to action_* methods, which should
        return either a context or some data"""

        action_method_name = 'action_%s' % name
        if hasattr(self, action_method_name):
            return getattr(self, action_method_name)(*params)
        raise NotImplementedError("action %s not found in %s.%s" % (name, self.__class__.__name__, action_method_name))


class MultiContext(ActionContext):
    
    _registry = {}
    
    @classmethod
    def register(cls, action_name):
        
        def wrapper(context_class):
            cls._registry[action_name] = context_class
            #setattr(cls, 'action_%s' % action_name, lambda r: context_class(r))
            return context_class
        return wrapper
    
    def action(self, name):
        try:
            action_context_class = self._registry[name]
        except KeyError:
            raise NotImplementedError("action %s not registered in %s" % (name, self.__class__.__name__))
        
        return action_context_class(self.request)
