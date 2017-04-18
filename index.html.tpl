<!doctype html>
<html class="no-js" lang="">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title></title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.css" />
        <link rel="stylesheet" href="main.css" />
    </head>
    <body>
        <table>
            <tbody>
                {% for ad in ads %}
                    <tr data-link="{{ad.link}}">
                        <td><img src="{{ad.img}}"/></td>
                        <td>{{ad.price}}</td>
                        <td>
                            <h2>{{ad.title}}</h2>
                            <br/>
                            <div>
                                {{ad.desc}}
                            </div>
                        </td>
                        <td>{{ad.added}}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        <script src="main.js" type="text/javascript"></script>
    </body>
</html>