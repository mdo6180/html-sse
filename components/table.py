from typing import List, Dict


newline = "\n"

def table_rows(rows: List[Dict]):
    return newline.join(
        f"""
        <tr>
            <td>{ row["book"] }</td>
            <td>{ row["author"] }</td>
            <td>{ row["node"] }</td>
        </tr>
        """ for row in rows
    )
