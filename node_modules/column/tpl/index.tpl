<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="/assets/ico/favicon.ico">

    <title>Home | Column</title>
    <!-- Bootstrap core CSS -->
    <link href="/assets/bootstrap-3.1.0/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="/assets/styles/column.css" rel="stylesheet">
  </head>

  <body id="home">
    <% include navbar.tpl %>

    <div class="container">
      <div class="column-header">
        <h1 class="column-title">Column</h1>
        <p class="lead column-description">磕首问路，码梦为生</p>
      </div>

      <div class="row">
        <div class="col-sm-8 blog-main">
          <ul>
          <% articles.forEach(function (article) { %>
            <li>
              <a href="articles/<%=article.title%>.html"><%=article.title%></a>
            </li>
          <% });%>
          </ul>
          <% include disqus.tpl %>
        </div>
        <div class="col-sm-3 col-sm-offset-1 column-sidebar">
          <% include sidebar.tpl %>
        </div>
      </div>
    </div><!-- /.container -->

    <% include footer.tpl %>
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/assets/scripts/jquery-1.10.2.min.js"></script>
    <script src="/assets/bootstrap-3.1.0/js/bootstrap.min.js"></script>
  </body>
</html>
