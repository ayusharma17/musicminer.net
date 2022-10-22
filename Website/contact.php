<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />

    <title>Music Miner</title>
  </head>
  <body>
    <nav>
      <p id="nav-heading">Music Miner</p>
      <a href="index.php" class="navbar" id="main">Main</a>
      <a href="about.php" class="navbar">About</a>
      <a href="contact.php" class="navbar">Contact</a>
    </nav>
    <h1>Contact</h1>
    <form id="fcf-form-id" class="fcf-form-class" method="post" action="contact-form-process.php">
          <div class="fcf-input-group">
              <input type="text" id="Name" name="Name" class="fcf-form-control" placeholder = "Name"required>
          </div>
      <div class="fcf-form-group">
          <div class="fcf-input-group">
              <input type="email" id="Email" name="Email" class="fcf-form-control" required placeholder="Email">
          </div>
          <div class="fcf-input-group">
              <textarea id="Message" name="Message" class="fcf-form-control" rows="10" maxlength="3000" placeholder="Enter Message" required></textarea>
          </div>
          <button type="submit" id="fcf-button" class="fcf-btn fcf-btn-primary fcf-btn-lg fcf-btn-block">Send</button>
      </div>
    </form>
    <p id = "copy"><span>&copy;</span>Ayush Sharma</p>
  </body>
</html>





