from pypresence import Presence

client_id = "959012812208898068"
RPC = Presence(client_id)
RPC.connect()

while True:
  RPC.update(
    large_image = "a_ba3110fdd51d4dd8226203e0845a5bfa",
    large_text = "ITz_Developer",
    details = "Interested in",
    state = "Gaming/Programming",
    buttons = [{"label": "Join us!", "url": "https://discord.gg/PAayag54"}]
)