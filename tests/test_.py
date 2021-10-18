from unittest import TestCase
from app import app
from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
