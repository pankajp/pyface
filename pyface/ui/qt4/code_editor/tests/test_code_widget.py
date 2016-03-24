#------------------------------------------------------------------------------
# Copyright (c) 2016, Enthought Inc
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license.
#
# Author: Enthought Inc
# Description: <Enthought pyface code editor>
#------------------------------------------------------------------------------

# Standard library imports.
import unittest

# System library imports.
from pyface.qt import QtCore, QtGui
from pyface.qt.QtTest import QTest

# Enthought library imports.


# Local imports.
from pyface.ui.qt4.code_editor.code_widget import CodeWidget, AdvancedCodeWidget


class TestCodeWidget(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.qapp = QtGui.QApplication.instance() or QtGui.QApplication([])

    def tearDown(self):
        self.qapp.processEvents()

    def test_readonly_editor(self):
        cw = CodeWidget(None)
        text = 'Some\nText'
        cw.setPlainText(text)

        def check(typed, expected):
            cursor = cw.textCursor()
            cursor.setPosition(0)
            cw.setTextCursor(cursor)
            QTest.keyClicks(cw, typed)
            self.assertEqual(cw.toPlainText(), expected)

        cw.setReadOnly(True)
        check('More', text)

        cw.setReadOnly(False)
        check('Extra', 'Extra' + text)

    def test_readonly_replace_widget(self):
        acw = AdvancedCodeWidget(None)
        text = 'Some\nText'
        acw.code.setPlainText(text)
        acw.show()

        def click_key_seq(widget, key_seq):
            if not isinstance(key_seq, QtGui.QKeySequence):
                key_seq = QtGui.QKeySequence(key_seq)
            try:
                first_key = key_seq[0]
            except IndexError:
                return False
            key = QtCore.Qt.Key(first_key & ~QtCore.Qt.KeyboardModifierMask)
            modifier = QtCore.Qt.KeyboardModifier(
                first_key & QtCore.Qt.KeyboardModifierMask)
            QTest.keyClick(widget, key, modifier)
            return True

        acw.code.setReadOnly(True)
        if click_key_seq(acw, QtGui.QKeySequence.Find):
            self.assertTrue(acw.find.isVisible())
            acw.find.hide()

        acw.code.setReadOnly(False)
        if click_key_seq(acw, QtGui.QKeySequence.Find):
            self.assertTrue(acw.find.isVisible())
            acw.find.hide()

        acw.code.setReadOnly(True)
        if click_key_seq(acw, QtGui.QKeySequence.Replace):
            self.assertFalse(acw.replace.isVisible())

        acw.code.setReadOnly(False)
        if click_key_seq(acw, QtGui.QKeySequence.Replace):
            self.assertTrue(acw.replace.isVisible())
        acw.replace.hide()
        self.assertFalse(acw.replace.isVisible())


if __name__ == '__main__':
    unittest.main()
