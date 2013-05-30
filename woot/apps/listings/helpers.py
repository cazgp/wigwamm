KITCHEN_TYPES = (
    (1, 'Open-plan'),
    (2, 'Separate'),
)

PARKING_TYPES = (
    (1, 'garage'),
    (2, 'double'),
    (3, 'single'),
)

HEATING_TYPES = (
    (1, 'gas'),
    (2, 'oil'),
    (3, 'electric'),
)

GLAZING_TYPES = (
    (1, 'single'),
    (2, 'double'),
    (3, 'triple'),
)

GLAZING_MATERIAL = (
    (1, 'timer'),
    (2, 'UPVC'),
)

LAST_MONTHS = (
    (1, '1 month'),
    (2, '12 months'),
    (3, '24 months'),
)

DEPOSIT = (
    (1, '1 month'),
    (2, '6 weeks'),
    (3, '2 months'),
)

COUNCIL_TAX = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E'),
    (6, 'F'),
    (7, 'G'),
)

floors = ['B', 'G'] + range(1, 41)
FLOORS = zip(floors, floors)

MANAGED_BY = (
    (1, 'agent'),
    (2, 'landlord'),
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
