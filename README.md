# Base64-HL
A quick attempt at Base64 transcoding within Discord using [Hikari](https://github.com/hikari-py/hikari), and the [Lightbulb](https://github.com/tandemdude/hikari-lightbulb) command handler for Hikari.

Just a quick heads-up, but I had never touched Python or coded anything until I put this together out of boredom in early 2023. I'm releasing this nearly three months later with absolutely no review. It's probably very bad, and I apologize for that.
## Usage 
**This code requires Hikari-Lightbulb to function.** If your Bot is running on plain Discord.py, this will not work. This also assumes your Bot is already functional and online.

Using this module is as easy as dropping the blocks into your existing code, provided you structure it appropriately. A functioning example can be found in `example.py`.
## Features

- Customizable string recognition (https://* by default)
- Responds with transcoded string
- Slash command encoding & decoding


## Disclaimer

Due to the nature of Base64, this module can only match against a declared string encoded in Base64. By default this is `aHR0cHM6Ly9` or `https://`. You may declare multiple strings at a time to meet your needs, but it is not smart or worth my time to program this Bot to seek and reply to any potential Base64 encoded string.

Users should understand the risk of utilizing this module in larger servers, or within trusted Bots. Depending on your implementation, bad actors can use this functionality to serve unsecure or malicious links in chat via community trusted Bots. I am not responsible for any harm/damages caused by ineptitude, bad actors, or insecure implementation.


## Links

- License: [MIT](https://choosealicense.com/licenses/mit/)