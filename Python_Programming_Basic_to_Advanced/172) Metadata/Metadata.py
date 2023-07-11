from importlib import metadata

print(metadata.version('pip'))

metadados_pip = metadata.metadata('pip')

print(list(metadados_pip))
"""
['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author',
'Author-email', 'License', 'Project-URL', 'Project-URL', 'Project-URL',
'Platform', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python',
'License-File', 'Description']
"""
# print(metadados_pip)
# Mostra a descrição completa

print(metadados_pip['Project-URL'])
# Documentation, https://pip.pypa.io

print(len(metadata.files('pip')))

# pip install django
print(metadata.requires('django'))
