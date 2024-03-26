#!/usr/bin/python3
""" Test for Console """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import subprocess


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.storage = FileStorage()

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.console.onecmd("show BaseModel {}".format(output))
                output = mock_stdout.getvalue().strip()
                self.assertTrue(output)