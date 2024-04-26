from typing import List, Dict
from .table import table_rows



def home_page(rows: List[Dict]):
    # Note: the error "Error in event handler: Error: write after end" i've been encountering thus far was because <!DOCTYPE> was not on the first line
    return f"""
    <!DOCTYPE>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Anacostia Console</title>
            
            <!-- Bulma CSS -->
            <link rel="stylesheet" href="/static/css/bulma.css">

            <!-- non-minified Htmx -->
            <script src="/static/js/htmx.js" type="text/javascript"></script>

            <!-- htmx SSE extension -->
            <script src="/static/js/sse.js"></script>
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
