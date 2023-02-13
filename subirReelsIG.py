# Importar la librería necesaria
import instaloader

# Iniciar sesión en tu cuenta de Instagram
L = instaloader.Instaloader()
L.login("<tu_usuario>", "<tu_contraseña>")

# Seleccionar el archivo Reel que desees publicar
video_path = "ruta/a/tu/reel.mp4"

# Publicar el Reel, le puedes añadir hashstags, describir tu contenido, etc
L.upload_video(video_path, caption="Mirá este contenido y síguenos!", hashtag="#reels #instavideo")