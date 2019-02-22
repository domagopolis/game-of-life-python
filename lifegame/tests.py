# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import json

from .models import World

class WorldMethodTests(TestCase):
    def setUp(self):
        self.name = 'test world'
        self.width = 100
        self.height = 100
        self.world = create_world(self.name, self.width, self.height, 30, 30)
        self.world.save()

    def test_has_alias(self):
        self.assertTrue(self.world.alias)

    def test_boundaries_set(self):
        self.assertEqual(self.world.height, self.height)
        self.assertEqual(self.world.width, self.width)

    def test_has_data(self):
        self.assertTrue(self.world.data)

    def test_data_has_boundaries(self):
        data = json.loads(self.world.data)
        columns = 0
        for column in data:
            columns += 1
            rows = 0
            for row in column:
                rows += 1
            self.assertEqual(rows, self.height)

        self.assertEqual(columns, self.width)

    def tearDown(self):
        self.world.delete()

def create_world(name, width, height, food_distribution, life_distribution):
    return World.objects.create(name=name, width=width, height=height)
