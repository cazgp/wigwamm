import zipfile

from datetime import datetime

from django.conf import settings
from django.core.files import File
from django.db.models import CharField
from django.template import Context, Template
from django.template.loader import get_template

def model_to_dict(instance, fields=None, exclude=None):
    """
    Returns a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, only the named
    fields will be included in the returned dict.

    ``exclude`` is an optional list of field names. If provided, the named
    fields will be excluded from the returned dict, even if they are listed in
    the ``fields`` argument.
    """
    opts = instance._meta
    data = {}
    for f in opts.fields:
        if not f.editable:
            continue
        if fields and not f.name in fields:
            continue
        if exclude and f.name in exclude:
            continue
        if f.choices:
            attr = "get_%s_display" % f.name
            value = getattr(instance, attr)()
        else:
            value = f.value_from_object(instance)
        data[f.name] = value
    return data

def create_rightmove(listing):
  agent_ref = 99
  address_1 = listing.address_1
  address_2 = listing.address_2
  town = listing.town

  # The last three digits of the postcode is *always* postcode_2
  postcode = listing.postcode.replace(' ', '').upper()
  postcode_1 = postcode[:-3]
  postcode_2 = postcode[-3:]

  # For the features, this is arbitrary, but number of bedrooms, number of
  # bathrooms, and type of heating
  feature_1 = "%s bedroom" % listing.bedrooms
  feature_2 = "%s bathroom" % listing.bathrooms
  feature_3 = listing.get_heating_display()

  # The summary again is quite arbitrary
  summary = "A %s bedroom located in the lovely area of %s." % (listing.bedrooms, listing.town)

  # The description is all the features formatted and bundled up
  t = get_template('listings/description.html')
  description = t.render(Context({
      'listing': model_to_dict(listing),
  })).strip('\n')

  # The branch ID is something which needs getting somehow
  branch_id = '99xx99'

  # This may be dynamic in the future, but for now it's available
  status_id = 0

  bedrooms = listing.bedrooms
  price = listing.price

  # The type of property
  prop_sub_id = listing.get_property_type_display()

  # Form the display address
  addresses = [address_1]
  if address_2: addresses.append(address_2)
  postcode = "%s %s" % (postcode_1, postcode_2)
  addresses.extend([town, postcode])
  display_address = ", ".join(addresses)

  # Assume always publish
  published_flag = 1

  let_date_available = listing.move_in_date
  let_furn_id = 0 if listing.furnished else 2

  # Assume always lettings
  trans_type_id = 2

  # Grab the photos
  photos = listing.listingphoto_set.all()

  rightmove_blm = get_template('listings/rightmove.blm')
  context = Context({
      'AGENT_REF': agent_ref,
      'ADDRESS_1': address_1,
      'ADDRESS_2': address_2,
      'TOWN': town,
      'POSTCODE_1': postcode_1,
      'POSTCODE_2': postcode_2,
      'FEATURE_1': feature_1,
      'FEATURE_2': feature_2,
      'FEATURE_3': feature_3,
      'SUMMARY': summary,
      'DESCRIPTION': description,
      'BRANCH_ID': branch_id,
      'STATUS_ID': status_id,
      'BEDROOMS': bedrooms,
      'PRICE': price,
      'PROP_SUB_ID': prop_sub_id,
      'DISPLAY_ADDRESS': display_address,
      'PUBLISHED_FLAG': published_flag,
      'LET_DATE_AVAILABLE': let_date_available,
      'LET_FURN_ID': let_furn_id,
      'TRANS_TYPE_ID': trans_type_id,
      'photos': photos,
  })

  # Create the zip file
  today = datetime.today()
  seq_no = today.strftime("%H%M")
  zip_file_name = "%s/tmp/%s.zip" % (settings.DJANGO_ROOT, branch_id)
  blm_file_name = "%s_%s%s.blm" % (branch_id, today.strftime("%Y%m%d"), seq_no)
  blm = rightmove_blm.render(context)
  with zipfile.ZipFile(zip_file_name, "w") as z:
      z.writestr(blm_file_name, blm)
      for index, photo in enumerate(photos):
          filetype = photo.photo.name.split(".")[-1]
          zip_photo_name = "%s_IMG_%02d.%s" % (agent_ref, index, filetype)
          z.write(photo.photo.path, zip_photo_name)
