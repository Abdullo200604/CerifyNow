import qrcode
from io import BytesIO
from django.core.files import File

def generate_qr(payload):
    img = qrcode.make(payload)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)  # MUHIM: File boshi!
    return File(buffer, name='qr.png')
