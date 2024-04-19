def chat_homepage():
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
        </head>
        <body hx-ext="sse" sse-connect="/event-source">
            <div hx-get="/chat-row" hx-trigger="sse:EventName" hx-swap="beforeend"></div>
        </body>
    </html>
    """

def chat_data(i: int):
    return f"""
    <div>Content to swap into your HTML page ({i}).</div>
    <div>More content to swap into your HTML page ({i}).</div>
    """