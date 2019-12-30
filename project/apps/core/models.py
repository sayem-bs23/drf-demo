from django.db import models


class Keyvalue(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Keyvalue"
        verbose_name_plural = "Keyvalues"

    def __unicode__(self):
        return '%s %s' % (self.key, self.value)
