index_view = """
        <div style="background-color: #707bb2; margin: 15px; border-radius: 5px; padding: 15px; width: 800px">
        <form action="/shorten-url" method="post">
            <p><input type=text name=url_to_shorten placeholder=" your url...">
            <p><input type=submit value="Shorten URL">
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

