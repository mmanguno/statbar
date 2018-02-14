# statbar
an uebersicht statusbar widget that uses a client-server architecture


## What it is
An ubersicht widget for a statusbar. The front-end makes a curl call to a 
localserver. The localserver, backed by Flask, does what it needs (e.g. makes
calls to Spotify, performs shell commands, etc.).

## How to run it
1. Install the dependencies: 
   ```bash
   pip install -r requirements.txt
   ```
2. Setup Spotify credentials, so we can poll spotify. Fill out the 
   config.yaml.example, and rename it to "config.yaml". I followed the
   steps in the [spotipy docs][0]. This will require you to make an app
   as a Spotify dev. If you don't want to do this, just comment out the
   spotify stuff in the server code.

3. Run the server, preferably keeping it in a background process:
   ```bash
   python3 server.py&
   ```
   The first time it runs, it will open up your browser (or whatever 
   `$BROWSER` is configured in your shell), and ask you to authenticate. This
   won't be often.

4. Move `bar.coffee` into the widgets folder.

That's it.

## What's next
Cleaning up HTML, adding icons, prettifying in general, adding more status
elements, maybe making it clickable. *Make this documentation better because 
it's almost 3am.*

[0]: http://spotipy.readthedocs.io/en/latest/#authorized-requests