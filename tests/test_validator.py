#!/usr/bin/env python
# coding=utf-8

import unittest
import json
import os
from src.validator import Validator


class ValidatorTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_validatorNone(self):
        validator = Validator()
        validator.validate(None)
        self.assertFalse(validator.isValid)

    def test_validatorClass(self):
        validator = Validator()
        validator.validate(validator)
        self.assertFalse(validator.isValid)

    def test_validatorStrings(self):
        validator = Validator()
        validator.validate("")
        self.assertFalse(validator.isValid)

        validator = Validator()
        validator.validate(" ")
        self.assertFalse(validator.isValid)

        validator = Validator()
        validator.validate("8711a05v0f085")
        self.assertFalse(validator.isValid)

    def test_validatorInvalid(self):
        validator = Validator()
        validator.validate("7711205106085")
        self.assertFalse(validator.isValid)

    def test_validatorValid(self):
        validator = Validator()
        validator.validate(" 8711205106085")
        self.assertTrue(validator.isValid)

        validator = Validator()
        validator.validate("8711205106085 ")
        self.assertTrue(validator.isValid)

        validator = Validator()
        validator.validate("8711205106085")
        self.assertTrue(validator.isValid)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(exit=False)
