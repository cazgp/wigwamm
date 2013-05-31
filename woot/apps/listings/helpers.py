KITCHEN_TYPES = (
    ('1', 'Open-plan'),
    ('2', 'Separate'),
)

ON_PARKING_TYPES = (
    ('1', 'None'),
    ('2', 'Free'),
    ('3', 'Permit'),
)

OFF_PARKING_TYPES = (
    ('1', 'None'),
    ('2', 'Drive'),
    ('3', 'Single garage'),
    ('4', 'Double garage'),
)

HEATING_TYPES = (
    ('1', 'Electric heating'),
    ('2', 'Gas heating'),
    ('3', 'Oil heating'),
)

GLAZING_TYPES = (
    ('1', 'Single glazed'),
    ('2', 'Double glazed'),
    ('3', 'Triple glazed'),
)

GLAZING_MATERIAL = (
    ('1', 'Timber windows'),
    ('2', 'UPVC windows'),
)

LAST_MONTHS = (
    ('1', 'Less than 1 month ago'),
    ('2', 'Less than 1 year ago'),
    ('3', '2+ years ago'),
)
PET_TYPES = (
    ('1', 'Pets allowed'),
    ('2', 'Caged pets only'),
    ('3', 'No pets allowed'),
)

AGREEMENT = (
    ('1', '6 months'),
    ('2', '12 months'),
    ('3', '24 months'),
)

BROADBAND = (
    ('1', 'Bills included'),
    ('2', 'Available'),
    ('3', 'Unavailable'),
)

DEPOSIT = (
    ('1', '1 month'),
    ('2', '6 weeks'),
    ('3', '2 months'),
)

COUNCIL_TAX = (
    ('1', 'A'),
    ('2', 'B'),
    ('3', 'C'),
    ('4', 'D'),
    ('5', 'E'),
    ('6', 'F'),
    ('7', 'G'),
)

floors = ['B', 'G'] + range(1, 41)
FLOORS = [(str(x), x) for x in floors]

MANAGED_BY = (
    ('1', 'Managed by agent'),
    ('2', 'Managed by landlord'),
)

BACK_GARDEN_TYPES = (
    ('1', 'None'),
    ('2', 'Balcony'),
    ('3', 'Patio'),
    ('4', 'Small'),
    ('5', 'Medium'),
    ('6', 'Large'),
)

FRONT_GARDEN_TYPES = (
    ('1', 'None'),
    ('2', 'Drive'),
    ('3', 'Patio'),
    ('4', 'Small'),
    ('5', 'Large'),
)

LIST_CHOICES = (
    ('r', 'rightmove'),
    #('z', 'zoopla'),
    #('g', 'gumtree'),
    #('c', 'craig\'s list'),
)

photo_order = [
    'living-room',
    'kitchen',
    'bedroom-1',
    'bedroom-2',
    'bedroom-3',
    'bedroom-4',
    'bedroom-5',
    'bedroom-6',
    'bathroom-1',
    'bathroom-2',
    'bathroom-3',
    'bathroom-4',
    'bathroom-5',
    'bathroom-6',
    'additional-room-1',
    'additional-room-2',
    'additional-room-3',
    'exterior',
    'floorplan',
]
