lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]


def clean_customer(raw):

    fields = raw.split(';')

    if len(fields) != 4:
        return None

    name = fields[0].strip().title()
    email = fields[1].strip().lower()
    phone = fields[2].strip()
    city = fields[3].strip().title()

    if name == "":
        return None

    words = name.split()

    for word in words:
        if not word.isalpha():
            return None

    if city == "":
        return None

    if email.count('@') != 1:
        return None

    parts = email.split('@')

    username = parts[0]
    domain = parts[1]

    if username == "":
        return None

    if '.' not in domain:
        return None

    if domain.startswith('.') or domain.endswith('.'):
        return None

    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')

    if phone.startswith('+91'):
        phone = phone[3:]

    elif len(phone) == 12 and phone.startswith('91'):
        phone = phone[2:]

    if len(phone) != 10:
        return None

    if not phone.isdigit():
        return None

    if phone[0] not in '6789':
        return None

    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }

rejected = 0

for record in lines:

    result = clean_customer(record)

    if result is not None:
        print(result)

    else:
        rejected += 1

print("Rejected:", rejected)