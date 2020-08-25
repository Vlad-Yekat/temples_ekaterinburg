from django.utils.translation import ugettext_lazy as _

ALL_SEASONS = 'all'
WINTER = 'winter'
SPRING = 'spring'
SUMMER = 'summer'
AUTUMN = 'autumn'

SEASONS = (
    (ALL_SEASONS, _('All seasons')),
    (WINTER, _('Winter view')),
    (SPRING, _('Spring view')),
    (SUMMER, _('Summer view')),
    (AUTUMN, _('Autumn/fall view')),
)

