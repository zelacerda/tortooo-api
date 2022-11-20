# tortooo-api

A minimalist spellchecker API used in the [tort.ooo] game.

## Instructions

1. Build image with `docker build -t spell .`;
2. Start API with `docker run --rm -e PORT=8000 -p 8000:8000 spell`;
3. Go to `localhost:8000/{word}` and see if {word} exists in the portuguese dictionary.

The spellchecker can correct the word by putting accents since in the tort.ooo game there isn't letters with accent.

Example: `localhost:8000/palavrao` will return `{ result: "palavrão" }`.