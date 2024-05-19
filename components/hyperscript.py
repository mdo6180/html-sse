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
            <button _="on click send hello to .hello_div">Send</button>
            <div>
                <div class="hello_div" _="on hello add .red to me on goodbye add .green to me">hello</div>
                <div class="hello_div" _="on hello add .green to me on goodbye add .red to me">goodbye</div>
            </div>
        </body>
    </html>
    """
