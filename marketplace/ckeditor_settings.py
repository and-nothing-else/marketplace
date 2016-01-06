
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo'],
            ['Format', 'PasteText', 'PasteFromWord'],

            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['Link', 'Unlink', 'Anchor', 'Image'],
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks', 'align'],
                'items': ['NumberedList', 'BulletedList', '-',
                          'Outdent', 'Indent', '-', 'Blockquote']
            },
            ['Source'],
            ['Maximize'],
        ],
        'width': '100%',
        'forcePasteAsPlainText': True
        # 'enterMode': 2,
    },
    'minimal': {
        'height': 100,
        'toolbar': [
            ['RemoveFormat', 'PasteText', 'PasteFromWord'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['Link', 'Unlink', 'Anchor', 'Image'],
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks', 'align'],
                'items': ['NumberedList', 'BulletedList', '-',
                          'Outdent', 'Indent', '-', 'Blockquote']
            },
            ['Source'],
            ['Maximize'],
        ],
        'width': '100%',
        'forcePasteAsPlainText': True
        # 'enterMode': 2,
    },
}
