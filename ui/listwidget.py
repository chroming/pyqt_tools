# -*- coding: utf-8 -*-

"""
带有添加item, 修改item text, 删除item方法的QListWidget子类

注意: 添加item及修改item text 均会使item变为修改状态, 单击或双击item即可退出此状态.

usage:

from listwidget import ListWidget

新建QListWidget:

new_list_widget = ListWidget(
                            add_action=add_button.clicked,  # 添加item信号
                            change_text_action=change_text_button_clicked,  # 改变item text信号
                            remove_action=remove_button.clicked,  # 删除item 信号
                            up_action=up_button.clicked,  # 上移当前item 信号
                            down_action=down_button.clicked  # 下移当前item 信号
                            )


给QListWidget实例添加方法:

new_list_widget = ListWidget(
                            widget=Qlistwidget,
                            add_action=add_button.clicked,  # 添加item信号
                            change_text_action=change_text_button_clicked,  # 改变item text信号
                            remove_action=remove_button.clicked,  # 删除item 信号
                            up_action=up_button.clicked,  # 上移当前item 信号
                            down_action=down_button.clicked  # 下移当前item 信号
                            )

"""

from PyQt4.QtGui import QListWidget, QListWidgetItem


class ListWidget(QListWidget):
    def __new__(cls, widget=None, *args, **kwargs):
        return widget if widget else super(ListWidget, cls).__new__(cls, *args, **kwargs)

    def __init__(self, widget=None, add_action=None, change_text_action=None, remove_action=None, up_action=None, down_action=None):
        super(ListWidget, self).__init__()
        #if widget:
        #    self = widget
        self.itemClicked.connect(self.click_action_connect)
        if add_action:
            add_action.connect(self.add_action_connect)
        if change_text_action:
            change_text_action.connect(self.rename_action_connect)
        if remove_action:
            remove_action.connect(self.remove_action_connect)
        if up_action:
            up_action.connect(self.up_action_connect)
        if down_action:
            down_action.connect(self.down_action_connect)

    def add_action_connect(self):
        new_item = QListWidgetItem()
        self.addItem(new_item)
        self.openPersistentEditor(new_item)

    def rename_action_connect(self):
        current_item = self.currentItem()
        self.openPersistentEditor(current_item)

    def remove_action_connect(self):
        item_row = self.currentRow()
        temp_item = self.takeItem(item_row)
        del temp_item

    def up_action_connect(self):
        current_cow = self.result_replacefrom_listwidget.currentRow()
        if current_cow != 0:
            up_text = self.result_replacefrom_listwidget.item(current_cow - 1).text()
            current_text = self.result_replacefrom_listwidget.item(current_cow).text()
            self.result_replacefrom_listwidget.item(current_cow - 1).setText(current_text)
            self.result_replacefrom_listwidget.item(current_cow).setText(up_text)
            self.result_replacefrom_listwidget.setCurrentItem(self.result_replacefrom_listwidget.item(current_cow - 1))

    def down_action_connect(self):
        current_cow = self.result_replacefrom_listwidget.currentRow()
        item_len = self.result_replacefrom_listwidget.count()
        if current_cow+1 < item_len:
            down_text = self.result_replacefrom_listwidget.item(current_cow + 1).text()
            current_text = self.result_replacefrom_listwidget.item(current_cow).text()
            self.result_replacefrom_listwidget.item(current_cow + 1).setText(current_text)
            self.result_replacefrom_listwidget.item(current_cow).setText(down_text)
            self.result_replacefrom_listwidget.setCurrentItem(self.result_replacefrom_listwidget.item(current_cow + 1))

    def click_action_connect(self, item):
        """
        关闭item编辑状态
        """
        self.widget.closePersistentEditor(item)