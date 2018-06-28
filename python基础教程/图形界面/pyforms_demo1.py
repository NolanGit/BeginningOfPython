import pyforms
from functools import reduce
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pypinyin import pinyin, lazy_pinyin


class AutoFiller(BaseWidget):

    def __init__(self):
        super(AutoFiller, self).__init__('Auto filler')
        self._project = ControlCombo('项目')
        self._project.add_item('后台')
        self._project.add_item('山东药监')
        self._project.add_item('沈阳药监')

        self._product = ControlCombo('产品')
        self._product.add_item('食品日常检查')
        self._product.add_item('快速检验')

        self._level = ControlCombo('严重程度')
        self._level.add_item('3-平均', '3')
        self._level.add_item('1-关键', '1')
        self._level.add_item('2-严重', '2')
        self._level.add_item('4-较轻', '4')

        self._type = ControlCombo('缺陷类型')
        self._type.add_item('1-功能性', '1')
        self._type.add_item('3-易用性', '3')

        self._person = ControlText('责任者')

        self._button = ControlButton('确定')
        self._button.value = self.__buttonAction

        self.formset = [('_project', '_product'), ('_level', '_type'), ('_person', '_button')]

    def add_str(self, a, b):
        return a + b

    def __buttonAction(self):
        pinyin = lazy_pinyin(self._project.value)
        print(pinyin)
        print(reduce(self.add_str, pinyin))


if __name__ == "__main__":
    pyforms.start_app(AutoFiller)
