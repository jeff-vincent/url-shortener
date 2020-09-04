index_view = """
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 800px">
        <form action="/shorten-url" method="post">
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=submit value="Shorten URL">
            <p><input type=hidden name=confirmed value=0>
        </form>
        </div>
        """

index_view_w_response = """
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 800px">
        <form action="/shorten-url" method="post">
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=submit value="Shorten URL">
            <br><br>
            <b><a href="{}">{}</a></b>
        </form>
        </div>
        """

confirmation_view = """
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 800px">
        <form action="/shorten-url" method="post">
            <p>We weren't able to connect to <b>{}</b>. Please confirm your URL by retyping it below.
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=hidden name=confirmed value=1>
            <p><input type=submit value="Confirm URL">
        </form>
        <form action="/" method="get">
            <p><input type=submit value="Cancel">
        </form>
        </div>
        """
