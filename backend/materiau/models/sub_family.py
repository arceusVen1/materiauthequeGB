from django.db import models
from .family import Family


class SubFamily(models.Model):

    constituent = models.CharField(max_length=255)
    ref_number = models.IntegerField(null=True, blank=True)
    family = models.ForeignKey(Family)

    @property
    def reference(self):
        return '{}-{}'.format(self.family, self.ref_number)

    def compute_and_save(self):
        self.ref_number = self.family.subfamily_set.count()
        self.save()

    def get_absolute_url(self):
        return u'/materiaux/sous-famille/{}'.format(self.reference)

    def __str__(self):
        return self.reference