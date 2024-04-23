from typing import List, Dict
from .table import table_rows



def home_page(rows: List[Dict]):
    return f"""<html>
        <head>
            <meta charset="UTF-8">
            <title>Anacostia Console</title>
            
            <!-- Bulma CSS -->
            <link rel="stylesheet" href="/static/css/bulma.css">

            <!-- non-minified Htmx -->
            <script src="/static/js/htmx.js" type="text/javascript"></script>

            <!-- htmx SSE extension -->
            <script src="https://unpkg.com/htmx.org@1.9.12/dist/ext/sse.js"></script>
        </head>
        <body>
            <table class="table is-bordered">
                <thead>
                    <th>Book</th>
                    <th>Author</th>
                    <th>Node</th>
                </thead>
                <tbody hx-ext="sse" sse-connect="/events" sse-swap="UpdateEvent" hx-swap="beforeend"> 
                {table_rows(rows)}
                </tbody>
            </table>
        </body>
    </html>
    """
