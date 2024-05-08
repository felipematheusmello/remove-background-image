from flask import Blueprint, jsonify, request, render_template, send_file
from rembg import remove
from PIL import Image
from io import BytesIO


bp_bkgd = Blueprint('background', __name__)

@bp_bkgd.route('', __name__, methods=['POST'])
def remove_background():
    try:
        file = request.files['file']

        if file.filename == '':
            return 'No file selected', 400
        if file:
            input_image = Image.open(file.stream)
            output_image = remove(input_image, post_process_mask=True)
            img_io = BytesIO()
            output_image.save(img_io, 'PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=f'{file.filename}.png')


    except Exception as e:
        return jsonify({'error': str(e)}), 400