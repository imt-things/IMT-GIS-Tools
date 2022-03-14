from xml.etree import ElementTree
from pathlib import Path

out_file = Path('event_gdb/test.md')

in_file = Path('event_gdb/event_gdb_schema.xml')
print(in_file.resolve())
xml = ElementTree.ElementTree(file=in_file)

print(out_file)

output = '<details>\n<summary>\n\nDomains\n</summary>\n\n'

for domain in xml.findall('WorkspaceDefinition/Domains/Domain'):
    output += f'## {domain.find("DomainName").text}\n'
    output += '### Values:\n'
    for values in list(domain.findall('CodedValues/CodedValue')):
        for val in list(values):
            if val.tag == 'Name':
                output += f'- {val.tag}: {val.text}\n'
            else:
                output += f'  - {val.tag}: {val.text}\n'
output += '</details>\n\n'

output += '# Tables/Fields\n'

# Define attributes to write and do so
attribs_to_write = 'Type IsNullable Length Precision Required DomainFixed AliasName DefaultValue Domain'.split()

for field in xml.findall('WorkspaceDefinition/DatasetDefinitions/DataElement'):
    output += f'## {field.find("Name").text}\n'
    for field in list(field.findall('Fields/FieldArray/Field')):
        for attrib in list(field):
            if attrib.tag == 'Name':
                output += f'### {attrib.text}\n'
            elif attrib.tag == 'Domain':
                # Todo: Would be cool if this linked to the domain
                output += f'- DomainName: {field.find("Domain/DomainName").text}\n'
            elif attrib.tag in(attribs_to_write):
                output += f'- {attrib.tag}: {attrib.text}\n'



output += '# Subtypes'

with out_file.open('w') as out:
    out.write(output)
