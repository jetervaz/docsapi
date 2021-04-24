import io
import re

import base64

from docx import Document


def get_fields_from_template_file(template_file):
    """Retrieve fields available in template file."""
    doc = Document(template_file)
    doc_text = "\n".join([p.text for p in doc.paragraphs])
    field_re = re.compile('{{([^}}]*)}}')
    return field_re.findall(doc_text)


def decode_b64_to_stream(encoded_file):
    """Decode b64 encoded file to file stream."""
    decoded_file = base64.b64decode(encoded_file)
    template_file = io.BytesIO(decoded_file)
    return template_file


def get_fields_from_b64_file(encoded_file):
    """Retrieve fields from b64 encoded file."""
    template_file = decode_b64_to_stream(encoded_file)
    return get_fields_from_template_file(template_file)
