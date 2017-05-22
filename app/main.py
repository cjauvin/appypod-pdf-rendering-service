from appy.pod.renderer import Renderer
from flask import Flask, request, send_file
import json
import os
import uuid


PORT = 12345
WORK_DIR = '/tmp'
DEBUG = True

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_pdf_from_odt_template():
    """
    Receive an ODT template file and a JSON value file, perform the
    rendering to PDF with appy.pod, and return the resulting file.

    Input files:
      tmpl: ODT template
      values: JSON values to fill in

    Output file:
      pdf: resulting PDF file
    """

    assert 'tmpl' in request.files
    assert request.files['tmpl'].filename.endswith('.odt')
    assert 'values' in request.files

    values = json.load(request.files['values'])

    # generate unique name to avoid collisions
    name = str(uuid.uuid4())
    input_odt_path = os.path.join(WORK_DIR, '%s.odt' % name)
    output_pdf_path = os.path.join(WORK_DIR, '%s.pdf' % name)
    request.files['tmpl'].save(input_odt_path)

    ren = Renderer(
        input_odt_path, values, output_pdf_path,
        pythonWithUnoPath='/usr/bin/python3',
        overwriteExisting=True
    )
    ren.run()

    fn = '%s.pdf' % os.path.splitext(request.files['tmpl'].filename)[0]
    return send_file(
        output_pdf_path,
        mimetype='application/pdf',
        attachment_filename=fn,
        as_attachment=True
    )


@app.route('/test', methods=['GET'])
def test():
    return 'service is available'


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
