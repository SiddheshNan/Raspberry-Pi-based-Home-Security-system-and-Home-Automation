from twilio.rest import Client
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
  cloud_name = "",
  api_key = "",
  api_secret = ""
)


upload = cloudinary.uploader.upload("admin.png")
print(upload['secure_url'])