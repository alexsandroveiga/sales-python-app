from terminaltables import SingleTable

def adaptTable (title: str, headers: list[str], rows):
  table_data = [
    headers
  ]
  for row in rows:
    table_data.append(row.values())
  table = SingleTable(table_data, title)
  print('\n' + table.table)