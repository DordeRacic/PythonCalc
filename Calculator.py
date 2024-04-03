import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
    
        
        
        self.show()
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        
        #Creating the buttons
        self.results_area = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter')
        btn_result.clicked.connect(self.func_result)  # Connect to func_result
        btn_clear = qtw.QPushButton('C', clicked = self.clearCalc)
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_minus= qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_prod = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_div = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))
        
        #Adding the buttons to the layout
        container.layout().addWidget(self.results_area,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn_9,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_7,2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(btn_6,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_4,3,2)
        container.layout().addWidget(btn_minus,3,3)
        container.layout().addWidget(btn_3,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_1,4,2)
        container.layout().addWidget(btn_0,5,0,1,3)
        container.layout().addWidget(btn_prod,4,3)
        container.layout().addWidget(btn_div,5,3)
        self.layout().addWidget(container)
        
    def num_press(self,key_nunmber):
        self.temp_nums.append(key_nunmber)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.results_area.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.results_area.setText(temp_string)
            
    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums= []
        self.results_area.setText(''.join(self.fin_nums))
    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.results_area.setText(fin_string)
    def clearCalc(self):
        self.results_area.clear()
        self.temp_nums.clear()
        self.fin_nums.clear()
        

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion')) #apply a certain style
app.exec()
