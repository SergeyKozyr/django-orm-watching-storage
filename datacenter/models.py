from django.db import models
from django.utils.timezone import localtime

from datacenter.constants import HOUR_AS_MINUTES, MINUTE_AS_SECONDS


class Passcard(models.Model):
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=True)
  passcode = models.CharField(max_length=200, unique=True)
  owner_name = models.CharField(max_length=255)

  def __str__(self):
    if self.is_active:
      return self.owner_name
    return f'{self.owner_name} (inactive)'


class Visit(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
  entered_at = models.DateTimeField()
  leaved_at = models.DateTimeField(null=True)

  def __str__(self):
    return "{user} entered at {entered} {leaved_at}".format(
        user=self.passcard.owner_name,
        entered=self.entered_at,
        leaved_at="left at " + str(self.leaved_at) if self.leaved_at else "did not leave"
    )

  def get_duration(self):
    current_time = localtime()
    local_enter_time = localtime(value=self.entered_at)
    local_leave_time = localtime(value=self.leaved_at)

    if not self.leaved_at:
      delta = current_time - local_enter_time
    else:
      delta = local_leave_time - local_enter_time
    return delta

  def format_duration(self, duration):
    total_seconds = duration.total_seconds()
    mins, secs = divmod(total_seconds, MINUTE_AS_SECONDS)
    hours, mins = divmod(mins, HOUR_AS_MINUTES)
    return f'{hours:.0f}:{mins:.0f}:{secs:.0f}'

  def is_long(self, minutes=60):
    duration = self.get_duration().total_seconds()
    duration_in_minutes = duration / MINUTE_AS_SECONDS
    return duration_in_minutes > minutes