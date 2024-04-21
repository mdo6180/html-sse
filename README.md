# htmx SSE
This is me playing around with the [htmx server-sent-events extension](https://v1.htmx.org/extensions/server-sent-events/). I built two simple examples, sse.py and callback.py, that illustrates how to use FastAPI to build a backend that sends html snippets to the frontend via server-sent events.

### Using SSE only:
sse.py is a simple example of how to interact with htmx using just server-sent events. The server simply formats an html snippet, sends it to the frontend via SSE, and the snippet is then inserted into the DOM via htmx's SSE extension.

### Triggering Server Callbacks:
callback.py illustrates how to trigger server callbacks with `hx-trigger="sse:EventName"`. 
The server sends an event to the frontend with the name `EventName`. 
The attribute `hx-trigger="sse:EventName"` then triggers a GET request to an endpoint `\chat-row`. The server then responds to the GET request with an html snippet which is then recieved by htmx and inserted into the DOM. 

### Lessons learned:
1. HTML snippets must be formatted properly before being sent as a message in an event. See the `format_html_for_sse` function in sse.py. Note: I had never used SSEs before trying out the extension.
2. An SSE-only approach is simpler because it requires fewer endpoints and fewer html snippets.
3. Triggering server callbacks is more flexible; a few reasons why:
    1. Suppose we want to add two triggers, one to trigger on load and one that responds to an SSE. In this scenario, we could use the server callback approach with the attribute `hx-trigger="load, sse:EventName"`.
    2. According to the documentation, modifiers like `scroll` are not supported by the `hx-swap` attribute when it is used to control the swap strategy of the html snippet recieved by `sse-swap="EventName"`.
    3. You can use and reuse the same endpoint to do server callbacks for multiple events from multiple event sources.
