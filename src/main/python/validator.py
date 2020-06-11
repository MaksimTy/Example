from PyQt5.QtGui import QIntValidator, QRegExpValidator, QValidator
from PyQt5.QtCore import QRegExp


class Validator:

    minimumRow = 1
    maximumRow = 1048576
    minimumCol = "A"
    maximumCol = "XFD"
    numberPattern = "\\d+"
    letterPattern = "[a-zA-Z]+"

    def __init__(self, widget,  button, statusbar, sender=None):
        self.widget = widget
        self.button = button
        self.statusbar = statusbar
        self.sender = sender
        # результаты валидации каждого метода
        self.result = {"number": False, "letter": False, "row": False, "col": False}

    def isValid(self):
        return not list(self.result.values()).__contains__(True)

    def buttonSwitcher(self, param, message):
        if param == QValidator.Acceptable:
            self.button.setHidden(False)
            self.statusbar.clearMessage()
        else:
            self.button.setHidden(False)
            self.statusbar.showMessage(message)
        return param

    def numberValidator(self):
        validator = QRegExpValidator(QRegExp(self.numberPattern))
        message = "Ошибка в индексах строк. Допустимы только цифры."
        result = validator.validate(self.widget.text(), 0)
        if self.buttonSwitcher(result[0], message) != QValidator.Acceptable:
            self.result["number"] = True
            return result[0]

    def letterValidator(self):
        validator = QRegExpValidator(QRegExp(self.letterPattern))
        message = "Ошибка в индексах столбцов. Допустимы только буквы латинского алфавита."
        result = validator.validate(self.widget.text(), 0)
        if self.buttonSwitcher(result[0], message) != QValidator.Acceptable:
            self.result["letter"] = True
            return result[0]

    def rowValidator(self):
        if self.numberValidator() is not None:
            return self.numberValidator()
        minimum = self.minimumRow if self.sender.text() == "" else int(self.sender.text())
        validator = QIntValidator(minimum, self.maximumRow)
        result = (validator.validate(self.widget.text(), 0))
        message = "Недопустимый диапазон строк!"
        if self.buttonSwitcher(result[0], message) != QValidator.Acceptable:
            self.result["row"] = True
            return result[0]

    def colValidator(self):
        if self.letterValidator() is not None:
            return self.letterValidator()
        minimum = self.letterIndexToIntValue(self.minimumCol) \
            if self.sender.text() == "" \
            else self.letterIndexToIntValue(self.sender.text())
        validator = QIntValidator(minimum, self.letterIndexToIntValue(self.maximumCol))
        result = validator.validate(str(self.letterIndexToIntValue(self.widget.text())), 0)
        message = "Недопустимый диапазон столбцов!"
        if self.buttonSwitcher(result[0], message) != QValidator.Acceptable:
            self.result["col"] = True
            return result[0]

    # Метод возвращает индекс сочетания латинских букв в верхнем регистре.
    # Индекс расчитывается как число в 24ричной системе.
    @staticmethod
    def letterIndexToIntValue(characters):
        letters = characters.upper()
        a = ord("A") - 1
        z = ord("Z") - a
        unicodes = [(ord(letter) - a) for letter in letters]
        alphabet = [*range(1, z + 1)]
        unicodes = list(filter(lambda code: code in alphabet, unicodes))
        unicodes.reverse()
        value = 0
        for i in range(len(unicodes)):
            value += pow(z, i) * unicodes[i]
        return value



