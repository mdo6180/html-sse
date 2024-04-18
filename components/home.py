def home_page():
    return """<html>
        <head>
            <meta charset="UTF-8">
            <title>Anacostia Console</title>
            
            <!-- Bulma CSS -->
            <link rel="stylesheet" href="/static/css/bulma.css">

            <!-- non-minified Htmx -->
            <script src="/static/js/htmx.js" type="text/javascript"></script>

            <!-- htmx SSE extension -->
            <script src="https://unpkg.com/htmx.org@1.9.12/dist/ext/sse.js"></script>

            <!-- minified _Hyperscript (Whole 9 Yards version) -->
            <script src="/static/js/_hyperscript_w9y.min.js"></script>
        </head>
        <body>
            <table class="table is-bordered" hx-ext="sse" sse-connect="/events">
                <thead>
                    <th>Book</th>
                    <th>Author</th>
                    <th>Node</th>
                </thead>
                <tbody hx-get="/rows" hx-trigger="sse:update" hx-target="this" hx-swap="beforeend"> 
                </tbody>
            </table>
        </body>
    </html>
    """