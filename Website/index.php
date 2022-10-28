<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <title>Find New Music</title>
    <meta
      name="description"
      content="Music Miner is website that helps you find new small artists from various genres and countries. Discover new music while also helping out the smaller underground artists."
    />
    <link rel="stylesheet" href="style.css" />
    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HDZC42YWYV"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-HDZC42YWYV');
</script>
  </head>
  <body id="body">


    <script>
      function randsong() {
        let xhr = new XMLHttpRequest();
        xhr.open(
          "get",
          "https://yushyush17.pythonanywhere.com",
          {"Access-Control-Allow-Origin": true}
        );
        xhr.send();

        xhr.onload = function () {
            const data = JSON.parse(xhr.response);
            document.getElementById("artist_name").innerHTML =
            "Artist Name: " + data['Name'];
            document.getElementById("listeners").innerHTML =
            "Monthly Listeners: " + data['Monthly Listeners'];
            document.getElementById("link").action = data['link'];
            const link_bt = document.getElementById("link-bt");
            link_bt.value = "Artist's Spotify";
            link_bt.style.display = "block";
            document.getElementById("genres").innerHTML = "genres: " + randomItem[3];
            document.getElementById("finder").innerHTML = "Find Another Artist";
            document.getElementById("intro").innerHTML = "now go to the Artist's Spotify page and just start listening";
      }; }
    </script>
    <nav class="start-items">
      <p id="nav-heading" class="navbar">Music Miner</p>
      <a href="index.php" class="navbar" id="main">Main</a>
      <a href="about.php" class="navbar">About</a>
      <a href="contact.php" class="navbar">Contact</a>
    </nav>
    <h1 class="start-items">Music Miner</h1>
    <p id="intro" class="start-items">
      Find new songs, new genres and new artists with the click of a button
    </p>
    <button onclick="randsong()" type="button" id="finder" class="start-items">
      Find An Artist
    </button>
    <p id="artist_name"></p>
    <p id="listeners"></p>
    <p id="genres"></p>
    <form id="link" action="" target="_blank">
      <input type="submit" id="link-bt" value="" style="display: none" />
    </form>
    <p id="copy" class="start-items"><span>&copy;</span>Ayush Sharma</p>

  </body>
</html>
