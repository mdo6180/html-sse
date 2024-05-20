def homepage():
    return """
    <!DOCTYPE>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Anacostia Console</title>

            <link rel="stylesheet" href="/static/css/hyperscript.css">
            
            <!-- non-minified Htmx -->
            <script src="/static/js/htmx.js" type="text/javascript"></script>

            <!-- htmx SSE extension -->
            <script src="/static/js/sse.js"></script>

            <!-- minified _Hyperscript (Whole 9 Yards version) -->
            <script src="/static/js/_hyperscript_w9y.min.js"></script>
        </head>
        <body>
            <div _="eventsource EventStream from /event-source
                        on open
                            log 'event source connected'
                        end
                    end">
                <div _="on HelloEvent from EventStream toggle .red on me">event1</div>
                <div _="on GoodbyeEvent from EventStream toggle .green on me">event2</div>
            </div>
        </body>
    </html>
    """
