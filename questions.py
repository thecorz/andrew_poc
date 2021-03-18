# Functions for showing questions 
import functools

import ipywidgets as widgets


class TwoBoxQuestion(object):
    def __init__(self, question_number, question_problem, answer1, out1, answer2, out2):
        self.question_number = question_number
        self.question_problem = question_problem
        self.answer1 = answer1
        self.answer2 = answer2
        
        button1 = widgets.Button(description="Check")
        button2 = widgets.Button(description="Check")
        button1.on_click(functools.partial(self.correction_function, box=0, answer=answer1, out=out1))
        button2.on_click(functools.partial(self.correction_function, box=1, answer=answer2, out=out2))
        
        self.q_widget = widgets.HBox([widgets.Label(f'({question_number})'), widgets.Label(question_problem), 
                                      widgets.VBox([widgets.HBox([widgets.Text(), 
                                                                   button1, 
                                                                   out1]), 
                                                     widgets.HBox([widgets.Text(), 
                                                                   button2, 
                                                                   out2])
                                                    ])
                                      ])

    def correction_function(self, b, box, answer, out):
        with out:
            out.clear_output()
            if self.q_widget.children[2].children[box].children[0].value == answer:
                print('CORRECT')
            else:
                print('Try again')

    def show(self):
        display(self.q_widget)
        
    def parse(self):
        return dict(box1=self.q_widget.children[2].children[0].children[0].value,
                    box2=self.q_widget.children[2].children[1].children[0].value)