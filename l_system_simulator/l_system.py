""" This module applies rules and executes them
after all the replacements acceptable within bounding volume
"""

import random


class LSystemSimulator:
    """ Apply grammar rules and apply operators """
    def __init__(self, parser, initial_word: str, rule_list: dict, iterations: int):
        self.parser = parser
        self.produced_word = initial_word
        self.iterations = iterations
        self.rule_list = rule_list

    def produce(self):
        """ Swap operators according to the grammar rules """
        if self.iterations > 0:
            while self.iterations > 0:
                old_word = self.produced_word
                self.produced_word = ""
                for operator in old_word:
                    if operator in self.rule_list.keys():
                        applicable_rules = self.rule_list[operator]
                        rule = random.choice(applicable_rules)
                        self.produced_word += rule
                    else:
                        self.produced_word += operator
                self.iterations -= 1
        return self.produced_word

    def apply_operators(self):
        """ Apply operator """
        parser = self.parser
        for symbol in self.produced_word:
            operator = parser.map_symbol(symbol)
            operator()
