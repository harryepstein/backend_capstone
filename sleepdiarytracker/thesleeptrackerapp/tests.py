# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from thesleeptrackerapp.models import MorningSleepData
from datetime import time, timedelta

# Create your tests here.

class TotalSleepTimeDiff(TestCase):
  def test_diff_total_sleep_time(self):
    msd = MorningSleepData()
    msd.bedtime = time(hour=12, minute=00, second=00, microsecond=123456)
    msd.exit_bed_time = time(hour=7, minute=00, second=00, microsecond=123456)
    self.assertEquals(timedelta(hours=5), msd.total_sleep_time_differece())
