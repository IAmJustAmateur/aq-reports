from datetime import timedelta
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
def replace_dict_key(d: dict, old: str, new: str) -> dict:
    '''
    replace old dictionary key with new one
    if old does not exist nothing happens
    '''
    try:
        d[new] = d[old]
        d.pop(old)
    except:
        pass
    return d

def set_color(cell, color):
    xml = ('<w:shd {} w:fill="' + color + '"/>').format(nsdecls('w'))
    shading_elm_1 = parse_xml(xml)
    cell._tc.get_or_add_tcPr().append(shading_elm_1)

def last_day_of_month(any_day):
        
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)

def delete_column(table, column_number):
    grid = table._tbl.find("w:tblGrid", table._tbl.nsmap)
    for cell in table.column_cells(column_number):
        cell._tc.getparent().remove(cell._tc)
    col_elem = grid[column_number]
    grid.remove(col_elem)

def delete_empty_column(table):
    column_number = 1
    while column_number <  len(table.columns):
        column_empty = True
        for row_number in range(1, (len(table.rows))):
            if table.cell(row_number, column_number).text != "":
                column_empty = False
                break
        if column_empty:
            delete_column(table, column_number)
        else:
            column_number += 1
            
