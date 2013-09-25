#!/usr/local/bin/python

import readline
readline.parse_and_bind("tab: complete")

class ARLCompleter:
    def __init__(self,logic):
        self.logic = logic

    def traverse(self,tokens,tree):
        if tree is None:
            return []
        elif len(tokens) == 0:
            return []
        if len(tokens) == 1:
            return [x+' ' for x in tree if x.startswith(tokens[0])]
        else:
            if tokens[0] in tree.keys():
                return self.traverse(tokens[1:],tree[tokens[0]])
            else:
                return []
        return []

    def complete(self,text,state):
        try:
            tokens = readline.get_line_buffer().split()
            if not tokens or readline.get_line_buffer()[-1] == ' ':
                tokens.append(text)
            results = self.traverse(tokens,self.logic) + [None]
            return results[state]
        except Exception,e:
            print e

logic = {
    'build':
            {
            'barracks':None,
            'bar':None,
            'generator':None,
            'lab':None
            },
    'train':
            {
            'riflemen':None,
            'rpg':None,
            'mortar':None
            },
    'research':
            {
            'armor':None,
            'weapons':None,
            'food':None
            }
    }

completer = ARLCompleter(logic)
readline.set_completer(completer.complete)

line = raw_input('prompt> ')
