index_view = """
<!DOCTYPE html>
<html>
   <head>
      <title>URL Shortener</title>
   </head>
   <body style="background-color:grey;">
        <h1 style="color: #585972; margin: 15px;">URL Shortener</h1>
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/shorten-url" method="post">
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=submit value="Shorten URL">
            <p><input type=hidden name=confirmed value=0>
        </form>
        </div>
    </body>
</html>
"""

index_view_w_response = """
<!DOCTYPE html>
<html>
   <head>
      <title>URL Shortener</title>
   </head>
   <body style="background-color:grey;">
        <h1 style="color: #585972; margin: 15px;">URL Shortener</h1>
        <div style="background-color: #707bb2; margin: 15px;; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/shorten-url" method="post">
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=submit value="Shorten URL">
            <br><br>
            <b><a href="{}">{}</a></b>
        </form>
        </div>
    </body>
</html>
"""

confirmation_view = """
<!DOCTYPE html>
<html>
   <head>
      <title>URL Shortener</title>
   </head>
   <body style="background-color:grey;">
        <h1 style="color: #585972; margin: 15px;">URL Shortener</h1>
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 400px">
        <form action="/shorten-url" method="post">
            <p>We weren't able to connect to <b style="color:blue">{}</b>. Please confirm your URL by retyping it below.
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=hidden name=confirmed value=1>
            <p><input type=submit value="Confirm URL">
        </form>
        <form action="/" method="get">
            <span style="color:red">
            <p><input style="color: red" type=submit value="Cancel">
            </span>
        </form>
        </div>
    </body>
</html>
"""
