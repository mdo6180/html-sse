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
                <div class="event_div" 
                    _=" on HelloEvent from EventStream
                            log it 
                            remove .green from me
                            add .red to me 
                        end
                        on GoodbyeEvent from EventStream
                            log it
                            remove .red from me
                            add .green to me
                        end">event1</div>
                <div class="event_div" 
                    _=" on HelloEvent from EventStream 
                            remove .red from me
                            add .green to me 
                        end
                        on GoodbyeEvent from EventStream 
                            remove .green from me
                            add .red to me
                        end">event2</div>
            </div>
        </body>
    </html>
    """
